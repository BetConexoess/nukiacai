#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit-assets.py — Nu Ki Açaí Asset Auditor
Varre Downloads e o projeto, classifica cada arquivo e gera relatório.
NÃO modifica, move ou apaga nenhum arquivo.
"""

import json
import csv
import os
import sys
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOWNLOADS_DIR = Path.home() / "Downloads"
REPORTS_DIR = PROJECT_ROOT / "reports"

SCAN_DIRS = [
    DOWNLOADS_DIR,
    PROJECT_ROOT / "assets",
    PROJECT_ROOT / "public",
    PROJECT_ROOT / "src" / "assets",
]

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".bmp", ".tiff", ".gif"}
ICON_EXTS = {".svg"}
ANIM_EXTS = {".json", ".lottie", ".webm", ".mp4"}
ALL_EXTS = IMAGE_EXTS | ICON_EXTS | ANIM_EXTS

# ---------------------------------------------------------------------------
# Regras de classificação
# ---------------------------------------------------------------------------

# Mapeamento pasta-pai → categoria
FOLDER_CATEGORY_MAP = {
    "abacaxi": "fruit",
    "banana": "fruit",
    "kiwi": "fruit",
    "manga": "fruit",
    "morangos": "fruit",
    "castanha": "topping",
    "coco-ralado": "topping",
    "ingredientes": "topping",
    "chocolate": "topping",
    "nutella": "topping",
    "folhas palmeiras": "leaf",
    "folhas-moldura": "leaf",
    "folhas-tropicais": "leaf",
    "particulas": "effect",
    "water": "effect",
    "frutas-caindo": "effect",
    "backgrounds": "background",
    "textures": "texture",
    "home": "background",
    "products": "product",
    "characters": "character",
    "delivery": "delivery-object",
}

# Mapeamento prefixo de nome → categoria
NAME_PREFIX_MAP = [
    ("raw-bg-", "background"),
    ("raw-textura-", "texture"),
    ("raw-produto-", "product"),
    ("raw-hero-", "product"),
    ("raw-fx-", "effect"),
    ("raw-leaf-", "leaf"),
    ("raw-topping-", "topping"),
    ("icon-", "icon"),
    ("check", "icon"),
    ("lottie-", "animation"),
]

# Mapeamento categoria → diretório de destino
CATEGORY_DEST_MAP = {
    "background": "assets/images/backgrounds",
    "texture": "assets/images/textures",
    "product": "assets/images/products",
    "fruit": "assets/images/ingredients/fruits",
    "topping": "assets/images/ingredients/toppings",
    "leaf": "assets/images/leaves",
    "effect": "assets/images/effects",
    "character": "assets/images/characters",
    "delivery-object": "assets/images/delivery",
    "icon": "assets/icons/interface",
    "animation": "assets/animations/lottie",
    "review": "assets/images/_review",
}

# Mapeamento categoria → ação
CATEGORY_ACTION_MAP = {
    "background": "convert-webp",
    "texture": "convert-webp",
    "product": "remove-bg-webp",
    "fruit": "remove-bg-webp",
    "topping": "remove-bg-webp",
    "leaf": "remove-bg-webp",
    "effect": "check-alpha-webp",
    "character": "remove-bg-webp",
    "delivery-object": "remove-bg-webp",
    "icon": "keep-svg",
    "animation": "keep-original",
    "review": "manual-review",
}

# Mapeamento categoria → largura máxima
CATEGORY_MAX_WIDTH = {
    "background": 1920,
    "texture": 1920,
    "product": 1200,
    "fruit": 700,
    "topping": 700,
    "leaf": 700,
    "effect": 700,
    "character": 700,
    "delivery-object": 700,
}

# ---------------------------------------------------------------------------
# Detecção de transparência
# ---------------------------------------------------------------------------
def has_transparency(filepath: Path) -> bool | None:
    """Retorna True se a imagem tem canal alpha, False se não, None se não for possível detectar."""
    try:
        from PIL import Image
        with Image.open(filepath) as img:
            if img.mode in ("RGBA", "LA", "PA"):
                # Verifica se realmente usa o canal alpha
                if img.mode == "RGBA":
                    extrema = img.getextrema()
                    if len(extrema) >= 4:
                        alpha_min = extrema[3][0]
                        return alpha_min < 255
                return True
            if img.mode == "P":
                if "transparency" in img.info:
                    return True
            return False
    except Exception:
        return None


def get_image_dimensions(filepath: Path) -> tuple[int, int] | None:
    """Retorna (width, height) ou None."""
    try:
        from PIL import Image
        with Image.open(filepath) as img:
            return img.size
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Classificação
# ---------------------------------------------------------------------------
def classify_file(filepath: Path) -> dict:
    """Classifica um arquivo e retorna metadados."""
    name = filepath.name.lower()
    stem = filepath.stem.lower()
    ext = filepath.suffix.lower()
    parent = filepath.parent.name.lower()
    grandparent = filepath.parent.parent.name.lower() if filepath.parent.parent else ""

    # Tamanho
    try:
        size_bytes = filepath.stat().st_size
    except OSError:
        size_bytes = 0

    size_kb = round(size_bytes / 1024, 1)

    # Dimensões e transparência
    dimensions = None
    transparent = None
    if ext in IMAGE_EXTS:
        dimensions = get_image_dimensions(filepath)
        transparent = has_transparency(filepath)

    # Classificação por categoria
    category = None
    observation = ""

    # 1. Verificar nome com prefixo
    for prefix, cat in NAME_PREFIX_MAP:
        if name.startswith(prefix):
            category = cat
            break

    # 2. Verificar pasta pai
    if category is None:
        if parent in FOLDER_CATEGORY_MAP:
            category = FOLDER_CATEGORY_MAP[parent]
        elif grandparent in FOLDER_CATEGORY_MAP:
            category = FOLDER_CATEGORY_MAP[grandparent]

    # 3. Extensão especial
    if category is None:
        if ext in ICON_EXTS and ("icon" in name or name == "check.svg"):
            category = "icon"
        elif ext in {".json", ".lottie"}:
            category = "animation"
        elif ext == ".webm":
            category = "animation"
        elif ext == ".mp4" and "lottie" in name:
            category = "animation"
            observation = "MP4 de lottie — avaliar conversão para webm"
        elif ext == ".svg" and "lottie" in name:
            category = "review"
            observation = "SVG animado de lottie — avaliar uso"
        elif ext == ".url":
            category = "review"
            observation = "Atalho de URL — ignorar"

    # 4. Verificar nomes iStockPhoto
    if category is None and "istockphoto" in name:
        category = "review"
        observation = "iStockPhoto preview — provavelmente tem marca d'água"

    # 5. Nomes genéricos com hash
    if category is None and len(stem) == 32 and all(c in "0123456789abcdef" for c in stem):
        # Hash MD5 — classificar pela pasta
        if parent in FOLDER_CATEGORY_MAP:
            category = FOLDER_CATEGORY_MAP[parent]
            observation = "Nome hash — classificado pela pasta pai"
        else:
            category = "review"
            observation = "Nome hash sem pasta reconhecível"

    # 6. Imagens com nomes descritivos longos (stock images com transparência)
    if category is None and ext in IMAGE_EXTS:
        name_lower = name.lower()
        if any(kw in name_lower for kw in ["splash", "water", "liquid", "drop"]):
            category = "effect"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["chocolate", "cookie", "cocoa"]):
            category = "topping"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["leaf", "palm", "tropical", "folha"]):
            category = "leaf"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["fruit", "fruta", "banana", "morango", "kiwi", "manga", "abacaxi"]):
            category = "fruit"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["acai", "açaí", "bowl", "tigela"]):
            category = "product"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["background", "sunset", "beach", "praia", "sea", "mar"]):
            category = "background"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["particle", "abstract", "glow", "burst"]):
            category = "effect"
            observation = "Classificado por palavras-chave no nome"
        elif any(kw in name_lower for kw in ["nutella", "spread", "hazelnut"]):
            category = "topping"
            observation = "Classificado por palavras-chave no nome"

    # 7. Fallback
    if category is None:
        category = "review"
        observation = observation or "Não classificado automaticamente"

    # Ícone SVG social
    if category == "icon" and ext == ".svg":
        if any(kw in name for kw in ["whatsapp", "instagram", "facebook", "twitter"]):
            dest = "assets/icons/social"
        elif any(kw in name for kw in ["address", "delivery", "truck"]):
            dest = "assets/icons/interface"
        else:
            dest = CATEGORY_DEST_MAP.get(category, "assets/images/_review")
    else:
        dest = CATEGORY_DEST_MAP.get(category, "assets/images/_review")

    # Ação
    action = CATEGORY_ACTION_MAP.get(category, "manual-review")

    # Se já tem transparência e categoria pede remoção de fundo, ajustar
    if transparent is True and action == "remove-bg-webp":
        action = "check-alpha-webp"
        observation = (observation + " | Já possui transparência, pular rembg").strip(" |")

    # Largura máxima
    max_width = CATEGORY_MAX_WIDTH.get(category)

    return {
        "original_name": filepath.name,
        "original_path": str(filepath),
        "extension": ext,
        "size_bytes": size_bytes,
        "size_kb": size_kb,
        "width": dimensions[0] if dimensions else None,
        "height": dimensions[1] if dimensions else None,
        "has_transparency": transparent,
        "category": category,
        "destination": dest,
        "action": action,
        "max_width": max_width,
        "observation": observation,
    }


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------
def scan_directories(dirs: list[Path]) -> list[dict]:
    """Varre os diretórios e classifica todos os arquivos relevantes."""
    results = []
    seen_paths = set()

    for scan_dir in dirs:
        if not scan_dir.exists():
            print(f"  ⏭  Diretório não existe, pulando: {scan_dir}")
            continue

        print(f"  📂 Varrendo: {scan_dir}")
        count = 0

        for filepath in sorted(scan_dir.rglob("*")):
            if not filepath.is_file():
                continue
            if filepath.suffix.lower() not in ALL_EXTS:
                continue
            # Evitar arquivos do próprio pipeline
            if "_raw" in str(filepath) or "_review" in str(filepath):
                continue

            real = filepath.resolve()
            if real in seen_paths:
                continue
            seen_paths.add(real)

            info = classify_file(filepath)
            results.append(info)
            count += 1

        print(f"     → {count} arquivos encontrados")

    return results


# ---------------------------------------------------------------------------
# Relatórios
# ---------------------------------------------------------------------------
def write_json_report(data: list[dict], path: Path):
    """Gera o relatório JSON."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_files": len(data),
        "summary": {},
        "files": data,
    }
    # Resumo por categoria
    cats = {}
    for item in data:
        cat = item["category"]
        cats[cat] = cats.get(cat, 0) + 1
    report["summary"] = dict(sorted(cats.items()))

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"  ✅ JSON: {path}")


def write_csv_report(data: list[dict], path: Path):
    """Gera o relatório CSV."""
    if not data:
        return

    fields = [
        "original_name", "original_path", "extension", "size_bytes", "size_kb",
        "width", "height", "has_transparency", "category", "destination",
        "action", "max_width", "observation"
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
    print(f"  ✅ CSV:  {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  🔍 Nu Ki Açaí — Auditoria de Assets")
    print("=" * 60)
    print()

    # Verificar Pillow
    try:
        from PIL import Image  # noqa: F401
        print("  ✅ Pillow disponível — dimensões e transparência serão detectadas")
    except ImportError:
        print("  ⚠️  Pillow não instalado — dimensões e transparência ficarão como None")
        print("     Instale com: pip install Pillow")
    print()

    print("  Varrendo diretórios...")
    results = scan_directories(SCAN_DIRS)
    print()

    # Resumo
    cats = {}
    for item in results:
        cat = item["category"]
        cats[cat] = cats.get(cat, 0) + 1

    print("  📊 Resumo por categoria:")
    for cat, count in sorted(cats.items()):
        action = CATEGORY_ACTION_MAP.get(cat, "?")
        print(f"     {cat:20s} → {count:3d} arquivo(s)  [{action}]")
    print(f"     {'TOTAL':20s} → {len(results):3d} arquivo(s)")
    print()

    # Gerar relatórios
    json_path = REPORTS_DIR / "assets-report.json"
    csv_path = REPORTS_DIR / "assets-report.csv"
    write_json_report(results, json_path)
    write_csv_report(results, csv_path)

    print()
    print("  ✅ Auditoria concluída! Nenhum arquivo foi modificado.")
    print(f"  📄 Revise: {json_path}")
    print(f"  📄 Revise: {csv_path}")
    print()


if __name__ == "__main__":
    main()

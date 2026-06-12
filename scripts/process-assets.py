#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process-assets.py — Nu Ki Açaí Asset Processor
Lê o relatório de auditoria e processa cada arquivo conforme sua categoria:
- Backgrounds/Textures: converte WebP, NÃO remove fundo
- Products/Fruits/Toppings/Leaves: remove fundo via rembg + WebP
- Effects: verifica transparência, converte WebP
- Icons: mantém SVG
- Animations: mantém JSON/WebM
- Review: copia sem processar
"""

import json
import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
ASSETS_DIR = PROJECT_ROOT / "assets"
RAW_DIR = ASSETS_DIR / "images" / "_raw"
REVIEW_DIR = ASSETS_DIR / "images" / "_review"
REPORT_PATH = REPORTS_DIR / "assets-report.json"

# Categorias que recebem remoção de fundo
REMBG_CATEGORIES = {"product", "fruit", "topping", "leaf", "character", "delivery-object"}

# Categorias que NÃO recebem remoção de fundo
NO_REMBG_CATEGORIES = {"background", "texture", "icon", "animation", "review", "effect"}

# Qualidade WebP
WEBP_QUALITY = 85
WEBP_QUALITY_LOSSLESS = True  # Para imagens com transparência

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
_rembg_session = None


def get_rembg_session():
    """Lazy-load da sessão rembg para evitar importação desnecessária."""
    global _rembg_session
    if _rembg_session is None:
        try:
            from rembg import new_session
            _rembg_session = new_session("u2net")
            print("  ✅ rembg sessão carregada (modelo u2net)")
        except ImportError:
            print("  ❌ rembg não instalado! Execute: pip install rembg onnxruntime")
            sys.exit(1)
        except Exception as e:
            print(f"  ❌ Erro ao carregar rembg: {e}")
            sys.exit(1)
    return _rembg_session


def create_directory_structure():
    """Cria toda a estrutura de diretórios necessária."""
    dirs = [
        "assets/images/_raw",
        "assets/images/_review",
        "assets/images/backgrounds",
        "assets/images/home",
        "assets/images/textures",
        "assets/images/products",
        "assets/images/ingredients/fruits",
        "assets/images/ingredients/toppings",
        "assets/images/leaves",
        "assets/images/effects",
        "assets/images/characters",
        "assets/images/delivery",
        "assets/icons/interface",
        "assets/icons/social",
        "assets/icons/badges",
        "assets/animations/lottie",
        "assets/animations/webm",
        "reports",
    ]
    for d in dirs:
        full = PROJECT_ROOT / d
        full.mkdir(parents=True, exist_ok=True)
    print("  ✅ Estrutura de diretórios criada")


def copy_to_raw(src: Path, item: dict) -> Path | None:
    """Copia o arquivo original para _raw/ preservando subpasta."""
    try:
        # Criar subpasta baseada na categoria
        cat = item.get("category", "misc")
        raw_subdir = RAW_DIR / cat
        raw_subdir.mkdir(parents=True, exist_ok=True)

        dest = raw_subdir / src.name
        # Evitar sobrescrita
        if dest.exists():
            stem = dest.stem
            suffix = dest.suffix
            counter = 1
            while dest.exists():
                dest = raw_subdir / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.copy2(src, dest)
        return dest
    except Exception as e:
        print(f"    ⚠️  Erro ao copiar para _raw: {e}")
        return None


def resize_image(img, max_width: int):
    """Redimensiona imagem mantendo proporção se exceder max_width."""
    if img.width <= max_width:
        return img
    ratio = max_width / img.width
    new_height = int(img.height * ratio)
    return img.resize((max_width, new_height), resample=3)  # LANCZOS


def remove_background(img):
    """Remove fundo usando rembg. Retorna imagem RGBA ou None em caso de falha."""
    try:
        from rembg import remove
        session = get_rembg_session()
        result = remove(img, session=session, post_process_mask=True)
        return result
    except Exception as e:
        print(f"    ⚠️  rembg falhou: {e}")
        return None


def has_real_transparency(img) -> bool:
    """Verifica se a imagem realmente usa o canal alpha."""
    if img.mode not in ("RGBA", "LA", "PA"):
        return False
    if img.mode == "RGBA":
        extrema = img.getextrema()
        if len(extrema) >= 4:
            return extrema[3][0] < 255
    return True


def save_webp(img, dest: Path, has_alpha: bool = False):
    """Salva imagem como WebP."""
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Evitar sobrescrita
    if dest.exists():
        stem = dest.stem
        counter = 1
        while dest.exists():
            dest = dest.parent / f"{stem}_{counter}.webp"
            counter += 1

    if has_alpha:
        # WebP com transparência — lossless para manter qualidade do alpha
        img.save(dest, "WEBP", quality=WEBP_QUALITY, method=4, lossless=False)
    else:
        # WebP sem transparência
        if img.mode == "RGBA":
            img = img.convert("RGB")
        img.save(dest, "WEBP", quality=WEBP_QUALITY, method=4)

    return dest


# ---------------------------------------------------------------------------
# Processadores por ação
# ---------------------------------------------------------------------------

def process_convert_webp(item: dict, log: list):
    """Converte para WebP sem remover fundo (backgrounds, texturas)."""
    from PIL import Image
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "error", "detail": "Arquivo não encontrado"})
        return

    try:
        with Image.open(src) as img:
            max_w = item.get("max_width") or 1920
            img = resize_image(img, max_w)

            dest_dir = PROJECT_ROOT / item["destination"]
            dest_name = src.stem + ".webp"
            dest = dest_dir / dest_name
            final_path = save_webp(img, dest, has_alpha=False)

            size_final = final_path.stat().st_size
            log.append({
                **item,
                "status": "ok",
                "final_path": str(final_path),
                "final_size_kb": round(size_final / 1024, 1),
                "final_width": img.width,
                "final_height": img.height,
                "detail": f"Convertido para WebP ({img.width}x{img.height})"
            })
            print(f"    ✅ {src.name} → {final_path.name} ({round(size_final/1024)}KB)")
    except Exception as e:
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


def process_remove_bg_webp(item: dict, log: list):
    """Remove fundo com rembg e converte para WebP transparente."""
    from PIL import Image
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "error", "detail": "Arquivo não encontrado"})
        return

    try:
        with Image.open(src) as img:
            # Converter para RGBA se necessário
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            # Remover fundo
            result = remove_background(img)
            if result is None:
                # Falha — mover para _review
                review_dest = REVIEW_DIR / src.name
                if not review_dest.exists():
                    shutil.copy2(src, review_dest)
                log.append({
                    **item,
                    "status": "review",
                    "final_path": str(review_dest),
                    "detail": "rembg falhou — enviado para _review"
                })
                print(f"    ⚠️  {src.name} → _review (rembg falhou)")
                return

            # Redimensionar
            max_w = item.get("max_width") or 700
            result = resize_image(result, max_w)

            # Salvar
            dest_dir = PROJECT_ROOT / item["destination"]
            dest_name = src.stem + ".webp"
            dest = dest_dir / dest_name
            final_path = save_webp(result, dest, has_alpha=True)

            size_final = final_path.stat().st_size
            log.append({
                **item,
                "status": "ok",
                "final_path": str(final_path),
                "final_size_kb": round(size_final / 1024, 1),
                "final_width": result.width,
                "final_height": result.height,
                "bg_removed": True,
                "detail": f"Fundo removido, WebP ({result.width}x{result.height})"
            })
            print(f"    ✅ {src.name} → {final_path.name} (bg removed, {round(size_final/1024)}KB)")
    except Exception as e:
        # Em caso de erro, mover para _review
        try:
            review_dest = REVIEW_DIR / src.name
            if not review_dest.exists():
                shutil.copy2(src, review_dest)
        except Exception:
            pass
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


def process_check_alpha_webp(item: dict, log: list):
    """Verifica transparência existente, converte para WebP mantendo alpha."""
    from PIL import Image
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "error", "detail": "Arquivo não encontrado"})
        return

    try:
        with Image.open(src) as img:
            alpha = has_real_transparency(img)
            max_w = item.get("max_width") or 700
            img = resize_image(img, max_w)

            dest_dir = PROJECT_ROOT / item["destination"]
            dest_name = src.stem + ".webp"
            dest = dest_dir / dest_name
            final_path = save_webp(img, dest, has_alpha=alpha)

            size_final = final_path.stat().st_size
            log.append({
                **item,
                "status": "ok",
                "final_path": str(final_path),
                "final_size_kb": round(size_final / 1024, 1),
                "final_width": img.width,
                "final_height": img.height,
                "has_alpha_preserved": alpha,
                "detail": f"WebP {'com' if alpha else 'sem'} transparência ({img.width}x{img.height})"
            })
            print(f"    ✅ {src.name} → {final_path.name} ({'alpha' if alpha else 'rgb'}, {round(size_final/1024)}KB)")
    except Exception as e:
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


def process_keep_svg(item: dict, log: list):
    """Copia SVG sem modificar."""
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "error", "detail": "Arquivo não encontrado"})
        return

    try:
        dest_dir = PROJECT_ROOT / item["destination"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name

        if not dest.exists():
            shutil.copy2(src, dest)

        log.append({
            **item,
            "status": "ok",
            "final_path": str(dest),
            "detail": "SVG mantido como está"
        })
        print(f"    ✅ {src.name} → {dest}")
    except Exception as e:
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


def process_keep_original(item: dict, log: list):
    """Copia animações (JSON, WebM, etc.) sem modificar."""
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "error", "detail": "Arquivo não encontrado"})
        return

    try:
        dest_dir = PROJECT_ROOT / item["destination"]
        ext = src.suffix.lower()

        # Ajustar pasta para WebM
        if ext == ".webm":
            dest_dir = PROJECT_ROOT / "assets" / "animations" / "webm"
        elif ext == ".mp4":
            dest_dir = PROJECT_ROOT / "assets" / "animations" / "webm"

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name

        if not dest.exists():
            shutil.copy2(src, dest)

        log.append({
            **item,
            "status": "ok",
            "final_path": str(dest),
            "detail": f"Animação copiada ({ext})"
        })
        print(f"    ✅ {src.name} → {dest}")
    except Exception as e:
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


def process_manual_review(item: dict, log: list):
    """Copia para _review sem processar."""
    src = Path(item["original_path"])
    if not src.exists():
        log.append({**item, "status": "review", "detail": "Arquivo não encontrado"})
        return

    try:
        REVIEW_DIR.mkdir(parents=True, exist_ok=True)
        dest = REVIEW_DIR / src.name

        if not dest.exists():
            shutil.copy2(src, dest)

        log.append({
            **item,
            "status": "review",
            "final_path": str(dest),
            "detail": item.get("observation", "Enviado para revisão manual")
        })
        print(f"    🔍 {src.name} → _review/")
    except Exception as e:
        log.append({**item, "status": "error", "detail": str(e)})
        print(f"    ❌ {src.name}: {e}")


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------
ACTION_HANDLERS = {
    "convert-webp": process_convert_webp,
    "remove-bg-webp": process_remove_bg_webp,
    "check-alpha-webp": process_check_alpha_webp,
    "keep-svg": process_keep_svg,
    "keep-original": process_keep_original,
    "manual-review": process_manual_review,
}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  🔧 Nu Ki Açaí — Processamento de Assets")
    print("=" * 60)
    print()

    # Verificar dependências
    try:
        from PIL import Image  # noqa: F401
        print("  ✅ Pillow disponível")
    except ImportError:
        print("  ❌ Pillow não instalado! Execute: pip install Pillow")
        sys.exit(1)

    # Verificar relatório de auditoria
    if not REPORT_PATH.exists():
        print(f"  ❌ Relatório não encontrado: {REPORT_PATH}")
        print("     Execute primeiro: python scripts/audit-assets.py")
        sys.exit(1)

    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report = json.load(f)

    files = report.get("files", [])
    print(f"  📦 {len(files)} arquivos para processar")
    print()

    # Criar estrutura
    print("  📁 Criando estrutura de diretórios...")
    create_directory_structure()
    print()

    # Copiar originais para _raw
    print("  📋 Copiando originais para _raw/...")
    image_exts = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".bmp", ".tiff", ".gif"}
    raw_count = 0
    for item in files:
        ext = item.get("extension", "").lower()
        if ext in image_exts:
            src = Path(item["original_path"])
            if src.exists():
                copy_to_raw(src, item)
                raw_count += 1
    print(f"  ✅ {raw_count} imagens copiadas para _raw/")
    print()

    # Processar cada arquivo
    processing_log = []

    # Agrupar por ação para exibição
    action_groups = {}
    for item in files:
        action = item.get("action", "manual-review")
        action_groups.setdefault(action, []).append(item)

    for action, items in action_groups.items():
        handler = ACTION_HANDLERS.get(action, process_manual_review)
        print(f"  🔄 [{action}] — {len(items)} arquivo(s)")

        for item in items:
            handler(item, processing_log)

        print()

    # Resumo
    status_counts = {}
    for entry in processing_log:
        s = entry.get("status", "unknown")
        status_counts[s] = status_counts.get(s, 0) + 1

    print("=" * 60)
    print("  📊 Resumo do processamento:")
    for status, count in sorted(status_counts.items()):
        icon = {"ok": "✅", "review": "🔍", "error": "❌"}.get(status, "❓")
        print(f"     {icon} {status:10s} → {count}")
    print(f"     📦 Total: {len(processing_log)}")
    print()

    # Salvar log de processamento
    log_path = REPORTS_DIR / "processing-log.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "processed_at": datetime.now().isoformat(),
            "total": len(processing_log),
            "summary": status_counts,
            "entries": processing_log,
        }, f, ensure_ascii=False, indent=2)
    print(f"  📄 Log salvo em: {log_path}")
    print()
    print("  ✅ Processamento concluído!")
    print("     Execute agora: python scripts/generate-asset-report.py")
    print()


if __name__ == "__main__":
    main()

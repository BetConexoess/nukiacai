#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate-asset-report.py — Nu Ki Açaí Asset Report Generator
Gera uma galeria HTML interativa para revisão visual dos assets processados.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
import base64

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
AUDIT_PATH = REPORTS_DIR / "assets-report.json"
LOG_PATH = REPORTS_DIR / "processing-log.json"
GALLERY_PATH = REPORTS_DIR / "assets-gallery.html"


def get_thumbnail_data_uri(filepath: str, max_size: int = 200) -> str:
    """Gera um data URI de miniatura para exibição inline."""
    try:
        p = Path(filepath)
        if not p.exists():
            return ""
        ext = p.suffix.lower()

        # SVG — inline direto
        if ext == ".svg":
            content = p.read_text(encoding="utf-8", errors="replace")
            encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
            return f"data:image/svg+xml;base64,{encoded}"

        # JSON/Lottie — sem miniatura
        if ext in (".json", ".lottie", ".webm", ".mp4"):
            return ""

        # Imagens — gerar miniatura com Pillow
        from PIL import Image
        with Image.open(p) as img:
            img.thumbnail((max_size, max_size), resample=3)
            import io
            buf = io.BytesIO()
            fmt = "PNG" if img.mode == "RGBA" else "JPEG"
            img.save(buf, format=fmt, quality=70)
            encoded = base64.b64encode(buf.getvalue()).decode("ascii")
            mime = "image/png" if fmt == "PNG" else "image/jpeg"
            return f"data:{mime};base64,{encoded}"
    except Exception:
        return ""


def build_gallery_html(audit_data: list, log_data: list) -> str:
    """Gera o HTML completo da galeria."""

    # Criar mapeamento original_path → log entry
    log_map = {}
    for entry in log_data:
        log_map[entry.get("original_path", "")] = entry

    # Categorias únicas
    categories = sorted(set(item.get("category", "unknown") for item in audit_data))

    # Contagem por categoria
    cat_counts = {}
    for item in audit_data:
        c = item.get("category", "unknown")
        cat_counts[c] = cat_counts.get(c, 0) + 1

    # Status counts
    status_counts = {"ok": 0, "review": 0, "error": 0, "pending": 0}
    for item in audit_data:
        entry = log_map.get(item.get("original_path", ""))
        if entry:
            s = entry.get("status", "pending")
            status_counts[s] = status_counts.get(s, 0) + 1
        else:
            status_counts["pending"] += 1

    total = len(audit_data)

    # Cards HTML
    cards_html = ""
    for i, item in enumerate(audit_data):
        name = item.get("original_name", "?")
        category = item.get("category", "unknown")
        action = item.get("action", "?")
        dest = item.get("destination", "?")
        size_kb = item.get("size_kb", 0)
        width = item.get("width") or "?"
        height = item.get("height") or "?"
        has_alpha = item.get("has_transparency")
        observation = item.get("observation", "")
        original_path = item.get("original_path", "")

        # Info do processamento
        entry = log_map.get(original_path, {})
        status = entry.get("status", "pending")
        final_path = entry.get("final_path", "")
        final_size = entry.get("final_size_kb", "")
        detail = entry.get("detail", "")

        # Status badge
        status_class = {
            "ok": "status-ok",
            "review": "status-review",
            "error": "status-error",
            "pending": "status-pending"
        }.get(status, "status-pending")

        status_label = {
            "ok": "✅ OK",
            "review": "🔍 Review",
            "error": "❌ Erro",
            "pending": "⏳ Pendente"
        }.get(status, "❓")

        # Thumbnails
        thumb_before = get_thumbnail_data_uri(original_path, 150)
        thumb_after = get_thumbnail_data_uri(final_path, 150) if final_path else ""

        alpha_badge = ""
        if has_alpha is True:
            alpha_badge = '<span class="badge badge-alpha">Alpha</span>'
        elif has_alpha is False:
            alpha_badge = '<span class="badge badge-opaque">Opaco</span>'

        review_class = " card-review" if status == "review" else ""
        review_class += " card-error" if status == "error" else ""

        cards_html += f"""
        <div class="card{review_class}" data-category="{category}" data-status="{status}">
            <div class="card-header">
                <span class="card-category">{category}</span>
                <span class="card-status {status_class}">{status_label}</span>
            </div>
            <div class="card-thumbs">
                <div class="thumb-box">
                    <span class="thumb-label">Original</span>
                    {"<img src='" + thumb_before + "' alt='Original' loading='lazy' />" if thumb_before else "<div class='thumb-placeholder'>Sem preview</div>"}
                </div>
                <div class="thumb-arrow">→</div>
                <div class="thumb-box">
                    <span class="thumb-label">Final</span>
                    {"<img src='" + thumb_after + "' alt='Final' loading='lazy' />" if thumb_after else "<div class='thumb-placeholder'>—</div>"}
                </div>
            </div>
            <div class="card-body">
                <p class="card-name" title="{name}">{name[:50]}{'...' if len(name) > 50 else ''}</p>
                <div class="card-meta">
                    <span>📐 {width}×{height}</span>
                    <span>📦 {size_kb}KB{' → ' + str(final_size) + 'KB' if final_size else ''}</span>
                    {alpha_badge}
                </div>
                <div class="card-details">
                    <span class="card-action">Ação: {action}</span>
                    <span class="card-dest" title="{dest}">📁 {dest.split('/')[-1] if '/' in dest else dest}</span>
                </div>
                {"<p class='card-obs'>" + observation + "</p>" if observation else ""}
                {"<p class='card-detail'>" + detail + "</p>" if detail else ""}
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Nu Ki Açaí — Galeria de Assets</title>
    <style>
        :root {{
            --bg-deep: #0E0122;
            --bg-mid: #15032E;
            --bg-card: #1C0833;
            --bg-hover: #2F154C;
            --purple-main: #6211AF;
            --purple-bright: #8B2CFF;
            --purple-soft: #CDBBEA;
            --white: #FFFFFF;
            --gold: #FFF1C7;
            --yellow: #FFD45A;
            --red: #FF315E;
            --green: #3DDC84;
            --orange: #FF9F43;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: var(--bg-deep);
            color: var(--white);
            line-height: 1.5;
        }}

        .header {{
            background: linear-gradient(135deg, var(--bg-mid), var(--purple-main));
            padding: 2rem;
            text-align: center;
            border-bottom: 2px solid var(--purple-bright);
        }}

        .header h1 {{
            font-size: 1.8rem;
            background: linear-gradient(135deg, var(--purple-bright), var(--yellow));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}

        .header .subtitle {{
            color: var(--purple-soft);
            font-size: 0.9rem;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }}

        .stat {{
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 0.5rem 1.2rem;
            text-align: center;
        }}

        .stat-value {{
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--purple-bright);
        }}

        .stat-label {{
            font-size: 0.75rem;
            color: var(--purple-soft);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .toolbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-deep);
            padding: 1rem 2rem;
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            align-items: center;
            border-bottom: 1px solid rgba(139,44,255,0.2);
        }}

        .filter-btn {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(139,44,255,0.3);
            color: var(--purple-soft);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.8rem;
            transition: all 0.2s ease;
        }}

        .filter-btn:hover {{
            background: rgba(139,44,255,0.2);
            border-color: var(--purple-bright);
        }}

        .filter-btn.active {{
            background: var(--purple-main);
            color: var(--white);
            border-color: var(--purple-bright);
        }}

        .filter-label {{
            color: var(--purple-soft);
            font-size: 0.8rem;
            margin-right: 0.5rem;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1rem;
            padding: 1.5rem 2rem;
        }}

        .card {{
            background: var(--bg-card);
            border-radius: 16px;
            border: 1px solid rgba(139,44,255,0.15);
            overflow: hidden;
            transition: all 0.3s ease;
        }}

        .card:hover {{
            border-color: var(--purple-bright);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(139,44,255,0.15);
        }}

        .card-review {{
            border-color: var(--orange) !important;
            box-shadow: inset 0 0 0 1px rgba(255,159,67,0.2);
        }}

        .card-error {{
            border-color: var(--red) !important;
            box-shadow: inset 0 0 0 1px rgba(255,49,94,0.2);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.6rem 1rem;
            background: rgba(255,255,255,0.02);
        }}

        .card-category {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--purple-bright);
            font-weight: 600;
        }}

        .card-status {{
            font-size: 0.7rem;
            padding: 0.15rem 0.5rem;
            border-radius: 6px;
            font-weight: 600;
        }}

        .status-ok {{ background: rgba(61,220,132,0.15); color: var(--green); }}
        .status-review {{ background: rgba(255,159,67,0.15); color: var(--orange); }}
        .status-error {{ background: rgba(255,49,94,0.15); color: var(--red); }}
        .status-pending {{ background: rgba(255,255,255,0.05); color: var(--purple-soft); }}

        .card-thumbs {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            padding: 0.8rem;
            background: rgba(0,0,0,0.3);
            /* Checkerboard for transparency */
            background-image:
                linear-gradient(45deg, rgba(255,255,255,0.03) 25%, transparent 25%),
                linear-gradient(-45deg, rgba(255,255,255,0.03) 25%, transparent 25%),
                linear-gradient(45deg, transparent 75%, rgba(255,255,255,0.03) 75%),
                linear-gradient(-45deg, transparent 75%, rgba(255,255,255,0.03) 75%);
            background-size: 12px 12px;
            background-position: 0 0, 0 6px, 6px -6px, -6px 0;
        }}

        .thumb-box {{
            text-align: center;
            flex: 1;
        }}

        .thumb-label {{
            display: block;
            font-size: 0.65rem;
            color: var(--purple-soft);
            margin-bottom: 0.3rem;
            text-transform: uppercase;
        }}

        .thumb-box img {{
            max-width: 140px;
            max-height: 100px;
            border-radius: 6px;
            object-fit: contain;
        }}

        .thumb-placeholder {{
            width: 100px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px dashed rgba(255,255,255,0.1);
            border-radius: 6px;
            font-size: 0.7rem;
            color: rgba(255,255,255,0.2);
            margin: 0 auto;
        }}

        .thumb-arrow {{
            color: var(--purple-bright);
            font-size: 1.2rem;
            flex-shrink: 0;
        }}

        .card-body {{
            padding: 0.8rem 1rem;
        }}

        .card-name {{
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--white);
            word-break: break-all;
            margin-bottom: 0.4rem;
        }}

        .card-meta {{
            display: flex;
            gap: 0.6rem;
            flex-wrap: wrap;
            font-size: 0.7rem;
            color: var(--purple-soft);
            margin-bottom: 0.4rem;
        }}

        .badge {{
            font-size: 0.6rem;
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            font-weight: 600;
        }}

        .badge-alpha {{
            background: rgba(61,220,132,0.15);
            color: var(--green);
        }}

        .badge-opaque {{
            background: rgba(255,255,255,0.05);
            color: var(--purple-soft);
        }}

        .card-details {{
            display: flex;
            justify-content: space-between;
            font-size: 0.7rem;
            color: rgba(255,255,255,0.4);
        }}

        .card-obs, .card-detail {{
            font-size: 0.7rem;
            color: var(--yellow);
            margin-top: 0.3rem;
            font-style: italic;
        }}

        .card-detail {{
            color: var(--purple-soft);
        }}

        .hidden {{ display: none !important; }}

        .empty-state {{
            grid-column: 1 / -1;
            text-align: center;
            padding: 4rem 2rem;
            color: var(--purple-soft);
        }}

        @media (max-width: 768px) {{
            .grid {{
                grid-template-columns: 1fr;
                padding: 1rem;
            }}
            .toolbar {{
                padding: 0.8rem 1rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <h1>🍇 Nu Ki Açaí — Galeria de Assets</h1>
        <p class="subtitle">Gerado em {datetime.now().strftime("%d/%m/%Y às %H:%M")}</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-value">{total}</div>
                <div class="stat-label">Total</div>
            </div>
            <div class="stat">
                <div class="stat-value">{status_counts.get('ok', 0)}</div>
                <div class="stat-label">Processados</div>
            </div>
            <div class="stat">
                <div class="stat-value">{status_counts.get('review', 0)}</div>
                <div class="stat-label">Revisão</div>
            </div>
            <div class="stat">
                <div class="stat-value">{status_counts.get('error', 0)}</div>
                <div class="stat-label">Erros</div>
            </div>
        </div>
    </header>

    <nav class="toolbar">
        <span class="filter-label">Filtrar:</span>
        <button class="filter-btn active" data-filter="all">Todos ({total})</button>
        {"".join(f'<button class="filter-btn" data-filter="{c}">{c} ({cat_counts[c]})</button>' for c in categories)}
        <span class="filter-label" style="margin-left: 1rem">Status:</span>
        <button class="filter-btn" data-status="review">🔍 Review ({status_counts.get('review', 0)})</button>
        <button class="filter-btn" data-status="error">❌ Erros ({status_counts.get('error', 0)})</button>
    </nav>

    <div class="grid" id="gallery">
        {cards_html}
    </div>

    <script>
        // Filtros
        document.querySelectorAll('.filter-btn[data-filter]').forEach(btn => {{
            btn.addEventListener('click', () => {{
                // Desativar botões de status
                document.querySelectorAll('.filter-btn[data-status]').forEach(b => b.classList.remove('active'));

                // Toggle categoria
                document.querySelectorAll('.filter-btn[data-filter]').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.dataset.filter;
                document.querySelectorAll('.card').forEach(card => {{
                    if (filter === 'all' || card.dataset.category === filter) {{
                        card.classList.remove('hidden');
                    }} else {{
                        card.classList.add('hidden');
                    }}
                }});
            }});
        }});

        document.querySelectorAll('.filter-btn[data-status]').forEach(btn => {{
            btn.addEventListener('click', () => {{
                const isActive = btn.classList.contains('active');

                // Reset all
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));

                if (!isActive) {{
                    btn.classList.add('active');
                    const status = btn.dataset.status;
                    document.querySelectorAll('.card').forEach(card => {{
                        card.classList.toggle('hidden', card.dataset.status !== status);
                    }});
                }} else {{
                    document.querySelector('.filter-btn[data-filter="all"]').classList.add('active');
                    document.querySelectorAll('.card').forEach(card => card.classList.remove('hidden'));
                }}
            }});
        }});
    </script>
</body>
</html>"""

    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  📊 Nu Ki Açaí — Geração de Relatório Visual")
    print("=" * 60)
    print()

    # Verificar Pillow
    try:
        from PIL import Image  # noqa: F401
        print("  ✅ Pillow disponível — miniaturas serão geradas")
    except ImportError:
        print("  ⚠️  Pillow não instalado — miniaturas não serão geradas")

    # Carregar dados
    if not AUDIT_PATH.exists():
        print(f"  ❌ Relatório de auditoria não encontrado: {AUDIT_PATH}")
        print("     Execute primeiro: python scripts/audit-assets.py")
        sys.exit(1)

    with open(AUDIT_PATH, "r", encoding="utf-8") as f:
        audit = json.load(f)

    audit_data = audit.get("files", [])
    print(f"  📦 {len(audit_data)} arquivos do audit")

    # Carregar log de processamento (pode não existir)
    log_data = []
    if LOG_PATH.exists():
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            log = json.load(f)
        log_data = log.get("entries", [])
        print(f"  📦 {len(log_data)} entradas do processamento")
    else:
        print("  ⚠️  Log de processamento não encontrado — mostrando apenas auditoria")

    print()
    print("  🎨 Gerando galeria HTML...")
    print("     (Gerando miniaturas — pode demorar um pouco)")
    print()

    html = build_gallery_html(audit_data, log_data)

    GALLERY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(GALLERY_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  ✅ Galeria gerada: {GALLERY_PATH}")
    print()
    print(f"  🌐 Abra no navegador:")
    print(f"     start {GALLERY_PATH}")
    print()


if __name__ == "__main__":
    main()

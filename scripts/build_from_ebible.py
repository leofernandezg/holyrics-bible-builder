"""End-to-end: descarga una traducción de ebible.org, parsea USFX, escribe Zefania.

Ejemplo:

    python3 scripts/build_from_ebible.py spaRV1909 \
        --title "Reina-Valera 1909" \
        --identifier RV1909 \
        --date 1909 \
        --rights "Public Domain" \
        --out output/public-domain/rv1909.xml

Para versiones que no estén en dominio público no usar este path: chequear
LEGAL.md primero.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from build_zefania import BibleMeta, build
from fetch_ebible import download
from parse_usfx import parse


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("translation_id", help="Código de ebible (ej: spaRV1909)")
    ap.add_argument("--title", required=True, help='Título legible ("Reina-Valera 1909")')
    ap.add_argument("--identifier", required=True, help='ID corto ("RV1909")')
    ap.add_argument("--language", default="SPA",
                    help="Código ISO del idioma para el bloque INFORMATION y los "
                         "nombres de libros (es/en/pt o spa/eng/por). Default: SPA.")
    ap.add_argument("--slug", default=None,
                    help="Slug del archivo en ebible si difiere del translation_id "
                         "(ej: 'eng-kjv2006' para engKJV)")
    ap.add_argument("--date", default="")
    ap.add_argument("--publisher", default="")
    ap.add_argument("--rights", default="Public Domain")
    ap.add_argument("--description", default="")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--no-strict", action="store_true",
                    help="No abortar si faltan libros/capítulos (úselo solo en debugging)")
    ap.add_argument("--force-download", action="store_true")
    args = ap.parse_args()

    try:
        print(f"1/3 ↓ Descargando {args.translation_id} de ebible.org...", file=sys.stderr)
        xml = download(args.translation_id, force=args.force_download, slug=args.slug)

        print(f"2/3 ⚙ Parseando USFX...", file=sys.stderr)
        verses = parse(xml)
        total_input = sum(len(v) for ch in verses.values() for v in ch.values())
        print(f"  ✓ {len(verses)} libros, {total_input} versículos parseados", file=sys.stderr)

        print(f"3/3 ✎ Escribiendo Zefania → {args.out}", file=sys.stderr)
        meta = BibleMeta(
            title=args.title,
            identifier=args.identifier,
            language=args.language,
            date=args.date,
            publisher=args.publisher,
            rights=args.rights,
            description=args.description or args.title,
            source=f"https://ebible.org/{args.translation_id}",
        )
        total_out = build(verses, meta, args.out, strict=not args.no_strict)
        print(f"  ✓ {total_out} versículos escritos en {args.out}", file=sys.stderr)
        print(f"\nListo. Importá {args.out} desde Holyrics (Settings → Bibles → Import).", file=sys.stderr)
    except Exception as e:  # noqa: BLE001
        print(f"\nERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Descarga una traducción desde ebible.org y la parsea a `{book: {chapter: [verses]}}`.

ebible.org publica explícitamente sus textos para redistribución (mayormente
dominio público o licencias permisivas). Es la fuente recomendada para versiones
libres. Verificá la licencia exacta del paquete que bajes en su página `details.php`.

Formato de entrada: **USFX** (XML), el más limpio para parsear programáticamente.

Uso típico:

    python3 scripts/fetch_ebible.py spaRV1909
    # → descarga, unzipea, y deja sources/ebible-cache/spaRV1909_usfx.xml

    python3 scripts/build_from_ebible.py spaRV1909 \
        --title "Reina-Valera 1909" --bsname-from canon \
        --out output/public-domain/rv1909.xml
"""
from __future__ import annotations

import argparse
import sys
import urllib.request
import zipfile
from pathlib import Path

# Cache anclado a la raíz del proyecto, no al cwd — así da igual desde dónde
# se invoque el script.
CACHE_DIR = Path(__file__).resolve().parent.parent / "sources" / "ebible-cache"


def download(translation_id: str, force: bool = False, slug: str | None = None) -> Path:
    """Baja el zip USFX de ebible.org. Devuelve la ruta al .xml extraído.

    `translation_id` es el código que usa ebible (ej. 'spaRV1909'). Es el
    segmento que aparece en la URL `ebible.org/<id>`.

    `slug` (opcional) es el nombre del archivo de descarga sin el sufijo
    `_usfx`. Por defecto coincide con `translation_id`, pero algunos paquetes
    tienen slugs distintos (ej. KJV: id=`engKJV` pero slug=`eng-kjv2006`).
    """
    slug = slug or translation_id
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = CACHE_DIR / f"{slug}_usfx.zip"
    xml_path = CACHE_DIR / f"{slug}_usfx.xml"

    if xml_path.exists() and not force:
        print(f"  ✓ ya en cache: {xml_path}", file=sys.stderr)
        return xml_path

    url = f"https://eBible.org/Scriptures/{slug}_usfx.zip"
    print(f"  ↓ {url}", file=sys.stderr)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "holyrics-bible-builder/0.1 "
                "(+https://github.com/leofernandezg/holyrics-bible-builder)"
            ),
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        zip_path.write_bytes(resp.read())

    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(CACHE_DIR)

    if not xml_path.exists():
        # Algunas distribuciones nombran el archivo XML interno distinto al slug
        candidates = (
            list(CACHE_DIR.glob(f"{slug}*usfx*.xml"))
            or list(CACHE_DIR.glob(f"{translation_id}*usfx*.xml"))
        )
        if not candidates:
            raise FileNotFoundError(
                f"no encontré el XML USFX en {CACHE_DIR} tras descomprimir {zip_path}"
            )
        xml_path = candidates[0]

    print(f"  ✓ extraído: {xml_path}", file=sys.stderr)
    return xml_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Baja una traducción desde ebible.org")
    ap.add_argument("translation_id", help="Código de ebible (ej: spaRV1909, eng-web)")
    ap.add_argument("--slug", default=None,
                    help="Slug del archivo si no coincide con translation_id (ej: 'eng-kjv2006' para engKJV)")
    ap.add_argument("--force", action="store_true", help="Re-descargar aunque exista")
    args = ap.parse_args()

    try:
        xml = download(args.translation_id, args.force, args.slug)
        print(xml)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

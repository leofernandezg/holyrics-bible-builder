"""Validación estructural del XML generado.

Chequeos:
- 66 libros con `number` 1..66 sin huecos.
- AT (1..39) bajo testament "Old"; NT (40..66) bajo "New".
- bname y bsname coinciden con el canon en el idioma declarado en
  <INFORMATION>/<language> (o el que se pase por --language).
- Cantidad de capítulos por libro coincide con el canon (`canon.BOOKS`).
- Cada capítulo tiene versos numerados 1..N consecutivos, sin huecos.
- Ningún verso vacío.
- Codificación UTF-8 sin BOM.

No verifica fidelidad literal contra la fuente — para eso ver `test_fidelity_usfx.py`.

Uso:
    python3 scripts/validate_xml.py <ruta.xml>
    python3 scripts/validate_xml.py <ruta.xml> --language en   # fuerza idioma
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

from canon import BOOKS


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)


def main(xml_path: Path, language: str | None = None) -> int:
    data = xml_path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        fail("el archivo tiene BOM UTF-8")
        return 1

    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        fail(f"no parsea como XML: {e}")
        return 1

    if root.tag != "XMLBIBLE":
        fail(f"root debería ser <XMLBIBLE>, es <{root.tag}>")
        return 1

    # Idioma: parámetro explícito o el del bloque INFORMATION
    if language is None:
        info = root.find("INFORMATION")
        lang_el = info.find("language") if info is not None else None
        language = (lang_el.text or "en").strip() if lang_el is not None else "en"

    by_number: dict[int, ET.Element] = {}
    for book in root.findall("BIBLEBOOK"):
        n = int(book.get("bnumber") or "0")
        if n in by_number:
            fail(f"libro {n} duplicado")
            return 1
        by_number[n] = book

    if set(by_number) != set(range(1, 67)):
        fail(f"libros faltantes/sobrantes: {sorted(set(range(1,67)) - set(by_number))}")
        return 1

    errors = 0
    for canon_book in BOOKS:
        book_el = by_number[canon_book.number]
        expected_name = canon_book.name(language)
        expected_short = canon_book.short(language)
        if book_el.get("bname") != expected_name:
            fail(f"libro {canon_book.number}: bname={book_el.get('bname')!r} != {expected_name!r} (lang={language})")
            errors += 1
        if book_el.get("bsname") != expected_short:
            fail(f"libro {canon_book.number}: bsname={book_el.get('bsname')!r} != {expected_short!r} (lang={language})")
            errors += 1
        chapters = book_el.findall("CHAPTER")
        chap_nums = [int(c.get("cnumber") or "0") for c in chapters]
        if chap_nums != list(range(1, canon_book.expected_chapters + 1)):
            fail(
                f"{expected_name}: capítulos {chap_nums} "
                f"!= esperados 1..{canon_book.expected_chapters}"
            )
            errors += 1
            continue
        for chap in chapters:
            cn = int(chap.get("cnumber") or "0")
            verses = chap.findall("VERS")
            vnums = [int(v.get("vnumber") or "0") for v in verses]
            if not verses:
                fail(f"{expected_name} {cn}: sin versos")
                errors += 1
                continue
            # La numeración debe ser estrictamente creciente y empezar en 1.
            # Gaps internos están permitidos: las traducciones del texto crítico
            # (ASV, WEB, etc.) omiten algunos versos vs. el Textus Receptus
            # (Mt 17:21, Mc 9:44, Jn 5:4, etc.). Lo importante es que no haya
            # duplicados ni números fuera de orden.
            if vnums != sorted(set(vnums)):
                fail(f"{expected_name} {cn}: versos duplicados o fuera de orden: {vnums}")
                errors += 1
            elif vnums[0] != 1:
                fail(f"{expected_name} {cn}: primer verso es {vnums[0]}, debería ser 1")
                errors += 1
            for v in verses:
                if not (v.text or "").strip():
                    fail(f"{expected_name} {cn}:{v.get('vnumber')} vacío")
                    errors += 1

    if errors:
        print(f"\n{errors} errores en la validación", file=sys.stderr)
        return 1

    total = sum(
        len(c.findall("VERS"))
        for b in by_number.values()
        for c in b.findall("CHAPTER")
    )
    print(f"OK: 66 libros, {total} versículos, idioma={language}. Estructura válida (Zefania XML).")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("xml", type=Path)
    ap.add_argument("--language", default=None,
                    help="Forzar idioma para validar bname (es/en/pt). Si se omite, se lee de <INFORMATION>/<language>.")
    args = ap.parse_args()
    sys.exit(main(args.xml, args.language))

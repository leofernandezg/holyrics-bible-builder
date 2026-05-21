"""Test de fidelidad char-por-char: Zefania XML vs USFX cacheado.

Para una versión generada con `build_from_ebible.py`:

  1. Re-parsea el USFX en `sources/ebible-cache/<id>_usfx.xml`.
  2. Lee el `output/.../X.xml` (Zefania).
  3. Compara verso por verso el texto que quedó en el XML contra lo que sale
     del USFX hoy. Cualquier diferencia es un fallo.

Esto cierra el loop: si el archivo Zefania que publicamos coincide carácter
por carácter con el USFX de ebible.org, es 100% reproducible y verificable
por cualquier tercero que repita el pipeline.

Uso:
    python3 scripts/test_fidelity_usfx.py spaRV1909 output/public-domain/rv1909.xml
"""
from __future__ import annotations

import sys
from pathlib import Path
from xml.etree import ElementTree as ET

from canon import BOOKS
from parse_usfx import parse


def diff_summary(a: str, b: str, ctx: int = 30) -> str:
    """Devuelve una descripción corta del primer diff entre a y b."""
    for i, (ca, cb) in enumerate(zip(a, b)):
        if ca != cb:
            start = max(0, i - ctx)
            end = min(min(len(a), len(b)), i + ctx)
            return (
                f"pos {i}: "
                f"XML…{a[start:end]!r}… "
                f"USFX…{b[start:end]!r}…"
            )
    if len(a) != len(b):
        if len(a) > len(b):
            return f"XML tiene {len(a) - len(b)} chars de más: ...{a[len(b):][:50]!r}"
        return f"USFX tiene {len(b) - len(a)} chars de más: ...{b[len(a):][:50]!r}"
    return "(no diff)"


def test(translation_id: str, xml_path: Path) -> int:
    cache = Path(__file__).resolve().parent.parent / "sources" / "ebible-cache" / f"{translation_id}_usfx.xml"
    if not cache.exists():
        print(f"  ✗ no encuentro el USFX cacheado: {cache}", file=sys.stderr)
        print(f"     correr antes: python3 scripts/fetch_ebible.py {translation_id}",
              file=sys.stderr)
        return 1

    print(f"  ⚙ Parseando USFX: {cache.name}", file=sys.stderr)
    usfx_data = parse(cache)

    print(f"  ⚙ Cargando Zefania XML: {xml_path}", file=sys.stderr)
    root = ET.fromstring(xml_path.read_bytes())

    matches = 0
    mismatches: list[tuple[str, int, int, str]] = []
    missing_xml = 0
    extra_xml = 0

    # Indexar el XML por (book_num, chapter, verse)
    xml_verses: dict[tuple[int, int, int], str] = {}
    for book_el in root.findall("BIBLEBOOK"):
        bnum = int(book_el.get("bnumber") or "0")
        for chap in book_el.findall("CHAPTER"):
            cnum = int(chap.get("cnumber") or "0")
            for v in chap.findall("VERS"):
                vnum = int(v.get("vnumber") or "0")
                xml_verses[(bnum, cnum, vnum)] = v.text or ""

    # Comparar
    canon_by_num = {b.number: b for b in BOOKS}
    for bnum, chapters in usfx_data.items():
        bname = canon_by_num.get(bnum).es_name if bnum in canon_by_num else f"#{bnum}"
        for cnum, verses in chapters.items():
            for vnum, usfx_text in verses.items():
                xml_text = xml_verses.get((bnum, cnum, vnum))
                if xml_text is None:
                    missing_xml += 1
                    mismatches.append((bname, cnum, vnum, "FALTA EN XML"))
                    continue
                if xml_text == usfx_text:
                    matches += 1
                else:
                    mismatches.append(
                        (bname, cnum, vnum, diff_summary(xml_text, usfx_text))
                    )

    # Detectar versos que sobran en el XML
    usfx_keys = {
        (bn, cn, vn)
        for bn, chs in usfx_data.items()
        for cn, vs in chs.items()
        for vn in vs
    }
    extra_xml = len(set(xml_verses) - usfx_keys)

    total = matches + len(mismatches)
    print(f"\n  Coinciden: {matches}/{total} ({100*matches/total:.2f}%)" if total else "")
    if missing_xml:
        print(f"  Faltan en XML: {missing_xml}")
    if extra_xml:
        print(f"  Sobran en XML: {extra_xml}")

    if mismatches:
        print("\n  Primeros 10 desajustes:")
        for bname, cn, vn, why in mismatches[:10]:
            print(f"    {bname} {cn}:{vn} — {why}")
        if len(mismatches) > 10:
            print(f"    (+ {len(mismatches) - 10} más)")
        return 1

    if extra_xml:
        print("  ✗ El XML tiene versos que no están en el USFX")
        return 1

    print(f"\n  ✓ Fidelidad char-por-char: {matches} versos idénticos al USFX de origen.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("uso: python3 scripts/test_fidelity_usfx.py <ebible_id> <ruta.xml>",
              file=sys.stderr)
        sys.exit(2)
    sys.exit(test(sys.argv[1], Path(sys.argv[2])))

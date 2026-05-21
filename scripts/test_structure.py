"""Tests de forma exhaustivos sobre un Zefania XML generado.

Sirve para cualquier versión generada por el pipeline (RV1909, RVC, etc.).
A diferencia de `validate_xml.py` (que cubre los chequeos básicos), esto va
más a fondo:

  1. XML bien formado y parseable.
  2. Encoding UTF-8 sin BOM.
  3. Root es `<XMLBIBLE>` con atributo `biblename`.
  4. `<INFORMATION>` presente y con campos clave (title, identifier, language, rights).
  5. 66 `<BIBLEBOOK>` con `bnumber` 1..66 sin huecos ni duplicados.
  6. `bname` y `bsname` coinciden con `canon.BOOKS` en el idioma declarado en
     `<INFORMATION>/<language>` (o el que se pase por `--language`).
  7. Cantidad de `<CHAPTER>` por libro == `expected_chapters` del canon.
  8. Capítulos numerados 1..N consecutivos, sin huecos.
  9. Versos numerados desde 1, consecutivos (permitido que un libro/cap tenga
     menos versos que la "norma" — las traducciones difieren — pero deben ser
     consecutivos a partir de 1).
 10. Ningún `<VERS>` vacío o solo con whitespace.
 11. Ningún carácter de control inválido (excepto \t, \n, \r).
 12. El texto de cada verso no tiene markup XML sin escapar (no quedaron `<w>`
     ni `<add>` ni similares del USFX).
 13. Sanity de orden: AT (1..39) antes que NT (40..66).
 14. Spot-checks de presencia de versículos icónicos (Génesis 1:1, Salmos 23:1,
     Juan 3:16, Apoc 22:21).

Salida: imprime cada chequeo con ✓/✗ y termina con código de salida 0 (todo
bien) o 1 (al menos un test falló).

Uso:
    python3 scripts/test_structure.py output/public-domain/rv1909.xml
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

from canon import BOOKS

OK = "  ✓"
FAIL = "  ✗"

# Permitido: tabs, newlines, carriage returns. Todo lo demás bajo U+0020
# (salvo los anteriores) es carácter de control inválido en XML/texto humano.
_INVALID_CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

# Markup residual que NO debería estar en el texto si el parser USFX/HTML
# hizo bien su trabajo.
_RESIDUAL_MARKUP = re.compile(r"<(?:w|add|nd|wj|f|fe|x|note)[\s>/]")


class Report:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.errors: list[str] = []

    def check(self, ok: bool, label: str, detail: str = "") -> None:
        if ok:
            self.passed += 1
            print(f"{OK} {label}")
        else:
            self.failed += 1
            msg = f"{label}" + (f" — {detail}" if detail else "")
            self.errors.append(msg)
            print(f"{FAIL} {msg}")


_SPOT_CHECKS_BY_LANG = {
    "es": [
        (1,  1,  1, ["principio"]),       # Génesis 1:1
        (19, 23, 1, ["pastor"]),          # Salmo 23:1
        (43, 3, 16, ["Dios"]),            # Juan 3:16
        (66, 22, 21, [""]),               # último verso (solo existencia)
    ],
    "en": [
        (1,  1,  1, ["beginning"]),       # Genesis 1:1
        (19, 23, 1, ["shepherd"]),        # Psalm 23:1
        (43, 3, 16, ["world"]),           # John 3:16
        (66, 22, 21, [""]),
    ],
    "pt": [
        (1,  1,  1, ["princípio"]),       # Gênesis 1:1
        (19, 23, 1, ["pastor"]),          # Salmo 23:1
        (43, 3, 16, ["Deus"]),            # João 3:16
        (66, 22, 21, [""]),
    ],
}


def test(xml_path: Path, language: str | None = None) -> int:
    r = Report()

    if not xml_path.exists():
        print(f"{FAIL} archivo no existe: {xml_path}")
        return 1

    raw = xml_path.read_bytes()

    # 1-2. Encoding + parseable
    r.check(not raw.startswith(b"\xef\xbb\xbf"), "Sin BOM UTF-8")
    try:
        raw.decode("utf-8")
        r.check(True, "Decodifica como UTF-8")
    except UnicodeDecodeError as e:
        r.check(False, "Decodifica como UTF-8", str(e))
        return 1

    try:
        root = ET.fromstring(raw)
        r.check(True, "XML bien formado")
    except ET.ParseError as e:
        r.check(False, "XML bien formado", str(e))
        return 1

    # 3. Root
    r.check(root.tag == "XMLBIBLE", f"Root <XMLBIBLE>", f"es <{root.tag}>")
    r.check(bool(root.get("biblename")), "Root tiene atributo `biblename`",
            f"biblename={root.get('biblename')!r}")

    # 4. <INFORMATION>
    info = root.find("INFORMATION")
    r.check(info is not None, "Bloque <INFORMATION> presente")
    if info is not None:
        for field in ("title", "identifier", "language", "rights"):
            el = info.find(field)
            present = el is not None and (el.text or "").strip() != ""
            r.check(present, f"<INFORMATION>/<{field}> no vacío")

    # Resolver idioma: parámetro explícito o <INFORMATION>/<language>
    if language is None:
        lang_el = info.find("language") if info is not None else None
        language = (lang_el.text or "en").strip() if lang_el is not None else "en"
    lang_key = language.lower()[:3]
    lang_key = {"spa": "es", "eng": "en", "por": "pt"}.get(lang_key, lang_key[:2])
    if lang_key not in _SPOT_CHECKS_BY_LANG:
        lang_key = "en"

    # 5. 66 libros, bnumber 1..66
    books = root.findall("BIBLEBOOK")
    r.check(len(books) == 66, f"66 libros", f"hay {len(books)}")

    bnumbers = [int(b.get("bnumber") or "0") for b in books]
    r.check(sorted(bnumbers) == list(range(1, 67)),
            "bnumber 1..66 sin huecos ni duplicados",
            f"valores: {sorted(bnumbers)}")

    # 13. Orden AT antes que NT
    if bnumbers == sorted(bnumbers):
        r.check(True, "Libros en orden canónico (1..66)")
    else:
        r.check(False, "Libros en orden canónico (1..66)", f"orden: {bnumbers}")

    # Reconstruir índice por número
    by_num = {int(b.get("bnumber") or "0"): b for b in books}

    # 6-10. Por libro
    total_verses = 0
    name_mismatches = 0
    chapter_mismatches = 0
    verse_seq_errors = 0
    empty_verses = 0
    ctrl_chars = 0
    residual_markup = 0

    for canon_book in BOOKS:
        book_el = by_num.get(canon_book.number)
        if book_el is None:
            continue

        expected_name = canon_book.name(lang_key)
        expected_short = canon_book.short(lang_key)
        if book_el.get("bname") != expected_name:
            name_mismatches += 1
        if book_el.get("bsname") != expected_short:
            name_mismatches += 1

        chapters = book_el.findall("CHAPTER")
        cnums = [int(c.get("cnumber") or "0") for c in chapters]
        if cnums != list(range(1, canon_book.expected_chapters + 1)):
            chapter_mismatches += 1
            print(f"     [debug] {expected_name}: capítulos {cnums[:5]}..."
                  f"{cnums[-3:]} (esperaba 1..{canon_book.expected_chapters})")

        for chap in chapters:
            verses = chap.findall("VERS")
            vnums = [int(v.get("vnumber") or "0") for v in verses]
            # Gaps internos están permitidos (traducciones del texto crítico
            # omiten versos como Mt 17:21, Jn 5:4); pero no duplicados ni
            # números fuera de orden, y el primer verso debe ser 1.
            if vnums and (vnums != sorted(set(vnums)) or vnums[0] != 1):
                verse_seq_errors += 1
            for v in verses:
                text = v.text or ""
                if not text.strip():
                    empty_verses += 1
                if _INVALID_CTRL.search(text):
                    ctrl_chars += 1
                if _RESIDUAL_MARKUP.search(text):
                    residual_markup += 1
                total_verses += 1

    r.check(name_mismatches == 0,
            f"Todos los `bname`/`bsname` coinciden con el canon (idioma={lang_key})",
            f"{name_mismatches} mismatches")
    r.check(chapter_mismatches == 0,
            "Cantidad de capítulos coincide con el canon en cada libro",
            f"{chapter_mismatches} libros con desajuste")
    r.check(verse_seq_errors == 0,
            "Versos numerados crecientes desde 1 (gaps internos permitidos para texto crítico)",
            f"{verse_seq_errors} capítulos con numeración rota")
    r.check(empty_verses == 0,
            "Ningún verso vacío",
            f"{empty_verses} versos sin texto")
    r.check(ctrl_chars == 0,
            "Sin caracteres de control inválidos",
            f"{ctrl_chars} versos con caracteres prohibidos")
    r.check(residual_markup == 0,
            "Sin markup XML residual (USFX) sin parsear",
            f"{residual_markup} versos con markup")

    print(f"\n     Total: {total_verses} versículos analizados")

    # 14. Spot-checks (idioma-específicos)
    for bnum, cnum, vnum, must_have in _SPOT_CHECKS_BY_LANG[lang_key]:
        book = by_num.get(bnum)
        chap = next((c for c in (book.findall("CHAPTER") if book is not None else [])
                     if c.get("cnumber") == str(cnum)), None)
        verse = next((v for v in (chap.findall("VERS") if chap is not None else [])
                      if v.get("vnumber") == str(vnum)), None)
        text = (verse.text or "") if verse is not None else ""
        present = verse is not None and all(
            (not s) or s.lower() in text.lower() for s in must_have
        )
        canon_name = next((b.name(lang_key) for b in BOOKS if b.number == bnum), "?")
        r.check(present, f"Spot-check: {canon_name} {cnum}:{vnum} contiene {must_have}",
                f"texto={text[:80]!r}")

    print()
    print(f"  {r.passed} OK · {r.failed} FAIL")
    if r.failed:
        print("\nFallos:")
        for e in r.errors:
            print(f"  - {e}")
        return 1
    return 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("xml", type=Path)
    ap.add_argument("--language", default=None,
                    help="Forzar idioma para chequeos (es/en/pt). Por default se lee de <INFORMATION>/<language>.")
    args = ap.parse_args()
    sys.exit(test(args.xml, args.language))

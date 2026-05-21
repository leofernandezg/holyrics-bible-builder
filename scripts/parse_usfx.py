"""Parser de USFX → estructura intermedia `{book_id: {chapter: {verse: text}}}`.

USFX es la variante XML de USFM que usa ebible.org. Es un formato "stream": los
marcadores `<c />` y `<v />` son auto-cerrantes y el texto fluye libremente
entre ellos hasta el próximo marcador. Esto hace que un parser DOM normal no
sirva — hay que recorrer el árbol en orden, acumulando texto.

Implementación: parseamos el árbol completo y lo recorremos en document order.
El texto de cada elemento (`.text` y `.tail`) se acumula al verso en curso,
salvo que estemos dentro de un tag de `_SKIP_TAGS` (notas al pie, encabezados,
etc.).

Las entradas que NO forman parte del texto bíblico (encabezados, notas al pie,
referencias cruzadas, paratext) se descartan según las reglas de `_SKIP_TAGS`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict
from xml.etree.ElementTree import Element, parse as _et_parse

# Mapeo USFX 3-letter book id → número canónico (1..66)
USFX_TO_NUMBER: Dict[str, int] = {
    "GEN": 1,  "EXO": 2,  "LEV": 3,  "NUM": 4,  "DEU": 5,
    "JOS": 6,  "JDG": 7,  "RUT": 8,  "1SA": 9,  "2SA": 10,
    "1KI": 11, "2KI": 12, "1CH": 13, "2CH": 14, "EZR": 15,
    "NEH": 16, "EST": 17, "JOB": 18, "PSA": 19, "PRO": 20,
    "ECC": 21, "SNG": 22, "ISA": 23, "JER": 24, "LAM": 25,
    "EZK": 26, "DAN": 27, "HOS": 28, "JOL": 29, "AMO": 30,
    "OBA": 31, "JON": 32, "MIC": 33, "NAM": 34, "HAB": 35,
    "ZEP": 36, "HAG": 37, "ZEC": 38, "MAL": 39, "MAT": 40,
    "MRK": 41, "LUK": 42, "JHN": 43, "ACT": 44, "ROM": 45,
    "1CO": 46, "2CO": 47, "GAL": 48, "EPH": 49, "PHP": 50,
    "COL": 51, "1TH": 52, "2TH": 53, "1TI": 54, "2TI": 55,
    "TIT": 56, "PHM": 57, "HEB": 58, "JAS": 59, "1PE": 60,
    "2PE": 61, "1JN": 62, "2JN": 63, "3JN": 64, "JUD": 65,
    "REV": 66,
}

# Tags que contienen metadata/paratext y NO deben aportar texto al versículo.
# El parser entra y sale de ellos, pero ignora su contenido.
_SKIP_TAGS = {
    "id", "h", "toc", "rem", "ide", "sts", "restore",
    "f", "fe", "x",                # notas al pie y refs cruzadas
    "fr", "ft", "fk", "fq", "fqa", "fl", "fp", "fv", "xo", "xt",
    "ms", "mr", "s", "sr", "r", "d", "sp",  # encabezados de sección
    "iex", "qa",
    "table", "tr", "th", "thr", "tc", "tcr",
    "fig", "ndx", "pro", "w_attrib",
    "languageCode",
}

# Tags transparentes: su texto pasa al verso en curso, pero no son markers.
_TRANSPARENT_TEXT = True  # marker; tags transparentes son todo lo no especial
_STRUCTURAL_TAGS = {"book", "c", "v", "ve"} | _SKIP_TAGS


_WS = re.compile(r"\s+")


def _normalize(text: str) -> str:
    """Colapsa espacios y arregla espacios alrededor de puntuación."""
    text = _WS.sub(" ", text).strip()
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text


class _State:
    __slots__ = ("result", "book", "chapter", "verse", "buf", "seen_unknown")

    def __init__(self) -> None:
        self.result: Dict[int, Dict[int, Dict[int, str]]] = {}
        self.book: int | None = None
        self.chapter: int | None = None
        self.verse: int | None = None
        self.buf: list[str] = []
        self.seen_unknown: set[str] = set()

    def flush(self) -> None:
        if self.book is None or self.chapter is None or self.verse is None:
            self.buf = []
            return
        text = _normalize("".join(self.buf))
        if not text:
            self.buf = []
            return
        self.result.setdefault(self.book, {}).setdefault(self.chapter, {})[self.verse] = text
        self.buf = []


def _walk(elem: Element, state: _State, skip: bool) -> None:
    """Recorre el árbol en document-order, acumulando texto al verso en curso.

    `skip=True` significa que estamos dentro de un tag de _SKIP_TAGS — el texto
    de este nodo y de sus descendientes se descarta; solo se preserva la
    estructura para no romper el orden de los marcadores `<v>` / `<c>`.
    """
    tag = elem.tag

    if tag == "book":
        state.flush()
        bid = (elem.get("id") or "").upper().strip()
        state.book = USFX_TO_NUMBER.get(bid)
        state.chapter = None
        state.verse = None
    elif tag == "c":
        state.flush()
        try:
            state.chapter = int((elem.get("id") or "").strip())
        except ValueError:
            state.chapter = None
        state.verse = None
    elif tag == "v":
        state.flush()
        try:
            state.verse = int((elem.get("id") or "").strip().split("-")[0])
        except ValueError:
            state.verse = None
    elif tag == "ve":
        state.flush()
        state.verse = None

    # Determinar si este nodo aporta texto al verso.
    is_skip = skip or (tag in _SKIP_TAGS)
    is_structural = tag in _STRUCTURAL_TAGS

    if not is_skip and not is_structural and tag != "usfx":
        if tag not in _TRANSPARENT and tag not in state.seen_unknown:
            state.seen_unknown.add(tag)
            print(f"  [warn] tag USFX desconocida (tratada como transparente): <{tag}>",
                  file=sys.stderr)

    # .text del elemento (texto entre `<tag>` y el primer hijo) suma si no es skip.
    if not is_skip and elem.text and tag != "usfx":
        state.buf.append(elem.text)

    # Recursión sobre hijos
    for child in elem:
        _walk(child, state, is_skip)

    # .tail del elemento (texto entre `</tag>` y la próxima sibling) siempre
    # va al verso en curso, salvo que el PADRE sea skip — pero el padre se
    # encarga de eso por su propio nivel de skip.
    if not skip and elem.tail:
        state.buf.append(elem.tail)


# Set explícito de tags que reconocemos como transparentes (para warning solo
# si aparece algo no listado).
_TRANSPARENT = {
    "w", "add", "nd", "wj", "qt", "tl", "bk", "em", "bd", "bdit", "it",
    "p", "q", "q1", "q2", "q3", "q4", "m", "mi", "pi", "pi1", "pi2", "li",
    "li1", "li2", "li3", "b", "qs", "qr", "qc", "qm", "qm1", "qm2",
    "pc", "pmo", "pm", "pmc", "pmr", "ph", "ph1", "lh", "lf",
    "cl", "cd",
    "sc",  # small caps (común en ASV)
    "k",   # keyword (común en WEB)
    "rq",  # reference quote (común en Bíblia Livre)
}


def parse(xml_path: Path) -> Dict[int, Dict[int, Dict[int, str]]]:
    """Recorre el USFX y devuelve `{book_number: {chapter: {verse: text}}}`.

    Usa tree walk completo (no iterparse) porque la API de tails de iterparse
    no es confiable cuando un `<v />` tiene texto directo en tail sin hijos
    intermedios (caso común en YLT y otras traducciones).
    """
    tree = _et_parse(xml_path)
    state = _State()
    _walk(tree.getroot(), state, skip=False)
    state.flush()
    return state.result


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("xml", type=Path)
    args = ap.parse_args()
    data = parse(args.xml)
    total = sum(len(v) for ch in data.values() for v in ch.values())
    print(f"libros: {len(data)}, versículos: {total}", file=sys.stderr)
    if 1 in data and 1 in data[1] and 1 in data[1][1]:
        print(f"GEN 1:1 → {data[1][1][1]!r}")

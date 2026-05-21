"""Builder genérico de Zefania XML — el formato que Holyrics requiere para importar.

Toma una estructura intermedia `{book_number: {chapter: {verse: text}}}` y un
metadata dict, y emite el `<XMLBIBLE>` que pide Holyrics. Independiente de la
fuente (BibleGateway, ebible.org, MySword, etc.) — quien lo invoca le pasa los
datos ya parseados.

Estructura del XML resultante (validada contra Holyrics):

    <XMLBIBLE biblename="...">
      <INFORMATION>...</INFORMATION>
      <BIBLEBOOK bnumber="1" bname="Génesis" bsname="Gn">
        <CHAPTER cnumber="1">
          <VERS vnumber="1">EN el principio crió Dios los cielos y la tierra.</VERS>
          ...
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

from canon import BOOKS


@dataclass(frozen=True)
class BibleMeta:
    """Metadatos para el bloque <INFORMATION> del Zefania."""
    title: str                      # ej "Reina-Valera 1909"
    identifier: str                 # ej "RV1909"
    language: str = "SPA"           # código ISO de 3 letras
    publisher: str = ""             # editor (si aplica)
    date: str = ""                  # año
    rights: str = "Public Domain"   # leyenda de derechos
    description: str = ""
    source: str = ""                # URL o referencia de la fuente


def build(
    verses: Dict[int, Dict[int, Dict[int, str]]],
    meta: BibleMeta,
    out_path: Path,
    *,
    strict: bool = True,
) -> int:
    """Escribe el XML Zefania en `out_path`. Devuelve la cantidad total de
    versículos escritos.

    Si `strict=True`, exige que estén presentes los 66 libros con todos los
    capítulos esperados (según `canon.BOOKS`). Falla con error claro si falta
    algo — es la guarda contra exports parciales.
    """
    root = Element("XMLBIBLE", biblename=meta.title)
    _write_info(root, meta)

    total = 0
    missing: list[str] = []

    for book in BOOKS:
        book_data: Optional[Dict[int, Dict[int, str]]] = verses.get(book.number)
        if book_data is None:
            missing.append(f"{book.es_name} (libro {book.number})")
            continue

        book_el = SubElement(
            root,
            "BIBLEBOOK",
            bnumber=str(book.number),
            bname=book.name(meta.language),
            bsname=book.short(meta.language),
        )
        for ch in range(1, book.expected_chapters + 1):
            chap_data = book_data.get(ch)
            if not chap_data:
                missing.append(f"{book.es_name} {ch}")
                continue
            chap_el = SubElement(book_el, "CHAPTER", cnumber=str(ch))
            for v_num in sorted(chap_data):
                v_text = chap_data[v_num]
                ve = SubElement(chap_el, "VERS", vnumber=str(v_num))
                ve.text = v_text
                total += 1

    if missing and strict:
        sample = ", ".join(missing[:5])
        more = f" (+ {len(missing) - 5} más)" if len(missing) > 5 else ""
        raise RuntimeError(f"faltan datos en {len(missing)} secciones: {sample}{more}")

    raw = tostring(root, encoding="utf-8", xml_declaration=True)
    pretty = minidom.parseString(raw).toprettyxml(indent="  ", encoding="UTF-8")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(pretty)
    return total


def _write_info(root: Element, meta: BibleMeta) -> None:
    info = SubElement(root, "INFORMATION")
    fields = {
        "title": meta.title,
        "creator": meta.publisher,
        "subject": "The Holy Bible",
        "description": meta.description or meta.title,
        "publisher": meta.publisher,
        "contributors": "",
        "date": meta.date,
        "type": "Bible",
        "format": "Zefania XML Bible Markup Language",
        "identifier": meta.identifier,
        "source": meta.source,
        "language": meta.language,
        "coverage": "",
        "rights": meta.rights,
    }
    for tag, value in fields.items():
        if value:
            SubElement(info, tag).text = value

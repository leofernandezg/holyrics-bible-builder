"""Canon protestante de 66 libros, con nombres en varios idiomas para el XML / Holyrics
y cantidad esperada de capítulos.

Cualquier mismatch entre `expected_chapters` y lo realmente parseado debe abortar
el pipeline. Es la guarda más simple contra una descarga incompleta.

Idiomas soportados en los nombres de libros: es (español), en (English),
pt (português). El idioma se elige en build_zefania.BibleMeta.language.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    number: int           # 1..66, orden canónico
    es_name: str          # nombre en español (full)
    es_short: str         # abreviatura en español
    en_name: str          # English full name
    en_short: str         # English short name
    pt_name: str          # nome em português (completo)
    pt_short: str         # abreviatura em português
    bg_search: str        # cómo lo escribe uno en el search de BibleGateway (legacy)
    expected_chapters: int
    testament: str        # "Old" o "New"

    def name(self, lang: str) -> str:
        """Devuelve el nombre completo del libro en el idioma pedido.

        `lang` puede ser un código ISO 639-1 (es, en, pt) o ISO 639-2/3
        (spa, eng, por). Case-insensitive. Default: en (cuando el código no
        coincide con ningún idioma soportado).
        """
        return _resolve(self, lang, full=True)

    def short(self, lang: str) -> str:
        """Devuelve la abreviatura del libro en el idioma pedido."""
        return _resolve(self, lang, full=False)


def _resolve(book: Book, lang: str, full: bool) -> str:
    code = (lang or "").lower()[:3]
    if code in ("es", "spa"):
        return book.es_name if full else book.es_short
    if code in ("en", "eng"):
        return book.en_name if full else book.en_short
    if code in ("pt", "por"):
        return book.pt_name if full else book.pt_short
    return book.en_name if full else book.en_short


BOOKS: list[Book] = [
    # Antiguo Testamento (39)
    Book(1,  "Génesis",          "Gn",   "Genesis",         "Gen",  "Gênesis",          "Gn",   "Genesis",         50, "Old"),
    Book(2,  "Éxodo",            "Ex",   "Exodus",          "Exo",  "Êxodo",            "Êx",   "Exodus",          40, "Old"),
    Book(3,  "Levítico",         "Lv",   "Leviticus",       "Lev",  "Levítico",         "Lv",   "Leviticus",       27, "Old"),
    Book(4,  "Números",          "Nm",   "Numbers",         "Num",  "Números",          "Nm",   "Numbers",         36, "Old"),
    Book(5,  "Deuteronomio",     "Dt",   "Deuteronomy",     "Deu",  "Deuteronômio",     "Dt",   "Deuteronomy",     34, "Old"),
    Book(6,  "Josué",            "Jos",  "Joshua",          "Jos",  "Josué",            "Js",   "Joshua",          24, "Old"),
    Book(7,  "Jueces",           "Jue",  "Judges",          "Jdg",  "Juízes",           "Jz",   "Judges",          21, "Old"),
    Book(8,  "Rut",              "Rt",   "Ruth",            "Rut",  "Rute",             "Rt",   "Ruth",             4, "Old"),
    Book(9,  "1 Samuel",         "1 S",  "1 Samuel",        "1Sa",  "1 Samuel",         "1Sm",  "1 Samuel",        31, "Old"),
    Book(10, "2 Samuel",         "2 S",  "2 Samuel",        "2Sa",  "2 Samuel",         "2Sm",  "2 Samuel",        24, "Old"),
    Book(11, "1 Reyes",          "1 R",  "1 Kings",         "1Ki",  "1 Reis",           "1Rs",  "1 Kings",         22, "Old"),
    Book(12, "2 Reyes",          "2 R",  "2 Kings",         "2Ki",  "2 Reis",           "2Rs",  "2 Kings",         25, "Old"),
    Book(13, "1 Crónicas",       "1 Cr", "1 Chronicles",    "1Ch",  "1 Crônicas",       "1Cr",  "1 Chronicles",    29, "Old"),
    Book(14, "2 Crónicas",       "2 Cr", "2 Chronicles",    "2Ch",  "2 Crônicas",       "2Cr",  "2 Chronicles",    36, "Old"),
    Book(15, "Esdras",           "Esd",  "Ezra",            "Ezr",  "Esdras",           "Ed",   "Ezra",            10, "Old"),
    Book(16, "Nehemías",         "Neh",  "Nehemiah",        "Neh",  "Neemias",          "Ne",   "Nehemiah",        13, "Old"),
    Book(17, "Ester",            "Est",  "Esther",          "Est",  "Ester",            "Et",   "Esther",          10, "Old"),
    Book(18, "Job",              "Job",  "Job",             "Job",  "Jó",               "Jó",   "Job",             42, "Old"),
    Book(19, "Salmos",           "Sal",  "Psalms",          "Psa",  "Salmos",           "Sl",   "Psalms",         150, "Old"),
    Book(20, "Proverbios",       "Pr",   "Proverbs",        "Pro",  "Provérbios",       "Pv",   "Proverbs",        31, "Old"),
    Book(21, "Eclesiastés",      "Ec",   "Ecclesiastes",    "Ecc",  "Eclesiastes",      "Ec",   "Ecclesiastes",    12, "Old"),
    Book(22, "Cantares",         "Cnt",  "Song of Solomon", "Sng",  "Cânticos",         "Ct",   "Song of Solomon",  8, "Old"),
    Book(23, "Isaías",           "Is",   "Isaiah",          "Isa",  "Isaías",           "Is",   "Isaiah",          66, "Old"),
    Book(24, "Jeremías",         "Jer",  "Jeremiah",        "Jer",  "Jeremias",         "Jr",   "Jeremiah",        52, "Old"),
    Book(25, "Lamentaciones",    "Lm",   "Lamentations",    "Lam",  "Lamentações",      "Lm",   "Lamentations",     5, "Old"),
    Book(26, "Ezequiel",         "Ez",   "Ezekiel",         "Ezk",  "Ezequiel",         "Ez",   "Ezekiel",         48, "Old"),
    Book(27, "Daniel",           "Dn",   "Daniel",          "Dan",  "Daniel",           "Dn",   "Daniel",          12, "Old"),
    Book(28, "Oseas",            "Os",   "Hosea",           "Hos",  "Oseias",           "Os",   "Hosea",           14, "Old"),
    Book(29, "Joel",             "Jl",   "Joel",            "Jol",  "Joel",             "Jl",   "Joel",             3, "Old"),
    Book(30, "Amós",             "Am",   "Amos",            "Amo",  "Amós",             "Am",   "Amos",             9, "Old"),
    Book(31, "Abdías",           "Abd",  "Obadiah",         "Oba",  "Obadias",          "Ob",   "Obadiah",          1, "Old"),
    Book(32, "Jonás",            "Jon",  "Jonah",           "Jon",  "Jonas",            "Jn",   "Jonah",            4, "Old"),
    Book(33, "Miqueas",          "Mi",   "Micah",           "Mic",  "Miquéias",         "Mq",   "Micah",            7, "Old"),
    Book(34, "Nahúm",            "Nah",  "Nahum",           "Nam",  "Naum",             "Na",   "Nahum",            3, "Old"),
    Book(35, "Habacuc",          "Hab",  "Habakkuk",        "Hab",  "Habacuque",        "Hc",   "Habakkuk",         3, "Old"),
    Book(36, "Sofonías",         "Sof",  "Zephaniah",       "Zep",  "Sofonias",         "Sf",   "Zephaniah",        3, "Old"),
    Book(37, "Hageo",            "Hag",  "Haggai",          "Hag",  "Ageu",             "Ag",   "Haggai",           2, "Old"),
    Book(38, "Zacarías",         "Zac",  "Zechariah",       "Zec",  "Zacarias",         "Zc",   "Zechariah",       14, "Old"),
    Book(39, "Malaquías",        "Mal",  "Malachi",         "Mal",  "Malaquias",        "Ml",   "Malachi",          4, "Old"),
    # Nuevo Testamento (27)
    Book(40, "Mateo",            "Mt",   "Matthew",         "Mat",  "Mateus",           "Mt",   "Matthew",         28, "New"),
    Book(41, "Marcos",           "Mr",   "Mark",            "Mrk",  "Marcos",           "Mc",   "Mark",            16, "New"),
    Book(42, "Lucas",            "Lc",   "Luke",            "Luk",  "Lucas",            "Lc",   "Luke",            24, "New"),
    Book(43, "Juan",             "Jn",   "John",            "Jhn",  "João",             "Jo",   "John",            21, "New"),
    Book(44, "Hechos",           "Hch",  "Acts",            "Act",  "Atos",             "At",   "Acts",            28, "New"),
    Book(45, "Romanos",          "Ro",   "Romans",          "Rom",  "Romanos",          "Rm",   "Romans",          16, "New"),
    Book(46, "1 Corintios",      "1 Co", "1 Corinthians",   "1Co",  "1 Coríntios",      "1Co",  "1 Corinthians",   16, "New"),
    Book(47, "2 Corintios",      "2 Co", "2 Corinthians",   "2Co",  "2 Coríntios",      "2Co",  "2 Corinthians",   13, "New"),
    Book(48, "Gálatas",          "Gá",   "Galatians",       "Gal",  "Gálatas",          "Gl",   "Galatians",        6, "New"),
    Book(49, "Efesios",          "Ef",   "Ephesians",       "Eph",  "Efésios",          "Ef",   "Ephesians",        6, "New"),
    Book(50, "Filipenses",       "Flp",  "Philippians",     "Php",  "Filipenses",       "Fp",   "Philippians",      4, "New"),
    Book(51, "Colosenses",       "Col",  "Colossians",      "Col",  "Colossenses",      "Cl",   "Colossians",       4, "New"),
    Book(52, "1 Tesalonicenses", "1 Ts", "1 Thessalonians", "1Th",  "1 Tessalonicenses","1Ts",  "1 Thessalonians",  5, "New"),
    Book(53, "2 Tesalonicenses", "2 Ts", "2 Thessalonians", "2Th",  "2 Tessalonicenses","2Ts",  "2 Thessalonians",  3, "New"),
    Book(54, "1 Timoteo",        "1 Ti", "1 Timothy",       "1Ti",  "1 Timóteo",        "1Tm",  "1 Timothy",        6, "New"),
    Book(55, "2 Timoteo",        "2 Ti", "2 Timothy",       "2Ti",  "2 Timóteo",        "2Tm",  "2 Timothy",        4, "New"),
    Book(56, "Tito",             "Tit",  "Titus",           "Tit",  "Tito",             "Tt",   "Titus",            3, "New"),
    Book(57, "Filemón",          "Flm",  "Philemon",        "Phm",  "Filemom",          "Fm",   "Philemon",         1, "New"),
    Book(58, "Hebreos",          "He",   "Hebrews",         "Heb",  "Hebreus",          "Hb",   "Hebrews",         13, "New"),
    Book(59, "Santiago",         "Stg",  "James",           "Jas",  "Tiago",            "Tg",   "James",            5, "New"),
    Book(60, "1 Pedro",          "1 P",  "1 Peter",         "1Pe",  "1 Pedro",          "1Pe",  "1 Peter",          5, "New"),
    Book(61, "2 Pedro",          "2 P",  "2 Peter",         "2Pe",  "2 Pedro",          "2Pe",  "2 Peter",          3, "New"),
    Book(62, "1 Juan",           "1 Jn", "1 John",          "1Jn",  "1 João",           "1Jo",  "1 John",           5, "New"),
    Book(63, "2 Juan",           "2 Jn", "2 John",          "2Jn",  "2 João",           "2Jo",  "2 John",           1, "New"),
    Book(64, "3 Juan",           "3 Jn", "3 John",          "3Jn",  "3 João",           "3Jo",  "3 John",           1, "New"),
    Book(65, "Judas",            "Jud",  "Jude",            "Jud",  "Judas",            "Jd",   "Jude",             1, "New"),
    Book(66, "Apocalipsis",      "Ap",   "Revelation",      "Rev",  "Apocalipse",       "Ap",   "Revelation",      22, "New"),
]


def total_chapters() -> int:
    return sum(b.expected_chapters for b in BOOKS)


if __name__ == "__main__":
    assert len(BOOKS) == 66
    assert sum(1 for b in BOOKS if b.testament == "Old") == 39
    assert sum(1 for b in BOOKS if b.testament == "New") == 27
    print(f"66 libros, {total_chapters()} capítulos totales")
    # Spot checks de localización
    for lang in ("es", "en", "pt"):
        print(f"  {lang}: {BOOKS[0].name(lang)}, {BOOKS[18].name(lang)}, {BOOKS[42].name(lang)}, {BOOKS[65].name(lang)}")

# Usage guide — holyrics-bible-builder

[🇪🇸 Español](USAGE.md) · **🇬🇧 English (you are here)** · [🇵🇹 Português](USAGE.pt.md)

This guide is written so that **anyone** — even without prior terminal
experience — can use the included translations or generate the ones they need.

If you just want to download **Reina-Valera 1909** and import it into Holyrics,
go straight to **[Case 1](#case-1-i-want-to-use-an-included-translation-rv1909)**.

---

## Table of contents

- [Before you start](#before-you-start)
- [Case 1: I want to use an included translation (RV1909)](#case-1-i-want-to-use-an-included-translation-rv1909)
- [Case 2: I want to generate another translation (advanced)](#case-2-i-want-to-generate-another-translation-advanced)
  - [Generate another translation](#generate-another-translation)
  - [Available translations](#available-translations-on-ebibleorg)
  - [Verify that the text matches the source](#verify-that-the-text-matches-the-source)
- [Case 3: I want a modern, copyrighted translation](#case-3-i-want-a-modern-copyrighted-translation)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)

---

## Before you start

You need:

- **Holyrics** installed on your Mac or PC (download from <https://www.holyrics.com.br/>).
- For Cases 2 and 3 (generating new translations): **Python 3.10+** (already
  bundled on Mac; on Windows download from <https://www.python.org/downloads/>).

You don't need programming knowledge for Case 1. For the rest, it's just
copy-and-paste of commands.

---

## Case 1: I want to use an included translation (RV1909)

**Reina-Valera 1909** is already generated, validated, and ready to import.

### Step 1: Download the file

1. Go to the repository page:
   <https://github.com/leofernandezg/holyrics-bible-builder>
2. Open the folder `output/public-domain/`.
3. Click the file `rv1909.xml`.
4. On the file page, click **"Download raw file"** (the download icon at
   the top right of the file viewer).
5. Save it to your Desktop or any convenient location.

### Step 2: Import into Holyrics

1. Open **Holyrics**.
2. On the main screen, click **"Go to Bible"** (in Spanish: "Ir a la Biblia").
3. In the top menu bar, click the **"Version"** menu.
4. Go to **"Import"** → **"Zefania XML"**.
5. Browse to and select the `rv1909.xml` file you downloaded.
6. A dialog **"Import - Bible"** opens with the ID, Name, Language and Description fields pre-filled (Holyrics reads them from the `<INFORMATION>` block of the XML). Click **"Ok"**.
7. Holyrics processes the file (10-30 seconds).
8. When done, the translation is available in the version dropdown, grouped by language.

### Step 3: Test it

1. In the Bible view, click the **version dropdown arrow** (top left, next to the current version).
2. Under the **"Spanish"** section, select **"Reina-Valera 1909"**.
3. Look up, for example, **John 3:16** — you should see:
   > Porque de tal manera amó Dios al mundo, que ha dado á su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.

✅ Done! You can now project verses in RV1909.

### Installing on multiple machines (e.g., the church PC)

- **Option A:** repeat Step 1 + Step 2 on each machine.
- **Option B:** after importing on one machine, copy the `.bib` file that
  Holyrics generated (located in
  `~/Holyrics/Holyrics/files/Bible LG/` on Mac, or
  `C:\Holyrics\Holyrics\files\Bible LG\` on Windows) to the same folder on
  the other machine.

---

## Case 2: I want to generate another translation (advanced)

Works for translations available on [ebible.org](https://ebible.org/). You'll
need Python installed.

### Step 1: Set up the project (first time only)

Open the **Terminal** (Mac: ⌘+Space, type "Terminal"; Windows: "PowerShell"
or "cmd").

Copy and paste these commands, one line at a time:

```bash
# 1. Clone the code (needs git installed; otherwise download the ZIP from GitHub)
git clone https://github.com/leofernandezg/holyrics-bible-builder.git
cd holyrics-bible-builder

# 2. Create an isolated virtual environment
python3 -m venv .venv

# 3. Install dependencies
.venv/bin/pip install lxml beautifulsoup4 requests
```

If it asks you to install `pip` or throws any error, open an issue on GitHub
and we'll help.

### Generate another translation

Each translation on ebible.org has a short **ID**. For example:

- Reina-Valera 1909 → `spaRV1909`
- King James Version → `engKJV`
- World English Bible → `eng-web`

To generate, run this command, replacing the values in quotes with the ones
for your translation:

```bash
.venv/bin/python scripts/build_from_ebible.py spaRV1909 \
    --title "Reina-Valera 1909" \
    --identifier RV1909 \
    --date 1909 \
    --rights "Public Domain" \
    --out output/public-domain/rv1909.xml
```

When done, you'll have the `.xml` file ready to import into Holyrics
(follow Step 2 of Case 1).

### Available translations on eBible.org

These are the translations the pipeline already supports (all redistributable):

| Translation | ID on ebible | Language | License | Command |
|---|---|---|---|---|
| Reina-Valera 1909 | `spaRV1909` | Spanish (`spa`) | Public domain | (see above) |
| Bíblia Livre | `porbr2018` | Portuguese (`por`) | CC BY 4.0 BR | attribution required |
| King James Version | `engKJV` | English (`eng`) | Public domain (outside UK) | use `--slug eng-kjv2006` |
| American Standard Version | `eng-asv` | English (`eng`) | Public domain | — |
| World English Bible | `eng-web` | English (`eng`) | Public domain dedicated | — |
| Young's Literal Translation | `engylt` | English (`eng`) | Public domain | — |
| Darby Translation | `engdby` | English (`eng`) | Public domain | — |

Full ebible search: <https://ebible.org/find/>. **Always verify the exact license** at `ebible.org/<ID>/copyright.htm` before redistributing the generated `.xml`.

> ⚠️ Some ebible.org packages have a download "slug" that differs from the page `id` (for instance KJV: id `engKJV`, slug `eng-kjv2006`). If the download fails with 404, check the USFX zip URL on the detail page and pass it via `--slug`.

### Verify that the text matches the source

The pipeline includes three layers of tests. Run all three after generating:

```bash
# 1. Basic structural validation (1 s)
.venv/bin/python scripts/validate_xml.py output/public-domain/rv1909.xml

# 2. Exhaustive shape tests: encoding, canon, numbering, no residual markup,
#    no control characters, spot-checks of key verses (~2 s)
.venv/bin/python scripts/test_structure.py output/public-domain/rv1909.xml

# 3. Character-by-character fidelity against the ebible.org USFX (~10 s)
.venv/bin/python scripts/test_fidelity_usfx.py spaRV1909 output/public-domain/rv1909.xml
```

If all three pass, the `.xml` is bit-exact reproducible — anyone who repeats
the pipeline gets the same hash.

To also generate a SHA-256 hash for comparison between machines:

```bash
shasum -a 256 output/public-domain/rv1909.xml > output/public-domain/rv1909.xml.sha256
```

---

## Case 3: I want a modern, copyrighted translation

⚠️ **Before continuing, read [LEGAL.en.md](LEGAL.en.md).** Modern translations
(RVC, RVR1960, NIV, NLT, NASB, etc.) are **copyrighted** by their respective
publishers. The standard quotation allowance (500-1,000 verses depending on
the publisher) covers projecting individual verses during worship, but it
**does not cover keeping a complete digital copy** nor redistributing the
file. In practice publishers rarely pursue internal church use, but it is
not formally authorized and depends on your jurisdiction's fair use / fair
dealing doctrine. See [LEGAL.en.md §3](LEGAL.en.md) for the full analysis.

This repository **does not include tools** to download copyrighted
translations from sites that don't publish them explicitly (BibleGateway,
YouVersion, etc.) — their terms of service prohibit automated access and,
even if technically possible, redistributing the resulting file would be
copyright infringement (see [LEGAL.en.md §4](LEGAL.en.md)).

### The proper path

- Buy the official digital edition from the publisher (when available).
- Or contact the publisher and request specific permission to project it
  in Holyrics:
  - **Sociedad Bíblica Argentina** (RVR1960, RVR1995, DHH, TLA): <https://sba.org.ar/politica-sobre-derechos-y-permisos-de-uso-de-los-textos-biblicos/>
  - **Biblica** (NIV / NVI): <https://www.biblica.com/permissions/>
  - **Tyndale** (NLT / NTV): <https://www.tyndale.com/permissions>
  - **Lockman Foundation** (NASB / LBLA / NBLA): <https://www.lockman.org/permission-to-quote-copyright-trademark-information/>

---

## Troubleshooting

### "tag not found: XMLBIBLE" when importing in Holyrics

Holyrics only accepts the **Zefania XML** format (root `<XMLBIBLE>`). If you
downloaded an `.xml` not from this project, it may be in a different format
(Beblia, OSIS, USFM) which Holyrics rejects. Verify the file starts with:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XMLBIBLE biblename="...">
```

### Holyrics hangs while importing

Try closing and reopening Holyrics. If it persists, check the file size —
a complete Bible `.xml` weighs between 4 and 7 MB. If it's much smaller,
it's incomplete.

### "command not found: python3"

On Windows use `py` or `python` (without the 3). On Mac, install Python
from <https://www.python.org/downloads/>.

### `git clone` doesn't work

Install git from <https://git-scm.com/downloads>. Or download the repo as
ZIP via the green **"Code → Download ZIP"** button on GitHub.

### I want to verify a file hasn't been modified

Each included translation ships with a `.sha256` file alongside. To check:

```bash
# Mac/Linux
shasum -a 256 output/public-domain/rv1909.xml
# Must match what rv1909.xml.sha256 says

# Windows PowerShell
Get-FileHash output\public-domain\rv1909.xml -Algorithm SHA256
```

---

## Glossary

- **Zefania XML**: standard format for digital Bibles that Holyrics imports.
  Structure: `<XMLBIBLE><BIBLEBOOK><CHAPTER><VERS>`.
- **USFX**: XML format used internally by ebible.org. Not directly importable
  by Holyrics; this project converts it to Zefania.
- **`.bib`**: Holyrics' internal binary format. Generated automatically when
  you import the `.xml`. Don't edit by hand.
- **Public domain**: a work whose copyright expired (or never had one).
  Anyone can use, copy, and redistribute it.
- **66-book canon**: 39 Old Testament + 27 New Testament books, without
  deuterocanonical books. Standard in Protestant churches.

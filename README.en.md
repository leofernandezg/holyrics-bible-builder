# holyrics-bible-builder

[🇪🇸 Español](README.md) · **🇬🇧 English (you are here)** · [🇵🇹 Português](README.pt.md)

A free tool to **import Bible translations into [Holyrics](https://www.holyrics.com.br/)**
using the Zefania XML format, and to **verify that the generated text is
character-for-character identical** to the source.

Built for churches that want to project Bible verses during worship services
and can't find the translation they need in the usual community repositories.

---

## What does it do?

Holyrics needs a `.xml` file (Zefania format) to add a new Bible translation.
Traditional translations like Reina-Valera 1960 or NIV come pre-packaged in
many community websites, but **other translations (such as the Reina-Valera
Contemporánea) don't exist as ready-made downloads anywhere**.

This project:

1. **Ships ready-to-import `.xml` files** in `output/public-domain/`.
2. **Lets you generate other translations** available in legally clean,
   open sources (like [ebible.org](https://ebible.org)).
3. **Validates automatically** that the generated text is identical to the
   source — character by character, across all 31,000+ verses.

## Translations included

The 6 most widely used translations in Spanish, Portuguese and English whose license permits redistribution:

| Translation | Language | Year | License | Download |
|---|---|---|---|---|
| Reina-Valera 1909 | Spanish | 1909 | Public domain | [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml) |
| Bíblia Livre | Portuguese | 2018 | CC BY 4.0 Brasil | [`output/public-domain/biblia-livre.xml`](output/public-domain/biblia-livre.xml) |
| King James Version (1769) | English | 1611 | Public domain (outside the UK) | [`output/public-domain/kjv.xml`](output/public-domain/kjv.xml) |
| American Standard Version | English | 1901 | Public domain | [`output/public-domain/asv.xml`](output/public-domain/asv.xml) |
| World English Bible | English | 2020 | Public domain (dedicated) | [`output/public-domain/web.xml`](output/public-domain/web.xml) |
| Young's Literal Translation | English | 1898 | Public domain | [`output/public-domain/ylt.xml`](output/public-domain/ylt.xml) |

All structurally validated and **character-by-character against the original source on [ebible.org](https://ebible.org)**. See [LEGAL.md](LEGAL.md) for license details.

> ⚠️ Modern translations like **RVC, RVR1960, NIV, NLT, NASB** are copyrighted
> and **not included here**. If you want to generate them for your church's
> internal use, there is a documented path in [USAGE.md](USAGE.en.md), but
> **read [LEGAL.md](LEGAL.md) first** to understand the implications.

## I just want to import RV1909 into Holyrics (quick)

1. Download [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml).
2. Open Holyrics → ⚙ (gear icon) → **Settings** → **Bibles** → **Import**.
3. Select the `rv1909.xml` file. Done.

Stuck? The step-by-step guide (written for non-technical users) lives in
**[USAGE.en.md](USAGE.en.md)**.

## I want to generate another translation

If the translation you need is available on [ebible.org](https://ebible.org/),
it generates with a single command. See **[USAGE.en.md → "Generate another translation"](USAGE.en.md#generate-another-translation)**.

## Documentation

- **[USAGE.en.md](USAGE.en.md)** — Step-by-step install/usage guide for
  non-technical users.
- **[LEGAL.md](LEGAL.md)** — Copyright analysis: which translations are safe
  to redistribute and which are not. **Required reading** before publishing.
- **[LICENSE](LICENSE)** — MIT (code only; Bible texts have their own licenses).

## Contributing

PRs welcome for:

- Adding adapters for other free sources (Crosswire SWORD, Open Scriptures, etc.)
- Pre-packaging more public-domain translations
- Improving translations of this documentation

Issues welcome for reporting bugs in the generated text, problems importing
into Holyrics, or suggestions.

## Credits

- Code: [Leonardo Fernández García](https://github.com/leofernandezg), MIT licensed.
- Public-domain texts: original translators (Reina y Valera, 1909, etc.).
- Free source hosting: [eBible.org](https://ebible.org).

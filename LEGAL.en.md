# Legal framework — read before using

[🇪🇸 Español](LEGAL.md) · **🇬🇧 English (you are here)** · [🇵🇹 Português](LEGAL.pt.md)

> **Disclaimer:** this document is an informational analysis, **not legal advice**.
> If you have doubts about a specific case, consult a lawyer or contact the
> copyright holder of the translation you want to use directly.

## TL;DR

| What this repo does | Is it legal? |
|---|---|
| Publishing the code (builder, validators, ebible.org adapter) | ✅ Yes (MIT) |
| Bundling **public-domain** translations (RV1909, KJV, WEB, etc.) | ✅ Yes — the text is free |
| **Locally** generating a modern translation (RVC, NIV, RVR1960...) and using it at your church | ⚠️ Unauthorized reproduction of the complete work: quotation policies (500-1,000 verses depending on the publisher) cover projecting individual verses, but do NOT cover keeping a complete digital copy. Publishers rarely pursue these uses in churches, but it is not formally authorized |
| **Publicly redistributing** a modern translation in any format | ❌ **No** — copyright infringement |

This repo is designed so that it is **impossible** to accidentally fall into the red case: `.gitignore` explicitly excludes `sources/*-cache/`, `output/rvc.xml`, `output/rvr1960.xml`, etc. The repo only distributes an adapter for [ebible.org](https://ebible.org), which publishes its texts for redistribution under explicit license.

---

## 1. Why are there copyrighted Bible translations?

Many people assume that "the Bible is in the public domain". That is true of the **source text** (Hebrew, Aramaic, Greek — all written 2,000+ years ago), but **not of modern translations**.

Each translation into English/Spanish/etc. is a **derivative work** created by contemporary translators, editors and revisers. Under the [Berne Convention](https://www.wipo.int/treaties/en/ip/berne/) (in force in virtually every country), a translation is a new creative work with its own copyright. Authorship belongs to the translator (or translation team); ownership of the economic rights depends on the contract under which the translation was made and the applicable labor regime (in the US, [17 USC §201(b)](https://www.law.cornell.edu/uscode/text/17/201) "work made for hire"; in Argentina, [Law 11.723 art. 16](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm)). In practice almost all modern Bible translations are published with ownership held by the Bible society or publishing house that commissioned them.

The Berne Convention provisions that support this:

1. **Art. 2(3)** — "Translations, adaptations, arrangements of music and other alterations of a literary or artistic work shall be protected as original works without prejudice to the copyright in the original work." Applied here: even though the original biblical text (Hebrew/Greek) is in the public domain due to age, a modern translation from the 20th or 21st century has its own autonomous copyright.
2. **Art. 5(2)** — "The enjoyment and the exercise of these rights shall not be subject to any formality." Applied here: there is no "Bible without copyright" by oversight — if the publisher hasn't explicitly released the text and the term hasn't expired, it is protected by default in any signatory jurisdiction, without need for registration or the © symbol.
3. **Art. 7(1)** — the **minimum** term of protection is the life of the author plus 50 years. Almost all signatories extended that term (see below). Applied here: translations from the 19th century or earlier (Sagradas Escrituras 1569, Reina-Valera Antigua 1602, RV1909) are in the public domain; modern ones (RVC 2011, RVR1960, NIV 1999) remain protected throughout the 21st century.

### Copyright term — by jurisdiction

The term depends on who holds the rights and which country applies:

- **Argentina, EU, most of Latin America** (Berne + national extensions): life of the author plus **70 years** from January 1st of the year following their death ([Law 11.723 art. 5](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm) for Argentina). For collaborative works, from the death of the last collaborator. For anonymous or corporate works, **70 years from publication**.
- **USA** (post-1978): for "work made for hire" or anonymous/pseudonymous works, **95 years from publication** or **120 years from creation**, whichever comes first (17 USC §302(c)). For pre-1978 works, rules vary based on renewal; the current cutoff (as of January 1, 2026) is: **any work published before 1931 is in the US public domain** ([Cornell/Hirtle chart](https://copyright.cornell.edu/publicdomain)).

Estimated terms for the most common translations:

| Translation | Pub. year | Argentina/EU (~70 from pub.) | USA (95 from pub.) | PD starting from |
|---|---|---|---|---|
| RVC | 2011 | 2081 | 2106 | the later one |
| RVR1960 | 1960 | 2030 | 2055 | 2055 |
| RVR1995 | 1995 | 2065 | 2090 | 2090 |
| NIV | 1999 | 2069 | 2094 | 2094 |
| LBLA | 1986 | 2056 | 2081 | 2081 |
| RV1909 | 1909 | (authors dead > 70 years) | < 1931 → already PD | **already in PD** |

These terms are indicative: they may vary if the actual ownership is held by natural persons and the term runs post mortem.

---

## 2. Translations you **can** freely redistribute

This repo ships with 6 pre-packaged translations in `output/public-domain/`. We chose them as the most widely used in Spanish, Portuguese and English whose text can be redistributed. Each license is checked against its respective source:

| Translation | Language | Year | License | Verified source |
|---|---|---|---|---|
| **Reina-Valera 1909** (`rv1909.xml`) | Spanish | 1909 | Public domain (declared by the source; confirmed by age — see §1) | [ebible.org/spaRV1909](https://ebible.org/find/details.php?id=spaRV1909) · [Project Gutenberg #5881](https://www.gutenberg.org/ebooks/5881) |
| **Bíblia Livre** (`biblia-livre.xml`) | Portuguese | 2018 | [Creative Commons Attribution 4.0 Brasil](https://creativecommons.org/licenses/by/4.0/) — allows redistribution with attribution. Copyright © 2018 Diego Santos, Mario Sérgio, e Marco Teles. Attribution goes in the `<INFORMATION>` block of the XML; do not remove it. | [ebible.org/porbr2018](https://ebible.org/find/details.php?id=porbr2018) |
| **King James Version** (`kjv.xml`, 1769 standardized text) | English | 1611 | Public domain outside the United Kingdom. In the UK there are [royal Letters Patent](https://en.wikipedia.org/wiki/Authorized_King_James_Version#Permission) granting exclusive rights to Cambridge/Oxford/Collins — does not apply outside the UK. | [ebible.org/engKJV](https://ebible.org/find/details.php?id=engKJV) |
| **American Standard Version** (`asv.xml`) | English | 1901 | Public domain (US copyright expired by age — before 1931). Textual basis for RSV, NASB and ESV. | [ebible.org/eng-asv](https://ebible.org/find/details.php?id=eng-asv) |
| **World English Bible** (`web.xml`) | English | started 1994, completed 2020 | Text explicitly dedicated to the public domain. The "World English Bible" trademark is registered by **eBible.org** and cannot be reused to identify modified versions; the text itself is copyright-free. | [ebible.org/eng-web](https://ebible.org/find/details.php?id=eng-web) |
| **Young's Literal Translation** (`ylt.xml`) | English | 1898 | Public domain (US copyright expired by age). Highly literal translation of Hebrew and Greek by Robert Young. | [ebible.org/engylt](https://ebible.org/find/details.php?id=engylt) |

To add other free translations, first **verify the copyright page of the specific source** (`ebible.org/<id>/copyright.htm`) and open an issue with the link.

> ⚠️ **Beware of similar-sounding names:**
> - "Reina-Valera Gómez (RVG)" 2004/2010/2023 is NOT public domain — it is a modern revision with its own copyright held by Dr. Humberto Gómez Caballero and specific restrictions.
> - The modern Almeida revisions (ARA, ARC, NAA, NTLH) are also not public domain — each has copyright held by SBB or SBTB. Only Bíblia Livre (2018) is freely redistributable in modern Portuguese.
> - RVR1960, RVR1995, NIV, NLT, NASB, etc. are all under active copyright.

---

## 3. Modern translations (RVC, RVR1960, NIV, NLT...): what's allowed and what's not

### Typical Bible-society policy for church use

Each publisher has its own policy (verified links in References). The common pattern — with an important nuance below — is:

> Verses may be quoted in non-commercial printed or digital publications up to a limit, **provided that**:
> 1. Quotations do not exceed a percentage of the total work containing them.
> 2. They do **not constitute a complete book** of the Bible.
> 3. Visible credit is given to the publisher (or, for internal church use, at least the abbreviation).

The specific limits vary:

| Publisher | Translations | Limit without permission | Max % of the work |
|---|---|---|---|
| Sociedad Bíblica Argentina (UBS) | RVR1960, RVR1995, DHH, TLA | 500 verses | 25% (50% per Bible book) |
| Biblica | NVI, NIV, NIrV | 500 verses | 25% |
| Tyndale | NTV, NLT | 500 verses | 25% |
| Sociedade Bíblica do Brasil | ARA, ARC, NAA, NTLH | 1,100 verses | 50% per book |
| Lockman Foundation | LBLA, NBLA, NASB, Amplified | **1,000 verses** | **50%** |

For internal church use (bulletins, transparencies, projection during worship), the first four policies allow omitting the full copyright notice if the abbreviation is included (`(RVR1960)`, `(NIV)`, `(NLT)`, `(ACF)`) at the end of each quotation.

### How this applies to Holyrics use

- ✅ **Projecting individual verses during worship, citing the abbreviation**: falls within quotation policy — the "service" is its own work that briefly quotes another.
- ⚠️ **Holyrics keeping the complete text locally** for searching and projecting: this is a **reproduction of the complete work** that the quotation policy does not cover. In practice publishers almost never pursue this church use — economic loss is marginal and the reputational cost is high — but **it is not formally authorized** and depends on the fair use / fair dealing doctrine of your jurisdiction, which differs from country to country.
- ⚠️ **Distributing the complete `.xml` or `.bib` file to another church**: redistribution of the complete work, outside the quotation framework. The correct approach is for each church to generate its own file on its own machine.
- ❌ **Uploading the `.xml` to a public repository (GitHub, gist, indexed dropbox, etc.)**: clear infringement. Public, permanent distribution + global access + indefinite availability + potential substitution for the commercial product. Enables a DMCA claim from the publisher with consequences for your account and the repo.

### Why this repo does NOT redistribute modern translations

Even if your individual use is likely covered by quotation policy for worship, publishing the file on GitHub would mean:

- Public and permanent distribution, not internal use.
- Global access without confessional filter.
- Search-engine indexing → a user could download the entire Bible avoiding having to buy the official digital edition.
- Potential DMCA claim from the publisher → takedown of your repository and your account.

That's why the pipeline generates these translations **locally on your machine**, and `.gitignore` prevents them from being committed.

---

## 4. Text sources: what can be used

To feed the pipeline, this repo supports a single legally clean source:

- **[ebible.org](https://ebible.org)** — explicitly publishes its packages for redistribution under the license each package declares on its `copyright.htm` page. Most are public domain. Used by the `scripts/fetch_ebible.py` adapter.

**About scraping other Bible sites** (BibleGateway, YouVersion, Bible Online, etc.): almost all prohibit automated access in their Terms of Use. For example the [BibleGateway Terms of Use](https://www.biblegateway.com/legal/terms/) (in force as of 2025-06-04, HarperCollins Christian Publishing) prohibit "automated data collection" and only authorize quotation up to 250 verses or 500 words for non-commercial purposes — reproducing the entire Bible exceeds that limit by two orders of magnitude. That's why this repo does not include scrapers or adapters for those sources.

For modern translations you need at your church, consider purchasing the official digital edition from the publisher or contacting them to request a specific license (links in References).

---

## 5. If you want to publish your own generated translation

Before uploading any `.xml` or `.bib` to a public repository:

- [ ] **Is the translation in the public domain?** Confirm both ways: (a) the source you got it from declares it explicitly on its copyright page, and (b) by age (authors dead > 70 years, or published before 1931 if you also care about the US). If it passes both, it's free.
- [ ] **If it has active copyright, do you have a written license from the publisher covering reproduction and redistribution in electronic format for public internet use?** Standard quotation policies (500-1,000 verses) do NOT count — to publish the complete file you need a specific signed license.
- [ ] **Did the publisher release the text under Creative Commons or another open license?** Verify the exact variant. CC BY and CC0 allow redistribution; CC BY-NC prohibits commercial use (and many open projects count as "commercial"); CC BY-ND prohibits derivatives (including format conversion).
- [ ] **Did you remove any mention of the publisher's trademark from the filename and the repo name?** Just because the work is free doesn't mean you can reuse the trademark to identify your package (see §7).

Links to the major publishers' policies are in the References section.

---

## 6. Attribution included in the generated XML files

Every XML generated by this pipeline includes an `<INFORMATION>` block with the `title`, `creator`, `publisher`, `date`, `identifier`, `language`, `source` and `rights` fields. Holyrics exposes this block on the translation's information screen so users can consult it.

Rules to maintain the integrity of the `rights` field:

- **Public-domain** translations: `<rights>Public Domain</rights>`. This is what is already committed for RV1909.
- **Copyrighted** translations generated locally: the field must contain the real publisher's notice, e.g. `Copyright © 2011 Sociedades Bíblicas Unidas`. If omitted or falsified, beyond the underlying legal issue, traceability is lost and the end user could mistakenly assume the translation is free.

**Do not hand-edit** the `<INFORMATION>` block in the generated XMLs. If you need to change attribution, modify the builder parameters (`--rights`, `--publisher`, etc. in `build_from_ebible.py`) and regenerate.

---

## 7. On the translation names mentioned in this repo

The names "Reina-Valera Contemporánea (RVC)", "Reina-Valera 1960 (RVR1960)",
"Nueva Versión Internacional (NVI)", "Nueva Traducción Viviente (NTV)",
"La Biblia de las Américas (LBLA)", "Almeida Corrigida Fiel (ACF)",
"Almeida Revista e Atualizada (ARA)", "King James Version (KJV)", and any
other similar designations are **titles and/or trademarks** of their
respective publishers (Sociedades Bíblicas Unidas, Biblica/Vida, Tyndale,
Lockman, Sociedade Bíblica do Brasil, Sociedade Bíblica Trinitariana, etc.).

Their mention in this repository (README, USAGE, LEGAL, code comments)
is exclusively for **referential identification**, so the user can know
which translation we are referring to. It does not imply:

- Endorsement, sponsorship, or association of those publishers with this project.
- That this project is an official version of those translations.
- Authorization to redistribute their text (which remains protected — see
  sections 1 to 5 above).

This use falls under what doctrine knows as **nominative fair use**
(US) / **referential use** (EU, Latin America): the minimum name necessary
to identify the work is used, without graphics, logos or distinctive
elements of the publisher, and without suggesting connection.

If you hold rights over any of these names and consider that a particular
use exceeds the referential, open an issue on GitHub and we'll adjust it.

## References

All URLs in this section are verified as of 2026-05-21. If you find a broken link, open an issue.

### International treaties and legislation

- **[Berne Convention for the Protection of Literary and Artistic Works](https://www.wipo.int/treaties/en/ip/berne/)** (WIPO, English text) — Basis of the international copyright regime. Relevant articles cited in section 1: Art. 2(3) (translations as protected works), Art. 5(2) (automatic protection without formality), Art. 7(1) (minimum term of life + 50 years).
- **[Law 11.723 — Legal Regime of Intellectual Property (Argentina)](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm)** (InfoLEG, current text, Spanish) — Art. 5: copyright lasts the life of the author plus **70 years** after January 1st of the year following their death. For collaborative works, the term runs from the death of the last collaborator. This is the applicable term in Argentina and similar in the EU and US for post-1978 works.
- **[Copyright Term and the Public Domain in the United States](https://copyright.cornell.edu/publicdomain)** (Cornell University Library, chart by Peter B. Hirtle, classic authority) — Canonical table for determining if a work is in the US public domain. Current rule: **every work published before 1931** is in the US public domain as of January 1, 2026 (the cutoff advances one year every January 1). Always-available mirror: [Wikimedia Commons](https://commons.wikimedia.org/wiki/Commons:Hirtle_chart).

### Bible societies and publishers' policies (source of 90% of modern translations)

- **[Sociedad Bíblica Argentina — Policy on rights and permissions](https://sba.org.ar/politica-sobre-derechos-y-permisos-de-uso-de-los-textos-biblicos/)** — 500-verse limit without written permission, not exceeding 25% of the work nor 50% of a complete Bible book. Covers RVR1960, RVR1995, DHH, TLA. For quotations in bulletins, transparencies and similar non-commercial uses, just the abbreviation at the end of each quotation suffices.
- **[Sociedade Bíblica do Brasil — End User License Agreement](https://www.sbb.org.br/acordo-de-licenca-de-usuario-final-eula)** — Policy similar to SBA's, applies to ARA, ARC, NAA, NTLH. Contact for extended permissions: `direitos@sbb.org.br`.
- **[Biblica — Permissions](https://www.biblica.com/permissions/)** (NVI / NIV / NIrV) — 500-verse limit without written permission, not exceeding 25% of the total nor a complete Bible book. For non-commercial church use (bulletins, transparencies) the abbreviation "NVI®"/"NIV®" suffices.
- **[Tyndale — Permissions](https://www.tyndale.com/permissions)** (NTV / NLT) — 500-verse limit in any printed or digital medium, same 25%/complete book as the others. Credit required in salable works.
- **[Lockman Foundation — Permission to Quote (NASB, NBLA, LBLA, Amplified)](https://www.lockman.org/permission-to-quote-copyright-trademark-information/)** — Broader limit: up to 1,000 verses without written permission, not exceeding 50%. Spanish version: [Permiso para citar](https://www.lockman.org/espanol/permiso-para-citar/).

### Sources and technical policies of the providers this repo uses

- **[eBible.org — Intellectual Property Policy](https://ebible.org/legal.php)** — General policy: public-domain works can be freely copied, protected ones require permission from the rights holder; eBible publishes each package with its specific license on the package detail page (`ebible.org/<id>/copyright.htm`). We use it as a source for free translations.
- **[eBible.org — Bibles in the Public Domain](https://ebible.org/publicdomain.htm)** — Official list of packages eBible considers public domain, with the caveat that names may be registered as trademarks and that the KJV has restrictions in the United Kingdom (Letters Patent).
- **[BibleGateway — Terms of Use](https://www.biblegateway.com/legal/terms/)** (latest version: 2025-06-04, operated by HarperCollins Christian Publishing) — Relevant section: prohibition of "automated data collection" / scraping and of commercial use without permission. Quotation allowance up to 250 verses or 500 words non-commercial. That's why this repo does not include an adapter for BibleGateway (see §4).

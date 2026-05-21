# Marco legal — leer antes de usar

> **Disclaimer:** este documento es un análisis informativo, **no es asesoramiento legal**.
> Si tenés dudas sobre un caso particular, consultá con un abogado o directamente
> con el titular del copyright de la versión que querés usar.

## TL;DR

| Lo que hace este repo | ¿Es legal? |
|---|---|
| Publicar el código (builder, validators, adapter ebible.org) | ✅ Sí (MIT) |
| Empaquetar versiones de **dominio público** (RV1909, KJV, WEB, etc.) | ✅ Sí — el texto es libre |
| Generar **localmente** una versión moderna (RVC, NVI, RVR1960...) y usarla en tu iglesia | ⚠️ Reproducción no autorizada de la obra completa: las políticas de citas (500-1.000 versículos según el editor) cubren la proyección de versos individuales, pero NO cubren tener una copia digital completa. Los editores rara vez persiguen estos usos en iglesias, pero formalmente no está autorizado |
| **Redistribuir** públicamente una versión moderna en cualquier formato | ❌ **No** — infracción de copyright |

Este repo está diseñado para que sea **imposible** caer accidentalmente en el caso rojo: `.gitignore` excluye explícitamente `sources/*-cache/`, `output/rvc.xml`, `output/rvr1960.xml`, etc. El repo solo distribuye un adapter para [ebible.org](https://ebible.org), que publica sus textos para redistribución bajo licencia explícita.

---

## 1. ¿Por qué hay versiones bíblicas con copyright?

Mucha gente asume que "la Biblia es de dominio público". Eso es cierto del **texto fuente** (hebreo, arameo, griego — todo escrito hace 2.000+ años), pero **no de las traducciones modernas**.

Cada traducción al español/inglés/etc. es una **obra derivada** creada por traductores, editores y revisores contemporáneos. Bajo el [Convenio de Berna](https://www.wipo.int/treaties/es/ip/berne/) (en vigor en prácticamente todos los países), una traducción es una obra creativa nueva con su propio copyright. La autoría es del traductor (o equipo de traductores); la titularidad de los derechos patrimoniales depende del contrato bajo el cual se hizo la traducción y del régimen laboral aplicable (en Argentina, [Ley 11.723 art. 16](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm); en EE.UU., 17 USC §201(b) "work made for hire"). En la práctica casi todas las traducciones bíblicas modernas están publicadas con titularidad de la sociedad bíblica o editorial que las comisionó.

Las disposiciones del Convenio de Berna que sustentan esto:

1. **Art. 2(3)** — "Las traducciones, adaptaciones, arreglos musicales y demás transformaciones de una obra literaria o artística serán protegidos como obras originales, sin perjuicio de los derechos del autor de la obra original." Aplicado acá: aunque el texto bíblico original (hebreo/griego) esté en dominio público por antigüedad, una traducción moderna del s. XX o XXI tiene su propio copyright autónomo.
2. **Art. 5(2)** — "El goce y el ejercicio de estos derechos no estarán subordinados a ninguna formalidad." Aplicado acá: no existe una "Biblia sin copyright" por descuido — si el editor no liberó el texto explícitamente y no transcurrió el plazo, está protegido por default en cualquier jurisdicción signataria, sin necesidad de registro ni símbolo ©.
3. **Art. 7(1)** — el plazo **mínimo** de protección es la vida del autor más 50 años. Casi todos los signatarios elevaron ese plazo (ver más abajo). Aplicado acá: las traducciones del s. XIX o anteriores (Sagradas Escrituras 1569, Reina-Valera Antigua 1602, RV1909) están en dominio público; las modernas (RVC 2011, RVR1960, NVI 1999) están protegidas durante todo el s. XXI.

### Plazo del copyright — por jurisdicción

El plazo depende de quién es titular y de qué país aplica:

- **Argentina, UE, mayor parte de Latinoamérica** (Berne + extensiones nacionales): vida del autor más **70 años** desde el 1° de enero del año siguiente a su muerte ([Ley 11.723 art. 5](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm) para Argentina). Para obras en colaboración, desde la muerte del último colaborador. Para obras anónimas o corporativas, **70 años desde la publicación**.
- **EE.UU.** (post-1978): para obras "work made for hire" o anónimas/seudónimas, **95 años desde la publicación** o **120 años desde la creación**, lo que ocurra antes (17 USC §302(c)). Para obras pre-1978, las reglas varían según renovación; el cutoff actual (al 1° de enero de 2026) es: **toda obra publicada antes de 1931 está en dominio público en EE.UU.** ([Cornell/Hirtle chart](https://copyright.cornell.edu/publicdomain)).

Estimación de plazos para las traducciones más comunes:

| Versión | Año pub. | Argentina/UE (≈70 desde pub.) | EE.UU. (95 desde pub.) | DP a partir de |
|---|---|---|---|---|
| RVC | 2011 | 2081 | 2106 | el último que aplique |
| RVR1960 | 1960 | 2030 | 2055 | 2055 |
| RVR1995 | 1995 | 2065 | 2090 | 2090 |
| NVI | 1999 | 2069 | 2094 | 2094 |
| LBLA | 1986 | 2056 | 2081 | 2081 |
| RV1909 | 1909 | (autores muertos > 70a) | < 1931 → PD ya | **ya está en DP** |

Estos plazos son orientativos: pueden variar si la titularidad real es de personas físicas y los plazos se cuentan post mortem.

---

## 2. Versiones que **podés** redistribuir libremente

Este repo viene con 6 versiones pre-empacadas en `output/public-domain/`. Las elegimos por ser las más usadas en español, portugués e inglés cuyo texto se puede redistribuir. Cada licencia está chequeada contra la fuente correspondiente:

| Versión | Idioma | Año | Licencia | Fuente verificada |
|---|---|---|---|---|
| **Reina-Valera 1909** (`rv1909.xml`) | Español | 1909 | Dominio público (declarado por la fuente; confirmado por antigüedad — ver §1) | [ebible.org/spaRV1909](https://ebible.org/find/details.php?id=spaRV1909) · [Project Gutenberg #5881](https://www.gutenberg.org/ebooks/5881) |
| **Bíblia Livre** (`biblia-livre.xml`) | Português | 2018 | [Creative Commons Attribution 4.0 Brasil](https://creativecommons.org/licenses/by/4.0/deed.pt_BR) — permite redistribuir con atribución. Copyright © 2018 Diego Santos, Mario Sérgio, e Marco Teles. La atribución va en el bloque `<INFORMATION>` del XML; no removerla. | [ebible.org/porbr2018](https://ebible.org/find/details.php?id=porbr2018) |
| **King James Version** (`kjv.xml`, texto estándar 1769) | English | 1611 | Dominio público fuera del Reino Unido. En el Reino Unido hay [Letters Patent reales](https://en.wikipedia.org/wiki/Authorized_King_James_Version#Permission) que otorgan derechos exclusivos a Cambridge/Oxford/Collins — no aplica fuera de UK. | [ebible.org/engKJV](https://ebible.org/find/details.php?id=engKJV) |
| **American Standard Version** (`asv.xml`) | English | 1901 | Dominio público (copyright US expirado por antigüedad — anterior a 1931). Base textual de RSV, NASB y ESV. | [ebible.org/eng-asv](https://ebible.org/find/details.php?id=eng-asv) |
| **World English Bible** (`web.xml`) | English | iniciada 1994, completada 2020 | Texto dedicado explícitamente al dominio público. La marca "World English Bible" está registrada por **eBible.org** y no se puede reusar para identificar versiones modificadas; el texto en sí es libre. | [ebible.org/eng-web](https://ebible.org/find/details.php?id=eng-web) |
| **Young's Literal Translation** (`ylt.xml`) | English | 1898 | Dominio público (copyright US expirado por antigüedad). Traducción altamente literal del hebreo y griego por Robert Young. | [ebible.org/engylt](https://ebible.org/find/details.php?id=engylt) |

Para sumar otras versiones libres, primero **verificá la página de copyright de la fuente concreta** (`ebible.org/<id>/copyright.htm`) y abrí un issue con el link.

> ⚠️ **Cuidados con nombres similares:**
> - "Reina-Valera Gómez (RVG)" 2004/2010/2023 NO es dominio público — es una revisión moderna con copyright propio del Dr. Humberto Gómez Caballero y restricciones específicas.
> - Las revisiones modernas de Almeida (ARA, ARC, NAA, NTLH) tampoco son dominio público — cada una tiene copyright de SBB o SBTB. Solo Bíblia Livre (2018) es libremente redistribuible en portugués moderno.
> - La RVR1960, RVR1995, NVI, NTV, LBLA, etc. están todas bajo copyright vigente.

---

## 3. Versiones modernas (RVC, RVR1960, NVI, NTV...): qué se puede y qué no

### Política típica de las sociedades bíblicas para uso eclesial

Cada editor tiene su política propia (links verificados en Referencias). El patrón común — con un matiz importante a continuación — es:

> Se permite citar versículos en publicaciones impresas o digitales no comerciales hasta un límite, **siempre que**:
> 1. Las citas no excedan un porcentaje del total de la obra que las contiene.
> 2. **No constituyan un libro completo** de la Biblia.
> 3. Se incluya crédito visible al editor (o, en uso eclesial interno, al menos la sigla).

Los límites concretos varían:

| Editor | Versiones | Límite sin permiso | % máximo de la obra |
|---|---|---|---|
| Sociedad Bíblica Argentina (SBU) | RVR1960, RVR1995, DHH, TLA | 500 versículos | 25% (50% por libro bíblico) |
| Biblica | NVI, NIV, NIrV | 500 versículos | 25% |
| Tyndale | NTV, NLT | 500 versículos | 25% |
| Sociedade Bíblica do Brasil | ARA, ARC, NAA, NTLH | 1.100 versículos | 50% por libro |
| Lockman Foundation | LBLA, NBLA, NASB, Amplified | **1.000 versículos** | **50%** |

Para uso eclesial interno (boletines, transparencias, proyección en culto), las cuatro primeras políticas permiten omitir el aviso completo de copyright si se incluye la sigla (`(RVR1960)`, `(NVI)`, `(NTV)`, `(ACF)`) al final de cada cita.

### Cómo se aplica esto al uso en Holyrics

- ✅ **Proyectar versículos individuales en culto, citando la sigla**: cae dentro de la política de citas — el "servicio" es una obra propia que cita brevemente otra.
- ⚠️ **Que tu copia local de Holyrics contenga el texto completo** para buscar y proyectar: es una **reproducción de la obra completa** que la política de citas no cubre. En la práctica los editores casi nunca persiguen este uso eclesial — la pérdida económica es marginal y el costo reputacional alto — pero **no está formalmente autorizado** y depende de la doctrina de uso justo / fair use / fair dealing de tu jurisdicción, que es diferente en cada país.
- ⚠️ **Distribuir el archivo `.xml` o `.bib` completo a otra iglesia**: redistribución de la obra completa, fuera del marco de citas. Lo correcto es que cada iglesia genere su propio archivo en su máquina.
- ❌ **Subir el `.xml` a un repositorio público (GitHub, gist, dropbox indexado, etc.)**: infracción clara. Publicación + redistribución global + acceso indefinido + posible sustitución del producto comercial. Habilita reclamo DMCA del editor con consecuencias para tu cuenta y el repo.

### Por qué este repo NO redistribuye versiones modernas

Aunque tu uso individual probablemente esté cubierto por la política de citas en culto, publicar el archivo en GitHub significaría:

- Distribución pública y permanente, no uso interno.
- Acceso global sin filtro confesional.
- Indexación por motores de búsqueda → un usuario podría descargar la Biblia entera evitando comprar la versión digital oficial.
- Posible reclamo DMCA del editor → takedown del repositorio y de tu cuenta.

Por eso el pipeline genera estas versiones **localmente en tu máquina**, y `.gitignore` evita que se commiteen.

---

## 4. Fuentes de texto: qué se puede usar

Para alimentar el pipeline, este repo soporta una sola fuente legalmente limpia:

- **[ebible.org](https://ebible.org)** — publica explícitamente sus paquetes para redistribución bajo la licencia que cada paquete declara en su página `copyright.htm`. La mayoría son dominio público. Lo usa el adapter `scripts/fetch_ebible.py`.

**Sobre el scraping de otros sitios bíblicos** (BibleGateway, YouVersion, Bíblia Online, etc.): casi todos prohíben el acceso automatizado en sus Terms of Use. Por ejemplo los [Terms of Use de BibleGateway](https://www.biblegateway.com/legal/terms/) (vigentes al 2025-06-04, HarperCollins Christian Publishing) prohíben "automated data collection" y solo autorizan citas hasta 250 versículos o 500 palabras no comerciales — reproducir la Biblia completa excede ese límite por dos órdenes de magnitud. Por eso este repo no incluye scrapers ni adapters para esas fuentes.

Para versiones modernas que necesites en tu iglesia, considerá comprar la edición digital oficial del editor o contactarlo pidiendo licencia específica (links en Referencias).

---

## 5. Si querés publicar tu propia versión generada

Antes de subir cualquier `.xml` o `.bib` a un repositorio público:

- [ ] **¿La versión es de dominio público?** Confirmá las dos vías: (a) la fuente de la que la sacaste lo declara explícitamente en su página de copyright, y (b) por antigüedad (autores muertos hace > 70 años, o publicada antes de 1931 si te importa también EE.UU.). Si pasa las dos, es libre.
- [ ] **Si tiene copyright vigente, ¿tenés licencia escrita del editor que cubra la reproducción y redistribución en formato electrónico para uso público en internet?** Las políticas de citas estándar (500-1.000 versículos) NO cuentan — para publicar el archivo completo necesitás licencia específica firmada.
- [ ] **¿El editor liberó el texto bajo Creative Commons u otra licencia abierta?** Verificá la variante exacta. CC BY y CC0 permiten redistribución; CC BY-NC prohíbe uso comercial (y muchos proyectos abiertos cuentan como "no comercial"); CC BY-ND prohíbe derivados (incluye conversión de formato).
- [ ] **¿Removiste cualquier mención del trademark del editor del nombre del archivo y del repo?** Que la obra sea libre no significa que puedas reusar la marca para identificar tu paquete (ver §7).

Links a las políticas de los principales editores están en la sección de Referencias.

---

## 6. Atribución que incluyen los XML generados

Cada XML generado por este pipeline incluye un bloque `<INFORMATION>` con los campos `title`, `creator`, `publisher`, `date`, `identifier`, `language`, `source` y `rights`. Holyrics expone este bloque en la pantalla de información de la versión y permite al usuario consultarlo.

Reglas para mantener la integridad del campo `rights`:

- Versiones de **dominio público**: `<rights>Public Domain</rights>` (o "Dominio Público"). Esto es lo que ya se commitea para RV1909.
- Versiones con **copyright vigente** generadas localmente: el campo debe contener el aviso del editor real, p. ej. `Copyright © 2011 Sociedades Bíblicas Unidas`. Si se omite o se falsea, además del problema legal de fondo, se pierde la trazabilidad y el usuario final podría asumir incorrectamente que la versión es libre.

**No editar a mano** el bloque `<INFORMATION>` en los XML generados. Si necesitás cambiar la atribución, modificá los parámetros del builder (`--rights`, `--publisher`, etc. en `build_from_ebible.py`) y regenerá.

---

## 7. Sobre los nombres de las traducciones mencionados en este repo

Los nombres "Reina-Valera Contemporánea (RVC)", "Reina-Valera 1960 (RVR1960)",
"Nueva Versión Internacional (NVI)", "Nueva Traducción Viviente (NTV)",
"La Biblia de las Américas (LBLA)", "Almeida Corrigida Fiel (ACF)",
"Almeida Revista e Atualizada (ARA)", "King James Version (KJV)", y cualquier
otra denominación similar son **títulos y/o marcas** de sus respectivos
editores (Sociedades Bíblicas Unidas, Biblica/Vida, Tyndale, Lockman,
Sociedade Bíblica do Brasil, Sociedade Bíblica Trinitariana, etc.).

Su mención en este repositorio (README, USAGE, LEGAL, comentarios en código)
es exclusivamente con fines de **identificación referencial**, para que el
usuario pueda saber a qué traducción nos estamos refiriendo. No implica:

- Endoso, patrocinio, ni asociación de esos editores con este proyecto.
- Que este proyecto sea una versión oficial de esas traducciones.
- Autorización para redistribuir su texto (que sigue protegido — ver
  secciones 1 a 5 arriba).

Este uso encuadra en lo que la doctrina conoce como **nominative fair use**
(EE.UU.) / **uso referencial** (UE, Latinoamérica): se utiliza el nombre
mínimo necesario para identificar la obra, sin gráficas, logos ni elementos
distintivos del editor, y sin sugerir conexión.

Si sos titular de derechos sobre alguno de estos nombres y considerás que
algún uso particular excede lo referencial, abrí un issue en GitHub y lo
ajustamos.

## Referencias

Todas las URLs de esta sección están verificadas al 2026-05-21. Si encontrás un link roto, abrí un issue.

### Tratados internacionales y legislación

- **[Convenio de Berna para la Protección de las Obras Literarias y Artísticas](https://www.wipo.int/treaties/es/ip/berne/)** (WIPO, texto en español) — Base del régimen internacional de copyright. Artículos relevantes citados en la sección 1: Art. 2(3) (traducciones como obras protegidas), Art. 5(1) (protección automática sin registro), Art. 7(1) (plazo mínimo de vida + 50 años).
- **[Ley 11.723 — Régimen Legal de la Propiedad Intelectual (Argentina)](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm)** (InfoLEG, texto vigente) — Art. 5: el copyright dura la vida del autor más **70 años** después del 1° de enero del año siguiente a su muerte. Para obras en colaboración, el plazo corre desde la muerte del último colaborador. Es el plazo aplicable en Argentina y similar en la UE y EE.UU. para obras pos-1978.
- **[Copyright Term and the Public Domain in the United States](https://copyright.cornell.edu/publicdomain)** (Cornell University Library, chart de Peter B. Hirtle, autoridad clásica) — Tabla canónica para determinar si una obra está en dominio público en EE.UU. Regla actual: **toda obra publicada antes de 1931** está en el dominio público estadounidense al 1° de enero de 2026 (el cutoff avanza un año cada 1° de enero). Mirror espejo siempre disponible: [Wikimedia Commons](https://commons.wikimedia.org/wiki/Commons:Hirtle_chart).

### Políticas de las sociedades bíblicas y editores (origen del 90% de las traducciones modernas)

- **[Sociedad Bíblica Argentina — Política sobre derechos y permisos](https://sba.org.ar/politica-sobre-derechos-y-permisos-de-uso-de-los-textos-biblicos/)** — Límite de 500 versículos sin permiso por escrito, sin exceder el 25% de la obra ni el 50% de un libro bíblico completo. Cubre RVR1960, RVR1995, DHH, TLA. Para citas en boletines, transparencias y similares no comerciales, basta con la sigla al final de cada cita.
- **[Sociedade Bíblica do Brasil — Acordo de Licença de Usuário Final](https://www.sbb.org.br/acordo-de-licenca-de-usuario-final-eula)** — Política similar a la de la SBA, aplica a ARA, ARC, NAA, NTLH. Contacto para permisos extendidos: `direitos@sbb.org.br`.
- **[Biblica — Permissions](https://www.biblica.com/permissions/)** (NVI / NIV / NIrV) — Límite de 500 versículos sin permiso escrito, sin exceder el 25% del total ni un libro bíblico completo. Para iglesias en uso no comercial (boletines, transparencias) basta la sigla "NVI®"/"NIV®".
- **[Tyndale — Permissions](https://www.tyndale.com/permissions)** (NTV / NLT) — Límite de 500 versículos en cualquier medio impreso o digital, mismo 25%/libro completo que las otras. Crédito requerido en obras vendibles.
- **[Lockman Foundation — Permission to Quote (NASB, NBLA, LBLA, Amplified)](https://www.lockman.org/permission-to-quote-copyright-trademark-information/)** — Límite más amplio: hasta 1.000 versículos sin permiso escrito, sin exceder el 50%. Versión en español: [Permiso para citar](https://www.lockman.org/espanol/permiso-para-citar/).

### Fuentes y políticas técnicas de los proveedores que usa este repo

- **[eBible.org — Intellectual Property Policy](https://ebible.org/legal.php)** — Política general: las obras de dominio público se pueden copiar libremente, las protegidas requieren permiso del titular; eBible publica cada paquete con su licencia específica en la página de detalle del paquete (`ebible.org/<id>/copyright.htm`). Lo usamos como fuente para versiones libres.
- **[eBible.org — Bibles in the Public Domain](https://ebible.org/publicdomain.htm)** — Lista oficial de paquetes que eBible considera dominio público, con la salvedad de que los nombres pueden estar registrados como marcas y que el KJV tiene restricciones en el Reino Unido (Letters Patent).
- **[BibleGateway — Terms of Use](https://www.biblegateway.com/legal/terms/)** (última versión: 2025-06-04, operado por HarperCollins Christian Publishing) — Sección relevante: prohibición de "automated data collection" / scraping y de uso comercial sin permiso. Permiso de cita hasta 250 versículos o 500 palabras no comerciales. Por eso este repo no incluye adapter para BibleGateway (ver §4).

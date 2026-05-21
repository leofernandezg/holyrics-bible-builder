# Marco legal — leia antes de usar

[🇪🇸 Español](LEGAL.md) · [🇬🇧 English](LEGAL.en.md) · **🇵🇹 Português (você está aqui)**

> **Disclaimer:** este documento é uma análise informativa, **não é aconselhamento jurídico**.
> Se você tem dúvidas sobre um caso particular, consulte um advogado ou diretamente
> o detentor dos direitos autorais da versão que deseja usar.

## TL;DR

| O que este repo faz | É legal? |
|---|---|
| Publicar o código (builder, validators, adapter ebible.org) | ✅ Sim (MIT) |
| Empacotar versões de **domínio público** (RV1909, KJV, WEB, etc.) | ✅ Sim — o texto é livre |
| Gerar **localmente** uma versão moderna (RVC, NVI, RVR1960...) e usá-la na sua igreja | ⚠️ Reprodução não autorizada da obra completa: as políticas de citação (500-1.000 versículos conforme a editora) cobrem a projeção de versículos individuais, mas NÃO cobrem manter uma cópia digital completa. As editoras raramente perseguem esses usos em igrejas, mas formalmente não está autorizado |
| **Redistribuir** publicamente uma versão moderna em qualquer formato | ❌ **Não** — violação de direitos autorais |

Este repo foi desenhado para que seja **impossível** cair acidentalmente no caso vermelho: o `.gitignore` exclui explicitamente `sources/*-cache/`, `output/rvc.xml`, `output/rvr1960.xml`, etc. O repo distribui apenas um adapter para [ebible.org](https://ebible.org), que publica seus textos para redistribuição sob licença explícita.

---

## 1. Por que existem versões bíblicas com direitos autorais?

Muita gente assume que "a Bíblia é de domínio público". Isso é verdadeiro do **texto fonte** (hebraico, aramaico, grego — tudo escrito há mais de 2.000 anos), mas **não das traduções modernas**.

Cada tradução para o português/inglês/espanhol/etc. é uma **obra derivada** criada por tradutores, editores e revisores contemporâneos. Sob a [Convenção de Berna](https://www.wipo.int/treaties/es/ip/berne/) (em vigor em praticamente todos os países), uma tradução é uma obra criativa nova com seus próprios direitos autorais. A autoria é do tradutor (ou equipe de tradutores); a titularidade dos direitos patrimoniais depende do contrato sob o qual a tradução foi feita e do regime trabalhista aplicável (no Brasil, [Lei 9.610/98 art. 17](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm); nos EUA, [17 USC §201(b)](https://www.law.cornell.edu/uscode/text/17/201) "work made for hire"). Na prática, quase todas as traduções bíblicas modernas são publicadas com titularidade da sociedade bíblica ou editora que as encomendou.

As disposições da Convenção de Berna que sustentam isso:

1. **Art. 2(3)** — "As traduções, adaptações, arranjos musicais e outras transformações de uma obra literária ou artística serão protegidos como obras originais, sem prejuízo dos direitos do autor da obra original." Aplicado aqui: ainda que o texto bíblico original (hebraico/grego) esteja em domínio público por antiguidade, uma tradução moderna do séc. XX ou XXI tem seu próprio direito autoral autônomo.
2. **Art. 5(2)** — "O gozo e o exercício desses direitos não estarão subordinados a nenhuma formalidade." Aplicado aqui: não existe uma "Bíblia sem direitos autorais" por descuido — se a editora não liberou o texto explicitamente e o prazo não expirou, está protegido por padrão em qualquer jurisdição signatária, sem necessidade de registro nem símbolo ©.
3. **Art. 7(1)** — o prazo **mínimo** de proteção é a vida do autor mais 50 anos. Quase todos os signatários elevaram esse prazo (veja abaixo). Aplicado aqui: as traduções do séc. XIX ou anteriores (Sagradas Escrituras 1569, Reina-Valera Antigua 1602, RV1909) estão em domínio público; as modernas (RVC 2011, RVR1960, NVI 1999) permanecem protegidas durante todo o séc. XXI.

### Prazo dos direitos autorais — por jurisdição

O prazo depende de quem é titular e de qual país se aplica:

- **Brasil** ([Lei 9.610/98 art. 41](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)): vida do autor mais **70 anos** a partir de 1º de janeiro do ano seguinte ao da sua morte. Para obras em coautoria, a partir da morte do último coautor. Para obras anônimas ou pseudônimas, **70 anos contados de 1º de janeiro do ano imediatamente posterior ao da primeira publicação**.
- **Argentina, UE, maior parte da América Latina** (Berna + extensões nacionais): vida do autor mais **70 anos** (similar ao Brasil).
- **EUA** (pós-1978): para obras "work made for hire" ou anônimas/pseudônimas, **95 anos a partir da publicação** ou **120 anos a partir da criação**, o que ocorrer primeiro (17 USC §302(c)). Para obras pré-1978, as regras variam conforme renovação; o cutoff atual (em 1º de janeiro de 2026) é: **toda obra publicada antes de 1931 está em domínio público nos EUA** ([Cornell/Hirtle chart](https://copyright.cornell.edu/publicdomain)).

Estimativa de prazos para as traduções mais comuns:

| Versão | Ano pub. | Brasil/UE (≈70 desde pub.) | EUA (95 desde pub.) | DP a partir de |
|---|---|---|---|---|
| RVC | 2011 | 2081 | 2106 | o último que se aplicar |
| RVR1960 | 1960 | 2030 | 2055 | 2055 |
| NVI (port.) | 2001 | 2071 | 2096 | 2096 |
| ARA | 1993 | 2063 | 2088 | 2088 |
| ACF | 1995 | 2065 | 2090 | 2090 |
| RV1909 | 1909 | (autores mortos > 70a) | < 1931 → já DP | **já em DP** |

Esses prazos são orientativos: podem variar se a titularidade real for de pessoas físicas e o prazo correr post mortem.

---

## 2. Versões que **você pode** redistribuir livremente

Este repo vem com 6 versões pré-empacotadas em `output/public-domain/`. Foram escolhidas como as mais usadas em espanhol, português e inglês cujo texto pode ser redistribuído. Cada licença é verificada contra a fonte correspondente:

| Versão | Idioma | Ano | Licença | Fonte verificada |
|---|---|---|---|---|
| **Reina-Valera 1909** (`rv1909.xml`) | Espanhol | 1909 | Domínio público (declarado pela fonte; confirmado pela antiguidade — veja §1) | [ebible.org/spaRV1909](https://ebible.org/find/details.php?id=spaRV1909) · [Project Gutenberg #5881](https://www.gutenberg.org/ebooks/5881) |
| **Bíblia Livre** (`biblia-livre.xml`) | Português | 2018 | [Creative Commons Attribution 4.0 Brasil](https://creativecommons.org/licenses/by/4.0/deed.pt_BR) — permite redistribuição com atribuição. Copyright © 2018 Diego Santos, Mario Sérgio, e Marco Teles. A atribuição vai no bloco `<INFORMATION>` do XML; não remova. | [ebible.org/porbr2018](https://ebible.org/find/details.php?id=porbr2018) |
| **King James Version** (`kjv.xml`, texto padrão 1769) | Inglês | 1611 | Domínio público fora do Reino Unido. No Reino Unido há [Letters Patent reais](https://en.wikipedia.org/wiki/Authorized_King_James_Version#Permission) que conferem direitos exclusivos a Cambridge/Oxford/Collins — não se aplica fora do UK. | [ebible.org/engKJV](https://ebible.org/find/details.php?id=engKJV) |
| **American Standard Version** (`asv.xml`) | Inglês | 1901 | Domínio público (direitos US expirados por antiguidade — anterior a 1931). Base textual de RSV, NASB e ESV. | [ebible.org/eng-asv](https://ebible.org/find/details.php?id=eng-asv) |
| **World English Bible** (`web.xml`) | Inglês | iniciada 1994, concluída 2020 | Texto dedicado explicitamente ao domínio público. A marca "World English Bible" está registrada por **eBible.org** e não pode ser reusada para identificar versões modificadas; o texto em si é livre de direitos. | [ebible.org/eng-web](https://ebible.org/find/details.php?id=eng-web) |
| **Young's Literal Translation** (`ylt.xml`) | Inglês | 1898 | Domínio público (direitos US expirados por antiguidade). Tradução altamente literal do hebraico e do grego por Robert Young. | [ebible.org/engylt](https://ebible.org/find/details.php?id=engylt) |

Para somar outras versões livres, primeiro **verifique a página de copyright da fonte concreta** (`ebible.org/<id>/copyright.htm`) e abra uma issue com o link.

> ⚠️ **Cuidado com nomes similares:**
> - "Reina-Valera Gómez (RVG)" 2004/2010/2023 NÃO é domínio público — é uma revisão moderna com direitos autorais próprios do Dr. Humberto Gómez Caballero e restrições específicas.
> - As revisões modernas de Almeida (ARA, ARC, NAA, NTLH) também não são domínio público — cada uma tem direitos autorais da SBB ou SBTB. Só a Bíblia Livre (2018) é livremente redistribuível em português moderno.
> - A RVR1960, RVR1995, NVI, NTV, LBLA, etc. estão todas sob direitos autorais vigentes.

---

## 3. Versões modernas (RVC, RVR1960, NVI, NTV, ACF, ARA...): o que se pode e o que não

### Política típica das sociedades bíblicas para uso eclesial

Cada editora tem sua política própria (links verificados em Referências). O padrão comum — com uma nuance importante a seguir — é:

> Permite-se citar versículos em publicações impressas ou digitais não comerciais até um limite, **desde que**:
> 1. As citações não excedam uma porcentagem do total da obra que as contém.
> 2. **Não constituam um livro completo** da Bíblia.
> 3. Inclua-se crédito visível à editora (ou, em uso eclesial interno, ao menos a sigla).

Os limites concretos variam:

| Editora | Versões | Limite sem permissão | % máximo da obra |
|---|---|---|---|
| Sociedad Bíblica Argentina (SBU) | RVR1960, RVR1995, DHH, TLA | 500 versículos | 25% (50% por livro bíblico) |
| Biblica | NVI, NIV, NIrV | 500 versículos | 25% |
| Tyndale | NTV, NLT | 500 versículos | 25% |
| Sociedade Bíblica do Brasil | ARA, ARC, NAA, NTLH | 1.100 versículos | 50% por livro |
| Lockman Foundation | LBLA, NBLA, NASB, Amplified | **1.000 versículos** | **50%** |

Para uso eclesial interno (boletins, transparências, projeção em culto), as quatro primeiras políticas permitem omitir o aviso completo de direitos se a sigla for incluída (`(RVR1960)`, `(NVI)`, `(NTV)`, `(ACF)`) ao final de cada citação.

### Como isto se aplica ao uso no Holyrics

- ✅ **Projetar versículos individuais no culto, citando a sigla**: cai dentro da política de citações — o "culto" é uma obra própria que cita brevemente outra.
- ⚠️ **Que sua cópia local do Holyrics contenha o texto completo** para buscar e projetar: é uma **reprodução da obra completa** que a política de citações não cobre. Na prática, as editoras quase nunca perseguem esse uso eclesial — a perda econômica é marginal e o custo reputacional alto — mas **não está formalmente autorizado** e depende da doutrina de uso justo / fair use / fair dealing da sua jurisdição, que é diferente em cada país.
- ⚠️ **Distribuir o arquivo `.xml` ou `.bib` completo para outra igreja**: redistribuição da obra completa, fora do marco de citações. O correto é que cada igreja gere seu próprio arquivo na sua máquina.
- ❌ **Subir o `.xml` a um repositório público (GitHub, gist, dropbox indexado, etc.)**: violação clara. Publicação + redistribuição global + acesso indefinido + possível substituição do produto comercial. Habilita reclamação DMCA da editora com consequências para sua conta e o repo.

### Por que este repo NÃO redistribui versões modernas

Embora seu uso individual provavelmente esteja coberto pela política de citações em culto, publicar o arquivo no GitHub significaria:

- Distribuição pública e permanente, não uso interno.
- Acesso global sem filtro confessional.
- Indexação por mecanismos de busca → um usuário poderia baixar a Bíblia inteira evitando comprar a versão digital oficial.
- Possível reclamação DMCA da editora → takedown do repositório e da sua conta.

Por isso o pipeline gera essas versões **localmente na sua máquina**, e o `.gitignore` evita que sejam commitadas.

---

## 4. Fontes de texto: o que se pode usar

Para alimentar o pipeline, este repo suporta uma única fonte legalmente limpa:

- **[ebible.org](https://ebible.org)** — publica explicitamente seus pacotes para redistribuição sob a licença que cada pacote declara em sua página `copyright.htm`. A maioria é domínio público. Usado pelo adapter `scripts/fetch_ebible.py`.

**Sobre o scraping de outros sites bíblicos** (BibleGateway, YouVersion, Bíblia Online, etc.): quase todos proíbem o acesso automatizado em seus Terms of Use. Por exemplo, os [Terms of Use do BibleGateway](https://www.biblegateway.com/legal/terms/) (vigentes em 2025-06-04, HarperCollins Christian Publishing) proíbem "automated data collection" e só autorizam citações até 250 versículos ou 500 palavras não comerciais — reproduzir a Bíblia inteira excede esse limite por duas ordens de grandeza. Por isso este repo não inclui scrapers nem adapters para essas fontes.

Para versões modernas que você precise na sua igreja, considere comprar a edição digital oficial da editora ou contatá-la pedindo licença específica (links em Referências).

---

## 5. Se você quiser publicar sua própria versão gerada

Antes de subir qualquer `.xml` ou `.bib` a um repositório público:

- [ ] **A versão é de domínio público?** Confirme as duas vias: (a) a fonte da qual você a obteve declara explicitamente em sua página de copyright, e (b) por antiguidade (autores mortos há > 70 anos, ou publicada antes de 1931 se você também se importar com os EUA). Se passar nas duas, é livre.
- [ ] **Se tem direitos autorais vigentes, você tem licença escrita da editora que cubra a reprodução e redistribuição em formato eletrônico para uso público na internet?** As políticas de citação padrão (500-1.000 versículos) NÃO contam — para publicar o arquivo completo você precisa de licença específica assinada.
- [ ] **A editora liberou o texto sob Creative Commons ou outra licença aberta?** Verifique a variante exata. CC BY e CC0 permitem redistribuição; CC BY-NC proíbe uso comercial (e muitos projetos abertos contam como "comerciais"); CC BY-ND proíbe derivados (inclui conversão de formato).
- [ ] **Você removeu qualquer menção do trademark da editora do nome do arquivo e do repo?** Que a obra seja livre não significa que você possa reusar a marca para identificar seu pacote (veja §7).

Links para as políticas das principais editoras estão na seção de Referências.

---

## 6. Atribuição que os XML gerados incluem

Cada XML gerado por este pipeline inclui um bloco `<INFORMATION>` com os campos `title`, `creator`, `publisher`, `date`, `identifier`, `language`, `source` e `rights`. O Holyrics expõe esse bloco na tela de informação da versão e permite ao usuário consultá-lo.

Regras para manter a integridade do campo `rights`:

- Versões de **domínio público**: `<rights>Public Domain</rights>` (ou "Domínio Público"). Isso é o que já é commitado para a RV1909.
- Versões com **direitos vigentes** geradas localmente: o campo deve conter o aviso da editora real, p. ex. `Copyright © 2011 Sociedades Bíblicas Unidas`. Se for omitido ou falsificado, além do problema legal de fundo, perde-se a rastreabilidade e o usuário final poderia assumir incorretamente que a versão é livre.

**Não editar à mão** o bloco `<INFORMATION>` nos XMLs gerados. Se precisar mudar a atribuição, modifique os parâmetros do builder (`--rights`, `--publisher`, etc. em `build_from_ebible.py`) e regere.

---

## 7. Sobre os nomes das traduções mencionados neste repo

Os nomes "Reina-Valera Contemporánea (RVC)", "Reina-Valera 1960 (RVR1960)",
"Nueva Versión Internacional (NVI)", "Nueva Traducción Viviente (NTV)",
"La Biblia de las Américas (LBLA)", "Almeida Corrigida Fiel (ACF)",
"Almeida Revista e Atualizada (ARA)", "King James Version (KJV)" e qualquer
outra denominação similar são **títulos e/ou marcas** de suas respectivas
editoras (Sociedades Bíblicas Unidas, Biblica/Vida, Tyndale, Lockman,
Sociedade Bíblica do Brasil, Sociedade Bíblica Trinitariana, etc.).

Sua menção neste repositório (README, USAGE, LEGAL, comentários no código)
é exclusivamente para fins de **identificação referencial**, para que o
usuário possa saber a qual tradução estamos nos referindo. Não implica:

- Endosso, patrocínio, nem associação dessas editoras com este projeto.
- Que este projeto seja uma versão oficial dessas traduções.
- Autorização para redistribuir seu texto (que segue protegido — veja
  seções 1 a 5 acima).

Este uso se encaixa no que a doutrina conhece como **nominative fair use**
(EUA) / **uso referencial** (UE, América Latina): utiliza-se o nome
mínimo necessário para identificar a obra, sem gráficos, logotipos nem
elementos distintivos da editora, e sem sugerir conexão.

Se você é titular de direitos sobre algum desses nomes e considera que
algum uso particular excede o referencial, abra uma issue no GitHub e
ajustaremos.

## Referências

Todas as URLs desta seção estão verificadas em 2026-05-21. Se encontrar um link quebrado, abra uma issue.

### Tratados internacionais e legislação

- **[Convenção de Berna para a Proteção das Obras Literárias e Artísticas](https://www.wipo.int/treaties/es/ip/berne/)** (WIPO) — Base do regime internacional de direitos autorais. Artigos relevantes citados na seção 1: Art. 2(3) (traduções como obras protegidas), Art. 5(2) (proteção automática sem formalidade), Art. 7(1) (prazo mínimo de vida + 50 anos).
- **[Lei 9.610/98 — Lei de Direitos Autorais (Brasil)](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)** (Planalto) — Art. 41: o direito autoral dura a vida do autor mais **70 anos** contados de 1º de janeiro do ano seguinte ao da sua morte. Para obras em coautoria, do último coautor.
- **[Lei 11.723 — Regime Legal da Propriedade Intelectual (Argentina)](https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm)** (InfoLEG, texto vigente, espanhol) — Art. 5: prazo similar ao brasileiro (70 anos pma).
- **[Copyright Term and the Public Domain in the United States](https://copyright.cornell.edu/publicdomain)** (Cornell University Library, chart de Peter B. Hirtle, autoridade clássica) — Tabela canônica para determinar se uma obra está em domínio público nos EUA. Regra atual: **toda obra publicada antes de 1931** está no domínio público estadunidense em 1º de janeiro de 2026 (o cutoff avança um ano a cada 1º de janeiro). Espelho sempre disponível: [Wikimedia Commons](https://commons.wikimedia.org/wiki/Commons:Hirtle_chart).

### Políticas das sociedades bíblicas e editoras (origem de 90% das traduções modernas)

- **[Sociedade Bíblica do Brasil — Acordo de Licença de Usuário Final](https://www.sbb.org.br/acordo-de-licenca-de-usuario-final-eula)** — Aplica-se a ARA, ARC, NAA, NTLH. Limite de 1.100 versículos sem permissão, sem exceder 50% de um livro bíblico. Contato para permissões estendidas: `direitos@sbb.org.br`.
- **[Sociedad Bíblica Argentina — Política sobre direitos e permissões](https://sba.org.ar/politica-sobre-derechos-y-permisos-de-uso-de-los-textos-biblicos/)** — Limite de 500 versículos sem permissão por escrito, sem exceder 25% da obra nem 50% de um livro bíblico completo. Cobre RVR1960, RVR1995, DHH, TLA.
- **[Biblica — Permissions](https://www.biblica.com/permissions/)** (NVI / NIV / NIrV) — Limite de 500 versículos sem permissão escrita, sem exceder 25% do total nem um livro bíblico completo. Para igrejas em uso não comercial (boletins, transparências) basta a sigla "NVI®"/"NIV®".
- **[Tyndale — Permissions](https://www.tyndale.com/permissions)** (NTV / NLT) — Limite de 500 versículos em qualquer meio impresso ou digital, mesmos 25%/livro completo das outras. Crédito requerido em obras vendáveis.
- **[Lockman Foundation — Permission to Quote (NASB, NBLA, LBLA, Amplified)](https://www.lockman.org/permission-to-quote-copyright-trademark-information/)** — Limite mais amplo: até 1.000 versículos sem permissão escrita, sem exceder 50%. Versão em espanhol: [Permiso para citar](https://www.lockman.org/espanol/permiso-para-citar/).

### Fontes e políticas técnicas dos provedores que este repo usa

- **[eBible.org — Intellectual Property Policy](https://ebible.org/legal.php)** — Política geral: as obras de domínio público podem ser copiadas livremente, as protegidas requerem permissão do titular; o eBible publica cada pacote com sua licença específica na página de detalhe do pacote (`ebible.org/<id>/copyright.htm`). Usamos como fonte para versões livres.
- **[eBible.org — Bibles in the Public Domain](https://ebible.org/publicdomain.htm)** — Lista oficial de pacotes que o eBible considera domínio público, com a ressalva de que os nomes podem estar registrados como marcas e que o KJV tem restrições no Reino Unido (Letters Patent).
- **[BibleGateway — Terms of Use](https://www.biblegateway.com/legal/terms/)** (última versão: 2025-06-04, operado por HarperCollins Christian Publishing) — Seção relevante: proibição de "automated data collection" / scraping e de uso comercial sem permissão. Permissão de citação até 250 versículos ou 500 palavras não comerciais. Por isso este repo não inclui adapter para BibleGateway (veja §4).

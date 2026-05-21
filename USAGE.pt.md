# Guia de uso — holyrics-bible-builder

[🇪🇸 Español](USAGE.md) · [🇬🇧 English](USAGE.en.md) · **🇵🇹 Português (você está aqui)**

Este guia foi escrito para que **qualquer pessoa** — mesmo sem experiência
prévia com terminal — possa usar as versões incluídas ou gerar as que precisar.

Se você só quer baixar a **Reina-Valera 1909** e importar no Holyrics, vá
direto ao **[Caso 1](#caso-1-quero-usar-uma-versão-já-incluída-rv1909)**.

---

## Índice

- [Antes de começar](#antes-de-começar)
- [Caso 1: Quero usar uma versão já incluída (RV1909)](#caso-1-quero-usar-uma-versão-já-incluída-rv1909)
- [Caso 2: Quero gerar outra versão (avançado)](#caso-2-quero-gerar-outra-versão-avançado)
  - [Gerar outra versão](#gerar-outra-versão)
  - [Lista de versões disponíveis](#lista-de-versões-disponíveis-no-eblibleorg)
  - [Verificar que o texto seja idêntico ao original](#verificar-que-o-texto-seja-idêntico-ao-original)
- [Caso 3: Quero a ACF, ARC, NAA ou outra versão moderna](#caso-3-quero-a-acf-arc-naa-ou-outra-versão-moderna)
- [Solução de problemas](#solução-de-problemas)
- [Glossário](#glossário)

---

## Antes de começar

Você precisa ter instalado:

- **Holyrics** no seu Mac ou PC (baixe em <https://www.holyrics.com.br/>).
- Para os Casos 2 e 3 (gerar versões novas): **Python 3.10+** (no Mac já vem
  pré-instalado; no Windows baixe em <https://www.python.org/downloads/>).

Você não precisa saber programar para o Caso 1. Para os outros, é só copiar
e colar comandos.

---

## Caso 1: Quero usar uma versão já incluída (RV1909)

A **Reina-Valera 1909** já está gerada, validada e pronta para importar.

### Passo 1: Baixar o arquivo

1. Acesse a página do repositório:
   <https://github.com/leofernandezg/holyrics-bible-builder>
2. Abra a pasta `output/public-domain/`.
3. Clique no arquivo `rv1909.xml`.
4. Na página do arquivo, clique no botão **"Download raw file"**
   (ícone de download, no canto superior direito do visualizador).
5. Salve no Desktop ou onde for conveniente.

### Passo 2: Importar no Holyrics

1. Abra o **Holyrics**.
2. No canto superior direito, clique no ícone de **⚙ engrenagem**.
3. Acesse **"Configurações"** (ou **"Settings"** se estiver em inglês).
4. No painel esquerdo, encontre **"Bíblias"** e clique nela.
5. Clique no botão **"Importar"** ou **"Adicionar versão da Bíblia"**.
6. Selecione o arquivo `rv1909.xml` que você baixou.
7. O Holyrics vai processá-lo (10-30 segundos).
8. Quando terminar, você verá **"Reina-Valera 1909"** na lista de versões disponíveis.

### Passo 3: Testar

1. Na tela principal do Holyrics, encontre a seção **"Bíblia"**.
2. Mude a versão selecionada para **"Reina-Valera 1909"**.
3. Procure, por exemplo, **João 3:16** — você deve ver:
   > Porque de tal manera amó Dios al mundo, que ha dado á su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.

✅ Pronto! Você já pode projetar versículos em RV1909.

### Se você precisa instalar em várias máquinas (ex. o PC da igreja)

- **Opção A:** repetir o Passo 1 + Passo 2 em cada máquina.
- **Opção B:** depois de importar em uma máquina, copie o arquivo `.bib`
  que o Holyrics gerou (fica em
  `~/Holyrics/Holyrics/files/Bible LG/` no Mac, ou
  `C:\Holyrics\Holyrics\files\Bible LG\` no Windows) para a mesma pasta na
  outra máquina.

---

## Caso 2: Quero gerar outra versão (avançado)

Funciona para versões disponíveis no [ebible.org](https://ebible.org/). Você
precisa ter Python instalado.

### Passo 1: Preparar o projeto (só na primeira vez)

Abra o **Terminal** (Mac: ⌘+Espaço, digite "Terminal"; Windows: "PowerShell"
ou "cmd").

Copie e cole estes comandos, um por linha:

```bash
# 1. Baixar o código (precisa do git instalado; se não, baixe o ZIP do GitHub)
git clone https://github.com/leofernandezg/holyrics-bible-builder.git
cd holyrics-bible-builder

# 2. Criar um ambiente virtual isolado
python3 -m venv .venv

# 3. Instalar as dependências
.venv/bin/pip install lxml beautifulsoup4 requests
```

Se pedir para instalar o `pip` ou der algum erro, abra uma issue no GitHub
e nós ajudamos.

### Gerar outra versão

Cada versão no ebible.org tem um **ID** curto. Por exemplo:

- Reina-Valera 1909 → `spaRV1909`
- King James Version → `engKJV`
- World English Bible → `eng-web`

Para gerar, rode este comando substituindo os valores entre aspas pelos da
sua versão:

```bash
.venv/bin/python scripts/build_from_ebible.py spaRV1909 \
    --title "Reina-Valera 1909" \
    --identifier RV1909 \
    --date 1909 \
    --rights "Public Domain" \
    --out output/public-domain/rv1909.xml
```

Ao terminar, você terá o arquivo `.xml` pronto para importar no Holyrics
(siga o Passo 2 do Caso 1).

### Lista de versões disponíveis no eBible.org

Estas são as versões que o pipeline já suporta (todas redistribuíveis):

| Versão | ID no ebible | Idioma | Licença | Comando |
|---|---|---|---|---|
| Reina-Valera 1909 | `spaRV1909` | Espanhol (`spa`) | Domínio público | (veja acima) |
| Bíblia Livre | `porbr2018` | Português (`por`) | CC BY 4.0 BR | requer atribuição |
| King James Version | `engKJV` | Inglês (`eng`) | Domínio público (fora do UK) | usar `--slug eng-kjv2006` |
| American Standard Version | `eng-asv` | Inglês (`eng`) | Domínio público | — |
| World English Bible | `eng-web` | Inglês (`eng`) | Domínio público dedicado | — |
| Young's Literal Translation | `engylt` | Inglês (`eng`) | Domínio público | — |
| Darby Translation | `engdby` | Inglês (`eng`) | Domínio público | — |

Busca completa do ebible: <https://ebible.org/find/>. **Sempre verifique a licença exata** em `ebible.org/<ID>/copyright.htm` antes de redistribuir o `.xml` gerado.

> ⚠️ Alguns pacotes do ebible.org têm um "slug" de download diferente do `id` da página (por exemplo o KJV: id `engKJV`, slug `eng-kjv2006`). Se o download falhar com 404, veja a URL do USFX zip na página de detalhe e passe-a via `--slug`.

### Verificar que o texto seja idêntico ao original

O pipeline inclui três níveis de testes. Rode os três depois de gerar:

```bash
# 1. Validação estrutural básica (1 s)
.venv/bin/python scripts/validate_xml.py output/public-domain/rv1909.xml

# 2. Testes de forma exaustivos: codificação, cânon, numeração, sem markup
#    residual, sem caracteres de controle, spot-checks de versículos-chave (~2 s)
.venv/bin/python scripts/test_structure.py output/public-domain/rv1909.xml

# 3. Fidelidade caractere por caractere contra o USFX do ebible.org (~10 s)
.venv/bin/python scripts/test_fidelity_usfx.py spaRV1909 output/public-domain/rv1909.xml
```

Se os três passarem, o `.xml` é bit-exact reproduzível — qualquer terceiro
que repita o pipeline obtém o mesmo hash.

Para gerar também um hash SHA-256 para comparar entre máquinas:

```bash
shasum -a 256 output/public-domain/rv1909.xml > output/public-domain/rv1909.xml.sha256
```

---

## Caso 3: Quero a ACF, ARC, NAA ou outra versão moderna

⚠️ **Antes de continuar, leia [LEGAL.md](LEGAL.md).** Versões modernas
(ACF, ARC, NAA, NVI, NTLH, etc.) têm **direitos autorais** da editora que
as publicou. A política de citações (500-1.100 versículos conforme a
editora) cobre a projeção de versículos individuais no culto, mas **não
cobre manter uma cópia digital completa** nem redistribuir o arquivo. Na
prática as editoras raramente perseguem o uso eclesial interno, mas
formalmente não está autorizado e depende da doutrina de fair use / uso
justo da sua jurisdição. Veja [LEGAL.md §3](LEGAL.md) para a análise completa.

Este repositório **não inclui ferramentas** para baixar versões com
direitos autorais de sites que não as publicam explicitamente (BibleGateway,
YouVersion, etc.) — seus termos de serviço proíbem acesso automatizado e,
mesmo se fosse tecnicamente possível, redistribuir o arquivo resultante
seria infração de direitos autorais (veja [LEGAL.md §4](LEGAL.md)).

### O caminho correto

- Compre a versão digital oficial da editora (quando disponível).
- Ou entre em contato com a editora pedindo licença específica para projetar
  no Holyrics:
  - **Sociedade Bíblica do Brasil** (ARA, ARC, NAA, NTLH): <https://www.sbb.org.br/acordo-de-licenca-de-usuario-final-eula> — pedidos: `direitos@sbb.org.br`
  - **Biblica** (NVI): <https://www.biblica.com/permissions/>
  - **Tyndale** (NLT): <https://www.tyndale.com/permissions>

---

## Solução de problemas

### "tag not found: XMLBIBLE" ao importar no Holyrics

O Holyrics só aceita o formato **Zefania XML** (root `<XMLBIBLE>`). Se você
baixou um `.xml` que não é deste projeto, pode estar em outro formato
(Beblia, OSIS, USFM) que o Holyrics rejeita. Verifique se o arquivo começa
com:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XMLBIBLE biblename="...">
```

### O Holyrics trava ao importar

Tente fechar e reabrir o Holyrics. Se persistir, veja o tamanho do arquivo
— um `.xml` de Bíblia completa pesa entre 4 e 7 MB. Se for muito menor,
está incompleto.

### "command not found: python3"

No Windows você precisa usar `py` ou `python` (sem o 3). No Mac, instale
o Python em <https://www.python.org/downloads/>.

### O comando `git clone` não funciona

Instale o git em <https://git-scm.com/downloads>. Ou baixe o repositório
como ZIP pelo botão verde **"Code → Download ZIP"** no GitHub.

### Quero verificar que o arquivo não foi modificado

Cada versão incluída vem com um arquivo `.sha256` ao lado. Para comparar:

```bash
# Mac/Linux
shasum -a 256 output/public-domain/rv1909.xml
# Deve coincidir com o que diz rv1909.xml.sha256

# Windows PowerShell
Get-FileHash output\public-domain\rv1909.xml -Algorithm SHA256
```

---

## Glossário

- **Zefania XML**: formato padrão para Bíblias digitais que o Holyrics
  importa. Estrutura: `<XMLBIBLE><BIBLEBOOK><CHAPTER><VERS>`.
- **USFX**: formato XML usado internamente pelo ebible.org. Não é importável
  diretamente pelo Holyrics; este projeto converte para Zefania.
- **`.bib`**: formato binário interno do Holyrics. Gerado automaticamente
  ao importar o `.xml`. Não edite à mão.
- **Domínio público**: obra cujo direito autoral expirou (ou nunca teve).
  Qualquer um pode usar, copiar e redistribuir.
- **Cânon de 66 livros**: 39 do Antigo Testamento + 27 do Novo, sem
  deuterocanônicos. Padrão nas igrejas protestantes.

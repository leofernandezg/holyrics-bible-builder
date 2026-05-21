# holyrics-bible-builder

[🇪🇸 Español](README.md) · [🇬🇧 English](README.en.md) · **🇵🇹 Português (você está aqui)**

Uma ferramenta gratuita para **importar Bíblias para o [Holyrics](https://www.holyrics.com.br/)**
no formato Zefania XML, e para **verificar que o texto gerado seja idêntico
ao original**, caractere por caractere.

Pensada para igrejas que querem projetar versículos nos cultos e não encontram
a versão que precisam nos repositórios habituais da comunidade.

---

## Para que serve?

O Holyrics precisa de um arquivo `.xml` (formato Zefania) para adicionar uma
nova versão da Bíblia. As versões tradicionais como Almeida Revista e
Atualizada já vêm prontas em muitos sites da comunidade, mas **outras versões
(como a Reina-Valera Contemporánea em espanhol) não existem empacotadas em
lugar nenhum**.

Este projeto:

1. **Entrega arquivos `.xml` prontos para importar** em `output/public-domain/`.
2. **Permite gerar outras versões** disponíveis em fontes legais e abertas
   (como o [ebible.org](https://ebible.org)).
3. **Valida automaticamente** que o texto gerado seja idêntico ao original
   — caractere por caractere, nos 31.000+ versículos.

## Versões incluídas

As 6 versões mais usadas em espanhol, português e inglês cuja licença permite redistribuição:

| Versão | Idioma | Ano | Licença | Baixar |
|---|---|---|---|---|
| Reina-Valera 1909 | Espanhol | 1909 | Domínio público | [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml) |
| Bíblia Livre | Português | 2018 | CC BY 4.0 Brasil | [`output/public-domain/biblia-livre.xml`](output/public-domain/biblia-livre.xml) |
| King James Version (1769) | Inglês | 1611 | Domínio público (fora do Reino Unido) | [`output/public-domain/kjv.xml`](output/public-domain/kjv.xml) |
| American Standard Version | Inglês | 1901 | Domínio público | [`output/public-domain/asv.xml`](output/public-domain/asv.xml) |
| World English Bible | Inglês | 2020 | Domínio público (dedicado) | [`output/public-domain/web.xml`](output/public-domain/web.xml) |
| Young's Literal Translation | Inglês | 1898 | Domínio público | [`output/public-domain/ylt.xml`](output/public-domain/ylt.xml) |

Todas validadas estruturalmente e **caractere por caractere contra a fonte original em [ebible.org](https://ebible.org)**. Veja [LEGAL.pt.md](LEGAL.pt.md) para detalhes de cada licença.

> ⚠️ Versões modernas como **RVC, RVR1960, NVI, ARC, NAA, ACF** têm direitos
> autorais e **não estão incluídas aqui**. Se você quer gerá-las para uso
> interno da sua igreja, existe um caminho documentado em [USAGE.pt.md](USAGE.pt.md),
> mas **leia [LEGAL.pt.md](LEGAL.pt.md) primeiro** para entender as implicações.

## Quero importar a RV1909 no Holyrics (rápido)

1. Baixe o arquivo [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml).
2. Abra o Holyrics → **"Ir para a Bíblia"** → menu **"Versão"** → **"Importar"** → **"Zefania XML"**.
3. Escolha o `rv1909.xml` e clique em **Ok** no diálogo de importação. Pronto — a versão fica disponível no dropdown de versões.

Travou? O guia passo-a-passo (para quem não é técnico) está em
**[USAGE.pt.md](USAGE.pt.md)**.

## Quero gerar outra versão

Se a versão que você procura estiver disponível no [ebible.org](https://ebible.org/),
ela se gera com um único comando. Veja
**[USAGE.pt.md → "Gerar outra versão"](USAGE.pt.md#gerar-outra-versão)**.

## Documentação

- **[USAGE.pt.md](USAGE.pt.md)** — Guia passo-a-passo de instalação e uso,
  feito para gente não técnica.
- **[LEGAL.pt.md](LEGAL.pt.md)** — Análise de direitos autorais: quais versões
  podem ser redistribuídas e quais não. **Leitura obrigatória** antes de
  publicar qualquer coisa.
- **[LICENSE](LICENSE)** — MIT (apenas para o código; os textos bíblicos têm
  licença própria).

## Quer contribuir?

PRs bem-vindas para:

- Adicionar adaptadores de outras fontes livres (Crosswire SWORD, Open Scriptures, etc.)
- Pré-empacotar mais versões de domínio público
- Melhorar a tradução desta documentação

Issues bem-vindas para reportar erros no texto gerado, problemas ao importar
no Holyrics, ou sugestões.

## Créditos

- Código: [Leonardo Fernández García](https://github.com/leofernandezg), licença MIT.
- Textos em domínio público: tradutores originais (Reina y Valera, 1909, etc.).
- Hospedagem de fontes livres: [eBible.org](https://ebible.org).

# holyrics-bible-builder

**🇪🇸 Español (estás acá)** · [🇬🇧 English](README.en.md) · [🇵🇹 Português](README.pt.md)

Una herramienta gratuita para **importar Biblias en [Holyrics](https://www.holyrics.com.br/)**
en formato Zefania XML, y para **verificar que el texto sea idéntico al
original**, palabra por palabra.

Pensada para iglesias que quieren proyectar versículos en sus servicios y no
encuentran la versión que necesitan en los repositorios habituales.

---

## ¿Para qué sirve?

Holyrics necesita un archivo `.xml` (formato Zefania) para agregar una versión
nueva de la Biblia. Las versiones tradicionales como Reina-Valera 1960 o NVI
ya vienen pre-armadas en muchos sitios de la comunidad, pero **otras versiones
(como la Reina-Valera Contemporánea) no existen empacadas en ningún lado**.

Este proyecto:

1. **Te da archivos `.xml` listos para importar** en Holyrics (en `output/public-domain/`).
2. **Te permite generar otras versiones** que estén disponibles en fuentes legales
   y abiertas (como [ebible.org](https://ebible.org)).
3. **Valida automáticamente** que el texto generado sea idéntico al original
   (carácter por carácter, los 31.000+ versículos).

## Versiones incluidas

Las 6 versiones de uso más extendido en español, portugués e inglés cuya licencia permite redistribución:

| Versión | Idioma | Año | Licencia | Descargar |
|---|---|---|---|---|
| Reina-Valera 1909 | Español | 1909 | Dominio público | [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml) |
| Bíblia Livre | Português | 2018 | CC BY 4.0 Brasil | [`output/public-domain/biblia-livre.xml`](output/public-domain/biblia-livre.xml) |
| King James Version (1769) | English | 1611 | Dominio público (fuera del Reino Unido) | [`output/public-domain/kjv.xml`](output/public-domain/kjv.xml) |
| American Standard Version | English | 1901 | Dominio público | [`output/public-domain/asv.xml`](output/public-domain/asv.xml) |
| World English Bible | English | 2020 | Dominio público (dedicado) | [`output/public-domain/web.xml`](output/public-domain/web.xml) |
| Young's Literal Translation | English | 1898 | Dominio público | [`output/public-domain/ylt.xml`](output/public-domain/ylt.xml) |

Todas validadas estructuralmente y **carácter por carácter contra la fuente original en [ebible.org](https://ebible.org)**. Ver [LEGAL.md](LEGAL.md) para los detalles de cada licencia.

> ⚠️ Las versiones modernas como **RVC, RVR1960, NVI, NTV, LBLA** tienen
> copyright y **no se incluyen acá**. Si querés generarlas para uso interno
> de tu iglesia, hay un camino documentado en [USAGE.md](USAGE.md), pero
> **leé primero [LEGAL.md](LEGAL.md)** para entender las implicancias.

## Quiero importar la RV1909 en Holyrics (rápido)

1. Descargá el archivo [`output/public-domain/rv1909.xml`](output/public-domain/rv1909.xml).
2. Abrí Holyrics → ⚙ (engranaje) → **Settings** → **Bibles** → **Import**.
3. Elegí el archivo `rv1909.xml`. Listo.

¿Te complicaste? La guía paso a paso (con instrucciones para gente que no es
técnica) está en **[USAGE.md](USAGE.md)**.

## Quiero generar otra versión

Si la versión que buscás está disponible en [ebible.org](https://ebible.org/),
se genera con un solo comando. Ver **[USAGE.md → "Generar otra versión"](USAGE.md#generar-otra-versión)**.

## Documentación

- **[USAGE.md](USAGE.md)** — Guía paso a paso para instalar y usar, pensada para
  gente no técnica.
- **[LEGAL.md](LEGAL.md)** — Análisis de copyright: qué versiones se pueden
  redistribuir y cuáles no. **Lectura obligatoria** antes de publicar nada.
- **[LICENSE](LICENSE)** — MIT (solo para el código; los textos bíblicos tienen
  su propia licencia).

## ¿Querés contribuir?

PRs bienvenidas para:

- Agregar adapters de otras fuentes libres (Crosswire SWORD, Open Scriptures, etc.)
- Pre-empaquetar más versiones de dominio público
- Mejorar la traducción de esta documentación

Issues bienvenidos para reportar errores en el texto generado, problemas al
importar en Holyrics, o sugerencias.

## Créditos

- Código: [Leonardo Fernández García](https://github.com/leofernandezg), licencia MIT.
- Textos en dominio público: traductores originales (Reina y Valera, 1909, etc.).
- Hosting de fuentes libres: [eBible.org](https://ebible.org).

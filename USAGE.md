# Guía de uso — holyrics-bible-builder

**🇪🇸 Español (estás acá)** · [🇬🇧 English](USAGE.en.md) · [🇵🇹 Português](USAGE.pt.md)

Esta guía está pensada para que **cualquier persona** — aunque nunca haya usado
una terminal — pueda usar las versiones incluidas o generar las que necesite.

Si solo querés bajar la **Reina-Valera 1909** e importarla en Holyrics, andá
directo a **[Caso 1](#caso-1-quiero-usar-una-versión-ya-incluida-rv1909)**.

---

## Índice

- [Antes de empezar](#antes-de-empezar)
- [Caso 1: Quiero usar una versión ya incluida (RV1909)](#caso-1-quiero-usar-una-versión-ya-incluida-rv1909)
- [Caso 2: Quiero generar otra versión (avanzado)](#caso-2-quiero-generar-otra-versión-avanzado)
  - [Generar otra versión](#generar-otra-versión)
  - [Lista de versiones disponibles](#lista-de-versiones-disponibles-en-eblibleorg)
  - [Verificar que el texto sea idéntico al original](#verificar-que-el-texto-sea-idéntico-al-original)
- [Caso 3: Quiero la RVC u otra versión moderna](#caso-3-quiero-la-rvc-u-otra-versión-moderna)
- [Solución de problemas](#solución-de-problemas)
- [Glosario](#glosario)

---

## Antes de empezar

Necesitás tener instalado:

- **Holyrics** en tu Mac o PC (descargar en <https://www.holyrics.com.br/>).
- Para los Casos 2 y 3 (generar versiones nuevas): **Python 3.10+** (en Mac
  ya viene; en Windows descargar de <https://www.python.org/downloads/>).

No necesitás conocimientos de programación para el Caso 1. Para los demás,
es solo copiar y pegar comandos.

---

## Caso 1: Quiero usar una versión ya incluida (RV1909)

La **Reina-Valera 1909** ya está generada, validada y lista para importar.

### Paso 1: Descargar el archivo

1. Andá a la página del repositorio:
   <https://github.com/leofernandezg/holyrics-bible-builder>
2. Abrí la carpeta `output/public-domain/`.
3. Hacé clic en el archivo `rv1909.xml`.
4. En la página del archivo, hacé clic en el botón **"Download raw file"**
   (ícono de bajada, arriba a la derecha del visor del archivo).
5. Guardalo en tu Escritorio o donde te quede cómodo.

### Paso 2: Importar en Holyrics

1. Abrí **Holyrics**.
2. En la pantalla principal, hacé clic en **"Ir a la Biblia"** (o **"Ir a Holyrics"** según la versión).
3. En la barra superior, hacé clic en el menú **"Versión"**.
4. Andá a **"Importar"** → **"Zefania XML"**.
5. Buscá y seleccioná el archivo `rv1909.xml` que descargaste.
6. Se abre un diálogo **"Importar - Biblia"** con los campos ID, Nombre, Idioma y Descripción ya completados (Holyrics los lee del bloque `<INFORMATION>` del XML). Hacé clic en **"Ok"**.
7. Holyrics procesa el archivo (10-30 segundos).
8. Cuando termina, la versión queda disponible en el dropdown de versiones, agrupada por idioma.

### Paso 3: Probarlo

1. En la vista de Biblia, hacé clic en la **flechita del dropdown de versión** (arriba a la izquierda, al lado de la versión actual).
2. Bajo la sección **"Español"** seleccioná **"Reina-Valera 1909"**.
3. Buscá, por ejemplo, **Juan 3:16** — debería aparecer:
   > Porque de tal manera amó Dios al mundo, que ha dado á su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.

✅ ¡Listo! Ya podés proyectar versículos en RV1909.

### Si tenés que instalarlo en varias máquinas (ej. la PC de la iglesia)

- **Opción A:** repetir el Paso 1 + Paso 2 en cada máquina.
- **Opción B:** después de importar en una máquina, copiar el archivo `.bib`
  que Holyrics generó (vive en
  `~/Holyrics/Holyrics/files/Bible LG/` en Mac, o
  `C:\Holyrics\Holyrics\files\Bible LG\` en Windows) a la misma carpeta en la otra máquina.

---

## Caso 2: Quiero generar otra versión (avanzado)

Sirve para versiones disponibles en [ebible.org](https://ebible.org/). Necesitás
tener Python instalado.

### Paso 1: Preparar el proyecto (solo la primera vez)

Abrí la **Terminal** (en Mac: ⌘+Espacio, escribí "Terminal"; en Windows:
"PowerShell" o "cmd").

Copiá y pegá estos comandos, uno por línea:

```bash
# 1. Bajar el código (necesitás git instalado; sino, descargá el ZIP desde GitHub)
git clone https://github.com/leofernandezg/holyrics-bible-builder.git
cd holyrics-bible-builder

# 2. Crear un entorno virtual aislado
python3 -m venv .venv

# 3. Instalar las dependencias
.venv/bin/pip install lxml beautifulsoup4 requests
```

Si te pide instalar `pip` o te tira algún error, abrí un issue en GitHub y te
ayudamos.

### Generar otra versión

Cada versión en ebible.org tiene un **ID** corto. Por ejemplo:

- Reina-Valera 1909 → `spaRV1909`
- King James Version → `engKJV`
- World English Bible → `eng-web`

Para generar, corré este comando reemplazando los valores entre comillas por
los de tu versión:

```bash
.venv/bin/python scripts/build_from_ebible.py spaRV1909 \
    --title "Reina-Valera 1909" \
    --identifier RV1909 \
    --date 1909 \
    --rights "Public Domain" \
    --out output/public-domain/rv1909.xml
```

Al terminar, vas a tener el archivo `.xml` listo para importar en Holyrics
(seguí el Paso 2 del Caso 1).

### Lista de versiones disponibles en eBible.org

Estas son las versiones que el pipeline ya soporta (todas redistribuibles):

| Versión | ID en ebible | Idioma | Licencia | Comando |
|---|---|---|---|---|
| Reina-Valera 1909 | `spaRV1909` | Español (`spa`) | Dominio público | (ver arriba) |
| Bíblia Livre | `porbr2018` | Português (`por`) | CC BY 4.0 BR | requiere atribución |
| King James Version | `engKJV` | English (`eng`) | Dominio público (fuera de UK) | usar `--slug eng-kjv2006` |
| American Standard Version | `eng-asv` | English (`eng`) | Dominio público | — |
| World English Bible | `eng-web` | English (`eng`) | Dominio público dedicado | — |
| Young's Literal Translation | `engylt` | English (`eng`) | Dominio público | — |
| Darby Translation | `engdby` | English (`eng`) | Dominio público | — |

Buscador completo de ebible: <https://ebible.org/find/>. **Verificá siempre la licencia exacta** en `ebible.org/<ID>/copyright.htm` antes de redistribuir el `.xml` que generes.

> ⚠️ Algunos paquetes en ebible.org tienen un "slug" de descarga que no coincide con el `id` de la página de detalle (por ejemplo el KJV: id `engKJV`, slug `eng-kjv2006`). Si el download falla con 404, fijate en la URL del USFX zip en la página de detalle y pasalo con `--slug`.

### Verificar que el texto sea idéntico al original

El pipeline incluye tres niveles de tests. Corré los tres después de generar:

```bash
# 1. Validación estructural básica (1 s)
.venv/bin/python scripts/validate_xml.py output/public-domain/rv1909.xml

# 2. Tests de forma exhaustivos: encoding, canon, numeración, sin markup
#    residual, sin caracteres de control, spot-checks de versos clave (~2 s)
.venv/bin/python scripts/test_structure.py output/public-domain/rv1909.xml

# 3. Fidelidad char-por-char contra el USFX de ebible.org (~10 s)
.venv/bin/python scripts/test_fidelity_usfx.py spaRV1909 output/public-domain/rv1909.xml
```

Si los tres pasan, el `.xml` es bit-exact reproducible — cualquier tercero
que repita el pipeline obtiene el mismo hash.

Si querés además generar un hash SHA-256 para comparar antes/después de
copiar entre máquinas:

```bash
shasum -a 256 output/public-domain/rv1909.xml > output/public-domain/rv1909.xml.sha256
```

---

## Caso 3: Quiero la RVC, RVR1960 u otra versión moderna

⚠️ **Antes de seguir, leé [LEGAL.md](LEGAL.md).** Las versiones modernas
(RVC, RVR1960, NVI, NTV, LBLA, ACF, NAA, etc.) tienen **copyright** del
editor que las publicó. La política de citas (500-1.000 versículos según el
editor) cubre la proyección de versos individuales en el culto, pero **no
cubre tener una copia digital completa** ni redistribuir el archivo. En la
práctica los editores no suelen perseguir el uso eclesial interno, pero
formalmente no está autorizado y depende de la doctrina de fair use de tu
jurisdicción. Ver [LEGAL.md §3](LEGAL.md) para el análisis completo.

Este repo **no incluye herramientas** para descargar versiones con copyright
desde sitios que no las publican explícitamente (BibleGateway, YouVersion,
etc.) — sus términos de servicio prohíben el acceso automatizado y, aunque
fuera técnicamente posible, redistribuir el archivo resultante sería
infracción de copyright (ver [LEGAL.md §4](LEGAL.md)).

### El camino correcto

- Comprá la versión digital oficial del editor (cuando esté disponible).
- O contactá al editor pidiendo licencia específica para proyectarla en Holyrics:
  - **Sociedad Bíblica Argentina** (RVR1960, RVR1995, DHH, TLA): <https://sba.org.ar/politica-sobre-derechos-y-permisos-de-uso-de-los-textos-biblicos/>
  - **Biblica** (NVI / NIV): <https://www.biblica.com/permissions/>
  - **Tyndale** (NTV / NLT): <https://www.tyndale.com/permissions>
  - **Lockman Foundation** (LBLA / NBLA / NASB): <https://www.lockman.org/permission-to-quote-copyright-trademark-information/> (versión en español: <https://www.lockman.org/espanol/permiso-para-citar/>)

---

## Solución de problemas

### "tag not found: XMLBIBLE" cuando importo en Holyrics

Holyrics solo acepta el formato **Zefania XML** (root `<XMLBIBLE>`). Si bajaste
un `.xml` que no es de este proyecto, puede estar en otro formato (Beblia,
OSIS, USFM) y Holyrics lo rechaza. Verificá que el archivo empiece con:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XMLBIBLE biblename="...">
```

### Holyrics se queda colgado al importar

Probá cerrar y reabrir Holyrics. Si persiste, fijate el tamaño del archivo
— un `.xml` de Biblia completa pesa entre 4 y 7 MB. Si es mucho más chico,
está incompleto.

### Cuando corro un comando dice "command not found: python3"

En Windows tenés que usar `py` o `python` (sin el 3). En Mac, instalá Python
desde <https://www.python.org/downloads/>.

### El comando `git clone` no funciona

Instalá git desde <https://git-scm.com/downloads>. O bajá el repo como ZIP
desde el botón verde **"Code → Download ZIP"** en GitHub.

### Quiero verificar que el archivo no se modificó

Cada versión incluida viene con un archivo `.sha256` al lado. Para comparar:

```bash
# Mac/Linux
shasum -a 256 output/public-domain/rv1909.xml
# Tiene que coincidir con lo que dice rv1909.xml.sha256

# Windows PowerShell
Get-FileHash output\public-domain\rv1909.xml -Algorithm SHA256
```

---

## Glosario

- **Zefania XML**: formato estándar para Biblias digitales que Holyrics
  importa. Estructura `<XMLBIBLE><BIBLEBOOK><CHAPTER><VERS>`.
- **USFX**: formato XML que usa ebible.org internamente. No lo importa
  Holyrics directamente; este proyecto lo convierte a Zefania.
- **`.bib`**: formato binario interno de Holyrics. Lo genera Holyrics al
  importar el `.xml`. No lo edites a mano.
- **Dominio público**: obra cuyo copyright expiró o nunca tuvo. Cualquiera
  puede usarla, copiarla y redistribuirla.
- **Canon de 66 libros**: 39 del Antiguo Testamento + 27 del Nuevo, sin
  deuterocanónicos. Es lo que usan las iglesias protestantes.

# Pipeline de Captura de Conocimiento → Kindle

> Diseñado: 2026-03-06
> Stack: OpenClaw + n8n self-hosted + Pandoc + Kindle email

---

## Vision general

Un sistema unificado que convierte cualquier fuente de contenido en un documento EPUB enviado al Kindle. El usuario solo manda un link (o video) por WhatsApp/Telegram — el sistema hace el resto.

```
Usuario (WhatsApp/Telegram)
    ↓
OpenClaw (recibe, clasifica, orquesta)
    ↓
Procesamiento segun tipo de fuente
    ↓
Generacion EPUB (Pandoc via n8n)
    ↓
Kindle (email a @kindle.com)
```

---

## Rol de cada herramienta

| Herramienta | Rol | Cuando se necesita |
|------------|-----|-------------------|
| **OpenClaw** | Interfaz con usuario, browser automation, decisiones inteligentes, investigacion profunda | Siempre (es el punto de entrada) |
| **n8n** | Orquestacion de pasos, llamadas a APIs, generacion EPUB, envio a Kindle | Procesamiento estructurado y confiable |
| **Pandoc** | Conversion de markdown/HTML a EPUB | Siempre (generacion del archivo) |
| **Whisper** | Transcripcion de audio/video | Videos sin transcripcion disponible |
| **Claude API** | Resumen, analisis, investigacion | Cuando se requiere procesamiento inteligente |

---

## Flujos por tipo de fuente

---

### Flujo 1: Video de Instagram

> ✅ **Probado exitosamente** (2026-03-13): `yt-dlp` descarga audio de reels públicos sin sesión. Whisper `small` transcribe en español con buena calidad. No se necesitó browser con sesión para contenido público.

**Problema:** Instagram no tiene API publica. Requiere login para contenido privado.

```
Usuario envia link de Instagram a OpenClaw (WhatsApp)
    ↓
OpenClaw: identifica fuente como Instagram
    ↓
OpenClaw: abre browser (sesion autenticada con Instagram)
    ↓
OpenClaw: descarga video o extrae audio via browser automation
    ↓
OpenClaw: envia audio a Whisper → transcripcion
    ↓
OpenClaw: envia transcripcion a Claude → resumen + investigacion rapida
    ↓
OpenClaw: dispara workflow n8n con el contenido procesado
    ↓
n8n: formatea en markdown → Pandoc → EPUB
    ↓
n8n: envia EPUB a email Kindle
    ↓
OpenClaw: confirma al usuario por WhatsApp
```

**Por que OpenClaw hace el browser:** Instagram bloquea scraping externo. El browser de OpenClaw ya tiene la sesion abierta.

---

### Flujo 2: Podcast largo en YouTube

**Problema:** NotebookLM no tiene API. La extension de Chrome es la unica forma de alimentarlo.

**Opcion A — Directo (sin NotebookLM):**
```
Usuario envia URL de YouTube a OpenClaw
    ↓
OpenClaw: skill youtube-transcript → transcripcion completa con timestamps
    ↓
OpenClaw: envia a Claude → genera documento de estudio estructurado
    ↓
OpenClaw: dispara workflow n8n
    ↓
n8n: markdown → Pandoc → EPUB → Kindle
```

**Opcion B — Con NotebookLM (notas mas ricas):**
```
Usuario envia URL de YouTube a OpenClaw (indica "con NotebookLM")
    ↓
OpenClaw: abre browser → navega a notebooklm.google.com
    ↓
OpenClaw: crea nuevo notebook → agrega URL de YouTube como fuente
    ↓
OpenClaw: espera procesamiento de NotebookLM
    ↓
OpenClaw: solicita "Briefing Document" o "Study Guide"
    ↓
OpenClaw: copia el contenido generado
    ↓
OpenClaw: dispara workflow n8n con el documento
    ↓
n8n: markdown → Pandoc → EPUB → Kindle
```

**Recomendacion:** Opcion A para agilidad, Opcion B cuando el contenido merece notas mas profundas.

---

### Flujo 3: Articulo web

**Problema:** Ninguno — es el flujo mas simple.

```
Usuario envia URL a OpenClaw
    ↓
OpenClaw: skill web-scraper → extrae contenido limpio (sin ads, sin nav)
    ↓
OpenClaw: dispara workflow n8n con el contenido
    ↓
n8n: markdown → Pandoc → EPUB → Kindle
```

**Variante con enriquecimiento:**
```
...mismo inicio...
    ↓
OpenClaw: Claude analiza el articulo → genera resumen + contexto adicional
    ↓
n8n: documento enriquecido → EPUB → Kindle
```

**Nota:** Este flujo podria vivir completamente en n8n si el usuario lo dispara manualmente. OpenClaw agrega valor cuando la entrada es conversacional.

---

### Flujo 4: Articulo de LinkedIn

**Problema:** LinkedIn requiere login. Ademas, el contenido suele merecer investigacion mas profunda.

```
Usuario envia URL de LinkedIn a OpenClaw (WhatsApp)
    ↓
OpenClaw: abre browser (sesion autenticada con LinkedIn)
    ↓
OpenClaw: extrae contenido completo del articulo via browser automation
    ↓
OpenClaw: Claude resume el articulo + identifica temas clave
    ↓
OpenClaw: lanza agente de investigacion profunda
    → busca informacion adicional sobre los temas
    → encuentra fuentes relacionadas
    → sintetiza hallazgos
    ↓
OpenClaw: consolida articulo original + investigacion en documento unico
    ↓
OpenClaw: dispara workflow n8n
    ↓
n8n: documento consolidado → Pandoc → EPUB → Kindle
    ↓
OpenClaw: notifica al usuario con resumen de 2-3 lineas
```

---

## Configuracion de Kindle

Amazon permite recibir documentos en el Kindle via email:
- Cada Kindle tiene una direccion `@kindle.com`
- Se configura en: Amazon Account → Manage Content → Preferences → Personal Document Settings
- n8n envia el EPUB como adjunto a esa direccion

---

## Infraestructura recomendada

```
Digital Ocean Droplet (4GB RAM, 2 vCPU)
├── OpenClaw (Docker)
│   ├── Canal: WhatsApp o Telegram
│   └── Skills: youtube-transcript, web-scraper, notebooklm, n8n
├── n8n (Docker)
│   └── Workflows por tipo de fuente
└── Pandoc (instalado en el sistema)
```

---

## Entrada: iOS Share Sheet via Shortcut

El mecanismo de entrada preferido es un **iOS Shortcut** instalado desde iCloud (mismo patrón que CalmDigest).

```
Share Sheet (iPhone) → Shortcut → POST webhook n8n → clasificación → flujo correspondiente
```

- El Shortcut toma la URL compartida y hace un HTTP POST al webhook de n8n en el Droplet
- OpenClaw solo interviene cuando se necesita browser automation (Instagram, LinkedIn)
- Referencia: inspeccionar el Shortcut de CalmDigest en app Shortcuts para ver la llamada HTTP exacta y replicarla apuntando a n8n

**Pendiente:** Daniel va a compartir el archivo/captura del Shortcut de CalmDigest para extraer la plantilla HTTP.

---

## Tareas pendientes

### Infraestructura base
- [ ] Montar Droplet en Digital Ocean (4GB RAM, 2 vCPU)
- [ ] Instalar OpenClaw via Docker
- [ ] Configurar canal de entrada: **Telegram** (preferido sobre WhatsApp para automatización)
- [ ] Instalar n8n via Docker
- [ ] Instalar skills en OpenClaw: youtube-transcript, web-scraper, notebooklm, n8n

### Email para envío al Kindle
- [ ] Crear cuenta Gmail dedicada para el pipeline (cuenta de Claude/automatizaciones)
- [ ] Activar verificación en dos pasos en esa cuenta
- [ ] Generar App Password en `myaccount.google.com/apppasswords` (nombre: `kindle-pipeline`)
- [ ] Configurar dirección @kindle.com en Amazon: Account → Manage Content → Preferences → Personal Document Settings
- [ ] Implementar script de envío (Python smtplib o msmtp)

### Workflow n8n
- [ ] Crear workflow n8n: markdown → Pandoc → EPUB → Kindle email

### Integración Claude API
- [ ] Integrar Claude API dentro de OpenClaw como motor de investigación y enriquecimiento
- [ ] Usar protocolo definido en `CLAUDE-enriquecimiento.md` como prompt base

### Pruebas por flujo (en orden recomendado)
- [ ] Probar flujo 3 (artículo web) — MVP más simple
- [ ] Probar flujo 2A (YouTube directo con transcripción)
- [ ] Probar flujo 1 (Instagram público) — ✅ transcripción local ya validada con yt-dlp + Whisper
- [ ] Probar flujo 4 (LinkedIn con browser + investigación profunda)
- [ ] Probar flujo 2B (YouTube + NotebookLM)

# OpenClaw — Contexto de Referencia

> Investigado: 2026-03-06

---

## ¿Qué es?

OpenClaw es un agente de IA personal, **open-source y self-hosted**. Pasó de unos pocos miles a +60,000 estrellas en GitHub en 72 horas a inicios de 2026. Es el proyecto de referencia para agentes personales autónomos.

- Repo oficial: https://github.com/openclaw/openclaw
- Sitio: https://openclaw.ai
- Tagline: "Your own personal AI assistant. Any OS. Any Platform. The lobster way."

---

## Capacidades core

### 1. Acceso al sistema
- Lectura y escritura de archivos
- Ejecución de comandos shell
- Control de procesos

### 2. Browser Automation (via Chrome DevTools Protocol - CDP)
- Navega cualquier URL como humano
- Extrae contenido de páginas con JS dinámico
- Llena formularios, hace clic, toma screenshots
- Maneja sesiones autenticadas (usa las credenciales del browser local)
- Credenciales nunca salen del computador

### 3. Canales de entrada (inbox multi-canal)
WhatsApp, Telegram, Slack, Discord, iMessage, Signal, Microsoft Teams, Matrix, LINE, Twitch, y más.

### 4. Skills (extensiones modulares)
- Registro público (ClawHub): +13,700 skills a febrero 2026
- Skills son componibles — se encadenan en pipelines
- Se instalan automáticamente cuando el agente los necesita

---

## Skills relevantes para pipeline de captura

| Skill | Función |
| --- | --- |
| `youtube-transcript` | Extrae transcripción completa de videos YouTube con timestamps |
| `youtube-summarizer` | Transcript + resumen estructurado en un paso |
| `video-transcript-downloader` | Descarga transcripciones de múltiples plataformas |
| `web-scraper` | Extracción inteligente de contenido web, boilerplate removal, metadata |
| `xpr-web-scraping` | Scraping avanzado con fallback multi-estrategia |
| `notebooklm` | Integración con Google NotebookLM via browser automation |
| `openclaw-skill-n8n` | Trigger y gestión de workflows n8n desde OpenClaw |

---

## Integración con n8n

OpenClaw y n8n se complementan:

- **OpenClaw** = cerebro + manos (intent, browser auth, decisiones)
- **n8n** = línea de ensamblaje (procesamiento confiable, APIs, transformaciones)

El skill `openclaw-skill-n8n` permite a OpenClaw disparar workflows de n8n como acción. Documentación: https://n8nlab.io/blog/openclaw-n8n-integration-guide

---

## Proyectos relacionados

| Proyecto | Descripción |
| --- | --- |
| **Nanobot** (HKUDS) | Versión ultra-ligera, ~4,000 líneas de código |
| **ClawWork** (HKUDS) | OpenClaw como "AI coworker" económico, gana dinero en tareas reales |
| **awesome-openclaw-skills** | +5,400 skills curados y categorizados |
| **awesome-openclaw-usecases** | Casos de uso de la comunidad |

---

## Setup recomendado para self-hosting

- VPS: Digital Ocean Droplet **4GB RAM / 2 vCPU / 80GB SSD (\~$24/mes)** — arrancar aquí, escalar a 8GB si hace falta
- OS: Ubuntu 24.04 LTS
- Instalar via Docker
- Configurar canal de entrada (WhatsApp o Telegram recomendado)
- Instalar skills según necesidad
- Documentación DigitalOcean: https://www.digitalocean.com/resources/articles/what-is-openclaw

---

## LLM local: Ollama + Qwen3.5

Para tareas simples (resúmenes, formateo, decisiones) sin consumir créditos de API externa.

### Modelo recomendado: `qwen3.5:2b`

| Modelo | RAM en uso | Disco | ¿Cabe en 4GB? |
| --- | --- | --- | --- |
| qwen3.5:0.8b | ~1.5 GB | ~500 MB | Sí, holgado |
| **qwen3.5:2b** | ~2.5–3 GB | ~1.5 GB | **Sí — recomendado** |
| qwen3.5:4b | ~5–6 GB | ~2.7 GB | No (OOM) |
| qwen3.5:9b | >8 GB | ~6.6 GB | No |

**Velocidad sin GPU:** 3–7 tokens/seg en 2 vCPU. Aceptable para pipelines asíncronos.

### Instalación

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:2b
```

### Exponer API para n8n y OpenClaw

```bash
# Editar servicio
sudo systemctl edit ollama.service
# Agregar:
# [Service]
# Environment="OLLAMA_HOST=0.0.0.0:11434"

sudo systemctl daemon-reload && sudo systemctl restart ollama
sudo ufw allow from <IP-CONFIABLE> to any port 11434
```

- API compatible con OpenAI: `http://<IP>:11434/v1/chat/completions`
- n8n tiene nodo nativo para Ollama (Base URL: `http://<IP>:11434`)
- **Seguridad:** restringir acceso por IP, no exponer públicamente sin auth

### Si 2B queda corto en calidad

Alternativas que caben en 4GB: `phi4-mini` (~2.3 GB), `gemma3:1b` (~1.2 GB).
Para usar `qwen3.5:4b` se necesitan 8GB RAM ($48/mes).

---

## Pendiente — Instalación OpenClaw en VPS

```bash
# 1. Instalar dependencias
apt-get update && apt-get install -y git nodejs npm

# 2. Clonar repo
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# 3. Correr setup con imagen oficial
export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
./docker-setup.sh
```

Dashboard quedará en: `http://167.71.86.102:18789`

---

## Comandos esenciales del VPS

### Droplet (SSH)

```bash
# Entrar
ssh root@167.71.86.102

# Salir (regresa a tu Mac, el droplet sigue corriendo)
exit
```

### Docker

```bash
# Ver contenedores corriendo
docker ps

# Entrar a un contenedor
docker exec -it <nombre-o-id> bash

# Salir sin detenerlo
Ctrl+P, luego Ctrl+Q

# Salir y detenerlo
exit

# Detener un contenedor
docker stop <nombre-o-id>

# Reiniciar un contenedor
docker restart <nombre-o-id>
```

---

### Credenciales Google OAuth2 (Gmail)

> ⚠️ Sensible — no subir a GitHub

- Client ID: `830231443665-gjifi6pvsqjjhlsli4asoe5l2qcpp2r1.apps.googleusercontent.com`
- Client Secret: `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`
- Redirect URI: pendiente — actualizar al nuevo dominio en Google Cloud Console

---

### Estado (2026-03-26)

🔴 **Reset completo.** El dominio `agrackcartasfreight.work` fue eliminado (los nameservers nunca propagaron). El túnel `n8n` (`e02d6586-1a0d-4abc-b049-d4446a66ba7b`) también fue eliminado. Se evalúa usar un droplet diferente al actual (`167.71.86.102`).

**Próximos pasos:**
- Adquirir nuevo dominio (cuenta personal, separada del trabajo)
- Crear nuevo droplet (si aplica)
- Crear nueva cuenta n8n
- Crear nuevo túnel Cloudflare
- Documentar aquí cuando esté listo

---

## Notas importantes

- El browser automation usa el Chrome local — las sesiones ya autenticadas (LinkedIn, Instagram, Google) están disponibles para el agente
- No requiere APIs de terceros para sitios con login si el browser ya tiene sesión activa
- Ideal para sitios sin API pública: LinkedIn, Instagram, NotebookLM

---

## Alternativa a evaluar: OpenFang

> Investigado: 2026-03-08 — Muy nuevo, revisar en 3-4 meses

- Repo: https://github.com/RightNow-AI/openfang
- Sitio: https://openfang.sh
- Lanzado: 24 febrero 2026 (~12 días al momento de investigar)
- ~12,400 stars en GitHub

### Diferencia filosófica con OpenClaw

OpenFang no es un chatbot evolucionado — es un **Agent OS**: daemons autónomos que corren 24/7 sin intervención del usuario. OpenClaw es chat-driven (tú mandas el link, él responde). OpenFang actúa solo y te reporta.

### Ventajas técnicas

- Construido en **Rust** — binario único de ~32MB, arranca en 180ms (vs 6s de OpenClaw)
- 16 capas de seguridad (WASM sandbox, audit trail, taint tracking, etc.)
- 171 modelos de 37 proveedores, 140+ endpoints REST/WS/SSE
- Compatible con API de OpenAI

### "Hands" relevantes para pipeline de captura

| Hand | Función |
| --- | --- |
| **Collector** | OSINT e inteligencia competitiva con knowledge graphs automáticos |
| **Researcher** | Investigación y productividad autónoma |
| **Browser** | Automatización web |
| **Clip** | Video shorts, captions, publicación automática |

### Por qué no usarlo todavía (marzo 2026)

- v0.1.x — demasiado temprano, APIs pueden cambiar
- Issue abierto (#137): Ollama no funciona bien ("model not found")
- Sin nodo nativo para n8n
- Ecosistema de skills muy incipiente vs +13,700 de OpenClaw

### Cuándo revisitarlo

Cuando llegue a **v1.0** (meta: mediados 2026). Si resuelve el soporte Ollama y agrega integración n8n, podría reemplazar a OpenClaw como base del pipeline.

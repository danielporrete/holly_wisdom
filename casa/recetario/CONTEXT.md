# Recetario — Contexto del proyecto

## Qué es esto

Sistema de notificaciones de menú diario vía Telegram.
Consulta Notion, elige el plato del día según rotación automática, y envía el mensaje.

## Archivos

- `meal_bot.py` — script principal
- `requirements.txt` — dependencias (solo `requests`)
- `.env.example` — variables de entorno necesarias

## Notion

- **Página principal:** Daily Meals Program
- **Base de datos:** Meals (`d2731541-8994-4d95-bcd9-a8ddf3eca721`)
- **67 platos** organizados por día (Lunes–Sábado), solo almuerzos
- **Sin domingos**
- Cada plato es una página con Ingredientes + Preparación (o link de YouTube + notas)

## Lógica de rotación

```
semana_ISO % cantidad_platos_del_día = índice_del_plato
```

Ejemplo: si hay 4 platos de Lunes y hoy es semana 15 → plato #3 (15 % 4 = 3)
Automático, sin estado, sin configuración mensual.

## Cron jobs a configurar

```
# 8pm — menú de mañana con receta completa
0 20 * * 1-6  cd /ruta/recetario && python meal_bot.py --tomorrow

# 6pm — lista de verificación de hoy
0 18 * * 1-6  cd /ruta/recetario && python meal_bot.py --today
```

## Variables de entorno necesarias

```
NOTION_TOKEN=secret_...       # Integration token de Notion (ClaudeCode bot)
TELEGRAM_TOKEN=...            # Token del bot claude_fnsk_bot
TELEGRAM_CHAT_ID=...          # Chat ID de Daniel
```

## Cómo obtener el NOTION_TOKEN

Settings de Notion → Connections → ClaudeCode integration → copiar el token interno.

## Cómo obtener el TELEGRAM_CHAT_ID

Mandar cualquier mensaje al bot y consultar:
https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates

## Próximos pasos

1. Instalar dependencias: `pip install -r requirements.txt`
2. Crear `.env` con las 3 variables
3. Probar: `python meal_bot.py --tomorrow`
4. Configurar cron jobs

#!/usr/bin/env python3
"""
meal_bot.py — Notificaciones diarias de menú vía Telegram

Uso:
  python meal_bot.py --tomorrow   # 8pm: menú de mañana + receta completa
  python meal_bot.py --today      # 6pm: lista de verificación de hoy
"""

import os
import sys
import argparse
import requests
from datetime import date, timedelta

NOTION_TOKEN  = os.environ["NOTION_TOKEN"]
NOTION_DB_ID  = "d2731541-8994-4d95-bcd9-a8ddf3eca721"
TELEGRAM_TOKEN   = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

WEEKDAY_MAP = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    # 6 = Domingo — sin menú programado
}


# ── Notion helpers ─────────────────────────────────────────────────────────────

def notion_headers() -> dict:
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }


def get_meals_for_day(day_name: str) -> list:
    """Devuelve todos los platos asignados a un día, ordenados por Fecha ascendente."""
    url = f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query"
    body = {
        "filter": {
            "property": "Día Asignado",
            "select": {"equals": day_name},
        },
        # Platos con Fecha primero (orden de rotación), sin fecha al final
        "sorts": [{"property": "Fecha", "direction": "ascending"}],
    }
    resp = requests.post(url, headers=notion_headers(), json=body)
    resp.raise_for_status()
    return resp.json()["results"]


def get_page_blocks(page_id: str) -> list:
    """Obtiene todos los bloques de contenido de una página de Notion."""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    resp = requests.get(url, headers=notion_headers())
    resp.raise_for_status()
    return resp.json()["results"]


# ── Rotación ────────────────────────────────────────────────────────────────────

def pick_meal(meals: list, target_date: date) -> dict | None:
    """
    Elige el plato para la fecha dada usando el número de semana ISO.
    La rotación es automática: semana N → meals[N % len(meals)]
    """
    if not meals:
        return None
    week_num = target_date.isocalendar()[1]
    return meals[week_num % len(meals)]


def meal_name(meal: dict) -> str:
    title = meal["properties"]["Nombre"]["title"]
    return "".join(t["plain_text"] for t in title) if title else "Plato sin nombre"


# ── Parser de contenido de receta ───────────────────────────────────────────────

def parse_recipe(blocks: list) -> dict:
    """
    Convierte los bloques de Notion en una estructura de receta.
    Soporta recetas con secciones Ingredientes/Preparación y recetas con video + notas.
    """
    recipe = {"ingredients": [], "steps": [], "notes": [], "video": None}
    current_section = None

    for block in blocks:
        btype = block["type"]

        if btype in ("heading_1", "heading_2", "heading_3"):
            text = _plain_text(block, btype).lower()
            if "ingrediente" in text:
                current_section = "ingredients"
            elif "preparaci" in text or "pasos" in text:
                current_section = "steps"
            else:
                current_section = "notes"

        elif btype == "bulleted_list_item":
            text = _plain_text(block, btype)
            if text and current_section in ("ingredients", "steps", "notes"):
                recipe[current_section].append(text)

        elif btype == "paragraph":
            rich = block.get("paragraph", {}).get("rich_text", [])
            for rt in rich:
                if rt.get("type") == "mention":
                    lm = rt.get("mention", {}).get("link_mention", {})
                    href = lm.get("href", "")
                    if "youtube" in href or "youtu.be" in href:
                        recipe["video"] = href
                elif rt.get("type") == "text":
                    text = rt.get("plain_text", "").strip()
                    if text:
                        recipe["notes"].append(text)

    return recipe


def _plain_text(block: dict, btype: str) -> str:
    rich = block.get(btype, {}).get("rich_text", [])
    return "".join(t.get("plain_text", "") for t in rich)


# ── Mensajes Telegram ───────────────────────────────────────────────────────────

def build_tomorrow_message(name: str, recipe: dict) -> str:
    lines = [f"🍽️ <b>Mañana cocinamos:</b> {name}\n"]

    if recipe["ingredients"]:
        lines.append("📋 <b>Ingredientes:</b>")
        for ing in recipe["ingredients"]:
            lines.append(f"  • {ing}")
        lines.append("")

    if recipe["steps"]:
        lines.append("👨‍🍳 <b>Preparación:</b>")
        for step in recipe["steps"]:
            lines.append(f"  {step}")
        lines.append("")

    if recipe["notes"]:
        lines.append("💡 <b>Notas:</b>")
        for note in recipe["notes"]:
            lines.append(f"  {note}")
        lines.append("")

    if recipe["video"]:
        lines.append(f'🎥 <a href="{recipe["video"]}">Ver receta en video</a>')

    return "\n".join(lines)


def build_checklist_message(name: str, recipe: dict) -> str:
    lines = [f"⏰ <b>Hoy cocinamos:</b> {name}\n"]

    if recipe["ingredients"]:
        lines.append("✅ <b>Lista de verificación:</b>")
        for ing in recipe["ingredients"]:
            lines.append(f"  ☐ {ing}")
        lines.append("")

    if recipe["steps"]:
        lines.append("🔥 <b>Pasos:</b>")
        for step in recipe["steps"]:
            lines.append(f"  → {step}")
        lines.append("")

    if recipe["notes"]:
        lines.append("💡 " + " | ".join(recipe["notes"]))

    if recipe["video"]:
        lines.append(f'\n🎥 <a href="{recipe["video"]}">Ver receta</a>')

    return "\n".join(lines)


# ── Telegram ────────────────────────────────────────────────────────────────────

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
    })
    resp.raise_for_status()
    return resp.json()


# ── Main ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Daily meal notifications")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tomorrow", action="store_true",
                       help="8pm: envía el menú de mañana con receta completa")
    group.add_argument("--today", action="store_true",
                       help="6pm: envía la lista de verificación de hoy")
    args = parser.parse_args()

    target_date = date.today() + timedelta(days=1) if args.tomorrow else date.today()
    weekday = target_date.weekday()

    if weekday not in WEEKDAY_MAP:
        print(f"Domingo — sin menú programado. Que descansen las ollas 🥘")
        sys.exit(0)

    day_name = WEEKDAY_MAP[weekday]
    meals = get_meals_for_day(day_name)

    if not meals:
        print(f"No hay platos asignados para {day_name} en Notion.")
        sys.exit(1)

    meal = pick_meal(meals, target_date)
    name = meal_name(meal)
    blocks = get_page_blocks(meal["id"])
    recipe = parse_recipe(blocks)

    if args.tomorrow:
        message = build_tomorrow_message(name, recipe)
        print(f"[8pm] Enviando: {name}")
    else:
        message = build_checklist_message(name, recipe)
        print(f"[6pm] Enviando checklist: {name}")

    result = send_telegram(message)
    msg_id = result["result"]["message_id"]
    print(f"OK — mensaje {msg_id} enviado a chat {TELEGRAM_CHAT_ID}")


if __name__ == "__main__":
    main()

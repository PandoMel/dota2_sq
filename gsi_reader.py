# gsi_reader.py

import requests

def get_game_state():
    try:
        response = requests.get("http://localhost:3000", timeout=2)
        return response.json()
    except Exception as e:
        print(f"[Ошибка GSI] Не удалось получить данные: {e}")
        return None

def extract_state(game_data):
    """
    Преобразует сырые данные GSI в числовой вектор состояния.
    Это лишь пример; можно расширить.
    """
    hero = game_data.get("hero", {})
    enemies = game_data.get("entities", [])

    health = hero.get("health", 0)
    max_health = hero.get("max_health", 1)
    mana = hero.get("manacurrent", 0)
    enemy_count = len([e for e in enemies if "npc_dota_creep" in e.get("name", "")])

    state = [
        health / max_health,
        mana / 100,
        enemy_count / 10,
        game_data.get("map", {}).get("game_time", 0) / 60,
        game_data.get("map", {}).get("clock_time", 0) / 60,
        hero.get("level", 1),
        int(hero.get("alive", False)),
        hero.get("xpos", 0) / 10000,
        hero.get("ypos", 0) / 10000,
        game_data.get("player", {}).get("kills", 0)
    ]

    return state

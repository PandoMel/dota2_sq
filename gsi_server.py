# gsi_server.py

from flask import Flask, request, jsonify
import json
from actions import use_ability, attack_enemy
import threading

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_gsi():
    data = request.get_json()

    # Выводим всё состояние (для дебага)
    print(json.dumps(data, indent=2))

    # === Анализируем состояние ===
    hero = data.get("hero", {})
    player_name = hero.get("name")
    health = hero.get("health")
    max_health = hero.get("max_health")

    print(f"[Герой] {player_name} | Здоровье: {health}/{max_health}")

    # === Пример логики ===
    if health < 0.3 * max_health:
        print("[Реакция] Герой ранен! Используем способность 1.")
        use_ability(1)

    # === Атака врагов ===
    enemies = data.get("entities", [])
    for enemy in enemies:
        if "npc_dota_creep" in enemy.get("name", "") and enemy.get("health", 0) > 0:
            print(f"[Враг обнаружен] {enemy['name']}")
            attack_enemy()
            break

    return jsonify({"status": "ok"}), 200


def run_server():
    app.run(host="localhost", port=3000)


if __name__ == "__main__":
    print("🚀 Запуск GSI-сервера...")
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    print("🌐 Сервер запущен на http://localhost:3000")
  

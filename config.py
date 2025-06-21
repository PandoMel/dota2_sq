# config.py
models_path = 'models/'
GSI_URL = "http://localhost:3000"  # Адрес GSI сервера
HERO_NAME = "npc_dota_hero_phantom_assassin"
ACTION_INTERVAL = 1.0  # Время между действиями (в секундах)
STATE_SIZE = 10        # Размер вектора состояния
ACTION_SPACE = 5       # Возможные действия: [move, attack, ability_1, ability_2, buy]
REWARD_WIN = 100
REWARD_DEATH = -100
REWARD_ALIVE = 1

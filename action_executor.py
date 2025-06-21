# action_executor.py

from actions import use_ability, attack_enemy, press_key

def execute_action(action_idx):
    """
    Выполняет действие по индексу.
    0: перемещение
    1: атака
    2: способность 1
    3: способность 2
    4: покупка предмета
    """
    if action_idx == 0:
        press_key('m')  # Пример: перемещение мышкой
    elif action_idx == 1:
        attack_enemy()
    elif action_idx == 2:
        use_ability(1)
    elif action_idx == 3:
        use_ability(2)
    elif action_idx == 4:
        press_key('d')  # Пример: купить предмет D
        

# actions.py

import pyautogui
import time

def press_key(key):
    """Эмулирует нажатие клавиши"""
    pyautogui.press(key)
    time.sleep(0.05)

def move_to(x, y):
    """Перемещение мыши на координаты"""
    pyautogui.moveTo(x, y)
    time.sleep(0.1)

def click():
    """Клик мышью"""
    pyautogui.click()
    time.sleep(0.1)

def use_ability(slot):
    """Использование способности по слоту (Q=1, W=2, E=3, R=4)"""
    keys = ['q', 'w', 'e', 'r']
    if 0 < slot <= len(keys):
        press_key(keys[slot - 1])

def attack_enemy():
    """Простая атака: Q + клик мыши"""
    press_key('q')
    click()

def buy_item(item_key):
    """Покупка предмета (например, d для daggers)"""
    press_key('d')  # Пример: покупка предмета по клавише D

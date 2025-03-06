import keyboard
import pyautogui
import random
import sys
import time


def search_template(img_name, confidence=0.99):
    mouse_pos = pyautogui.locateOnScreen(r'.\templates\{}'.format(img_name), confidence=confidence)
    return mouse_pos


def sleep_random(base=1000):
    time.sleep(random.randint(base + 500, base + 1000) / 1000)


def imitate_click(l, t):
    pyautogui.leftClick(l, t)
    sleep_random()


def check_enough_hero_count():
    result = True
    for i in range(3):
        mouse_pos = search_template('heroes_count{}.png'.format(i))
        result = False if mouse_pos is not None else result
    return result


def check_is_there_quest_slot():
    mouse_pos = search_template('quests_full.png')
    return False if mouse_pos is not None else True


while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    if check_enough_hero_count() and check_is_there_quest_slot():
        mouse_pos = search_template('quest.png')
        imitate_click(mouse_pos.left, mouse_pos.top)
        mouse_pos = search_template('grindable_quest.png', confidence=0.8)
        imitate_click(mouse_pos.left, mouse_pos.top)
        mouse_pos = search_template('explore_area.png')
        imitate_click(mouse_pos.left, mouse_pos.top)
        mouse_pos = search_template('close_icon.png')
        imitate_click(mouse_pos.left, mouse_pos.top)
    mouse_pos = search_template('grindable_quest_completed.png')
    if mouse_pos:
        imitate_click(mouse_pos.left, mouse_pos.top)
        sleep_random(base=5000)
        mouse_pos = search_template('collect_all.png')
        imitate_click(mouse_pos.left, mouse_pos.top)

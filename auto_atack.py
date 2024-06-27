#Executar: python .\auto_attack.py
#.\bot\Scripts\activate

from time import sleep
import button
import keyboard as kb
import pyautogui as pg # Executar no terminal: python -m venv bot # pip install pyautogui pynput #
from pynput.keyboard import Listener
from pynput import keyboard


#while True:
#   print(pg.position())


SUYANE = 1182, 530
#RENAN = 1732, 617
ARCANINE = ['F8', 'F6', 'F3', 'F7'] 
MIGHT = ['F8', 'F7', 'F6', 'F9']


def revive():
    my_position = pg.position()
    pg.moveTo(SUYANE)
    pg.click(button="right")
    kb.press(button.key['TAB'])
    pg.click(button="right")
    pg.moveTo(my_position)

def attack(hotkey, delay=0.6):
    for item in hotkey:
        kb.press(button.key[item], delay)


def key_code(key):
    if key == keyboard.Key.delete:
        return False
    if key == keyboard.Key.home:
        revive()
    if key == keyboard.Key.alt:
        kb.press(button.key['F'])
        attack(ARCANINE)
        pg.time.sleep(2.3) #ARCANINE = 2.3 / MIGHT = 1
        revive()
        kb.press(button.key['R'])
        
        
with Listener(on_press=key_code) as listener:
    listener.join()
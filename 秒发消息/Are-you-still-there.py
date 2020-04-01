import time
'''
try:
    import pynput
except ImportError:
    import os
    os.system('pip3 install pynput')
'''
from pynput.keyboard import Controller as key_cl
from pynput.mouse import Button, Controller

def keyboard_input(string):
    keyboard = key_cl()
    keyboard.type(string)

def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

def main(number, string):
    time.sleep(0.5)
    for i in range(number):
        keyboard_input(string)
        mouse_click()
        time.sleep(0.2)

if __name__ == "__main__":
    with open("like.txt",'r',encoding='UTF-8') as f:
        alldata = f.readlines()
        for i in alldata:
            main(1, i)

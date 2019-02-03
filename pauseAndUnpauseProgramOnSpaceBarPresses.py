##pauseAndUnpauseProgramOnSpaceBarPresses用空白鍵執行與暫停程式
import keyboard
import pyautogui
import random
import string
import time

phrase = str()
n = 0


class Get(object):
    wait = False
    def do_this(self, e):
        self.wait = not self.wait

a = Get()
keyboard.on_press_key("space", a.do_this)
while True:
    if not a.wait:
        if n > 5:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            n = 0
        else:
            for i in range(random.randint(1,10)):
                letter = random.choice(string.ascii_letters)
                phrase = phrase + letter
            print(phrase)
            pyautogui.typewrite(phrase)
            pyautogui.press("enter")
            phrase = str()
            n = n + 1
            time.sleep(0.005+0.001*random.randint(1,10))

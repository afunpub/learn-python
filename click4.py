##按F12每3秒按4
import keyboard,pyautogui,time
width,height=pyautogui.size()
def function1():
    pyautogui.press('4')
    time.sleep(3)

def buff():
    pyautogui.press('2')
    time.sleep(0.3)
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')
    
class Get():
    wait=False
    def doThis(self,e):
        self.wait=not self.wait
a=Get()
keyboard.on_press_key("f12",a.doThis)
keyboard.add_hotkey('f11',buff)
while True:
    if a.wait:
        function1()
        
    
        

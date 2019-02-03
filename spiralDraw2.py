##按F12在滑鼠目前座標順時針畫旋螺
import keyboard,pyautogui,time
width,height=pyautogui.size()
def spiralDraw():
    distance=200
    while distance >0:
        pyautogui.dragRel(distance,0,duration=0.2)
        distance -=5
        pyautogui.dragRel(0,distance,duration=0.2)
        pyautogui.dragRel(-distance,0,duration=0.2)
        distance -=5
        pyautogui.dragRel(0,-distance,duration=0.2)

class Get():
    wait=False
    def doThis(self,e):
        self.wait=not self.wait
a=Get()
keyboard.on_press_key("f9",a.doThis)
while True:
    if a.wait:
        spiralDraw()
        time.sleep(3)
    
        

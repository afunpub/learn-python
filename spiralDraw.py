##在滑鼠目前座標順時針畫旋螺
import pyautogui,time
time.sleep(5)
width,height = pyautogui.size()
pyautogui.click() #click to put draw program in focus
def spiralDraw():
    distance = 200
    while distance>0:
        pyautogui.dragRel(distance,0,duration=0.2) #draw right
        distance -=5
        pyautogui.dragRel(0,distance,duration=0.2) #draw down
        pyautogui.dragRel(-distance,0,duration=0.2) #draw left
        distance -=5
        pyautogui.dragRel(0,-distance,duration=0.2) #draw up

spiralDraw()      



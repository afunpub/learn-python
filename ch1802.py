##在滑鼠目前座標順時針移動100單位
import pyautogui
width,height = pyautogui.size()
for i in range(10):
	pyautogui.moveRel(100,0,duration=0.25)
	pyautogui.moveRel(0,100,duration=0.25)
	pyautogui.moveRel(-100,0,duration=0.25)
	pyautogui.moveRel(0,-100,duration=0.25)

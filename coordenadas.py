import time
import pyautogui

time.sleep(5)
x, y = pyautogui.position()
print ("x = "+str(x)+" y = "+str(y))
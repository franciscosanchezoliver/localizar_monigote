from pyautogui import *

while True:
    ruta_monigote = "monigote.png"
    if pyautogui.locateOnScreen(ruta_monigote) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
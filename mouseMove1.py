import pyautogui

run = True

print(pyautogui.position())

while (run == True):
    
    pyautogui.moveTo(1700, 30, duration = 1)
    pyautogui.moveTo(1750, 30, duration = 2)
    

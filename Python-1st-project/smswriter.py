import pyautogui
import time
massage = 5
while massage >0:
    time.sleep(4)
    pyautogui.typewrite("Mama Khela hobe ajke")
    pyautogui.typewrite("Khela Hobe, Khela hobe")
    time.sleep(2)
    pyautogui.press('enter')
    massage = massage - 1
import pyautogui
import time

x1 = input('X coord : ')
y1 = input('Y coord : ')
clicks = input('Number of clicks : ')
delay = input('Delay : ')


def GameClick(x1, y1, clicks, delay):
    for k in range(clicks):
        pyautogui.moveTo(x1, y1)
        pyautogui.click()
        time.sleep(delay)
    
x1 = int(x1)
y1 = int(y1)
clicks = int(clicks)
delay = float(delay)

GameClick(x1, y1, clicks, delay)

print('Auto click session is finish !')

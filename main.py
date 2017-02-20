import pyautogui
import time

x1 = input('Rentrez la coordonnée X en pixels de votre premier click : ')
y1 = input('Rentrez la coordonnée Y en pixels de votre premier click : ')
x2 = input('Rentrez la coordonnée X en pixels votre second click : ')
y2 = input('Rentrez la coordonnée Y en pixels votre second click : ')
clicks = input('Rentrez le nombre de clicks que vous voulez faire : ')
delay = input('Rentrez l’interval de temps entre chaque clique (en secondes) : ')


def GameClick(x1, y1, x2, y2, clicks, delay):
    for k in range(clicks):
        pyautogui.moveTo(x1, y1)
        pyautogui.click(clicks=200)
        print('first click')
        time.sleep(delay)
        pyautogui.moveTo(x2, y2)
        pyautogui.click(clicks=200)
        print('second click')
        time.sleep(delay)


x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
clicks = int(clicks)
delay = float(delay)

GameClick(x1, y1, x2, y2, clicks, delay)

print('Auto click session is finish !')

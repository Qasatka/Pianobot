from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#tile 1 X:  590 Y:  640 RGB: (158, 164, 231)
#tile 2 X:  675 Y:  640 RGB: (156, 162, 230)
#tile 3 X:  757 Y:  640 RGB: (253,  18,   1)
#tile 4 X:  842 Y:  640 RGB: (169, 173, 232)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(590, 350)[0] == 0:
        click(590, 350)
    if pyautogui.pixel(675, 350)[0] == 0:
        click(675, 350)
    if pyautogui.pixel(757, 350)[0] == 0:
        click(757, 350)
    if pyautogui.pixel(842, 350)[0] == 0:
        click(842, 350)
    

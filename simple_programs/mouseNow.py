"""
    This simple program was written for learning and exercise purposes.

    Features involved:
        - module import(pyautogui)
        - flow control: while loop

    Sources:
        https://automatetheboringstuff.com/chapter18/
"""

import pyautogui
import time


while True:
    x, y = pyautogui.position()
    position_str = str(x) + ', ' + str(y)
    print(position_str, end='')
    time.sleep(0.01)
    print('\b' * len(position_str), end='', flush=True)


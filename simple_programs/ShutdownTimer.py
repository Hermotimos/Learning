"""
    This simple program was written for learning and exercise purposes.

    Features involved:
        - modules import (os, time)
        - user defined functions
        - exception handling, assertions
        - flow control: if else, while

    Sources:
        https://automatetheboringstuff.com/chapter18/
"""


import os
import time


def shutdown_countdown():
    mode = ask_shutdown_mode()
    minutes = ask_time()
    ending = ''

    if minutes == 1:
        ending = 'ę'
    elif 1 < minutes < 5:
        ending = 'y'
    print(f'\nKomputer zostanie wyłączony za {minutes} minut{ending}.'
          '\n\t ...Zapisz otwarte pliki przed końcem odliczania, aby uniknąć utraty danych.'
          '\n\t\t ...W każdej chwili możesz przerwać odliczanie przez wyłączenie okna programu.')

    timer_secs = minutes * 60
    while timer_secs > 0:
        """
        'minutes' are deprecated before first print, 
        cause exe file created by pyinstaller misses a minute somehow and prints this variable only after 1 min
        """
        minutes -= 1
        print('\n', str(minutes), end='')
        timer_secs -= 60
        time.sleep(60)
    os.system(f"{mode}")


def ask_time():
    entry = input("Podaj za ile minut chcesz wyłączyć komputer i zatwierdź przez ENTER:\n")
    try:
        assert int(entry) > 0
        return int(entry)
    except Exception:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_time()


def ask_shutdown_mode():
    entry = input("Wybierz opcję zamykania systemu:\n1 - zamknięcie \n2 - hibernacja\n")
    mode = ''
    try:
        assert entry in ("1", "2")
        if entry == "1":
            mode = "shutdown /s /t 1"
        elif entry == "2":
            mode = "shutdown /h"
        return mode
    except AssertionError:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_shutdown_mode()


shutdown_countdown()

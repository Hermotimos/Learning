"""
    This simple program was written for learning and exercise purposes.

    Features involved:
        - modules import (os, time)
        - user defined functions
        - exception handling, assertions
        - flow control: if else, while loop
"""

import os
import time


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


def ask_time():
    entry = input("Podaj za ile minut chcesz wyłączyć komputer i zatwierdź przez ENTER:\n")
    try:
        assert int(entry) > 0
        return entry
    except Exception:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_time()


def shutdown_countdown():
    mode = ask_shutdown_mode()
    minutes_str = ask_time()
    ending = ''

    if minutes_str == "1":
        ending = 'ę'
    elif 1 < int(minutes_str[-1]) < 5:
        ending = 'y'
    print(f'\nKomputer zostanie wyłączony za {minutes_str} minut{ending}.'
          '\n\t ...Zapisz otwarte pliki przed końcem odliczania, aby uniknąć utraty danych.'
          '\n\t\t ...W każdej chwili możesz przerwać odliczanie przez wyłączenie okna programu.')

    minutes_int = int(minutes_str)
    timer_secs = minutes_int * 60
    while timer_secs > 0:
        """
        'minutes' are deprecated before first print, 
        cause exe file created by pyinstaller misses a minute somehow and prints this variable only after 1 min
        """
        minutes_int -= 1
        print('\n', str(minutes_int), end='')
        timer_secs -= 60
        time.sleep(60)
    os.system(f"{mode}")


shutdown_countdown()

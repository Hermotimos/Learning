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
    """
    Ask user to choose shutdown option (shutdown or hibernation). In case of wrong value ask recursively.

    Returns
    -------
    str: Shutdown command.
    """
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
    """
    Ask user to enter countdown start value in minutes. In case of wrong value ask recursively.

    Returns
    -------
    str: Number of minutes entered as str type.
    """
    entry = input("Podaj za ile minut chcesz wyłączyć komputer i zatwierdź przez ENTER:\n")
    try:
        assert int(entry) > 0
        return entry
    except Exception:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_time()


def shutdown_countdown():
    """
    Print countdown every minute and finally shutdown/hibernate system.

    Prints info about chosen countdown value and warns user to save progress before shutdown.
    Prints countdown every minute. When countdown ends, performs shutdown/hibernation.
    """
    mode = ask_shutdown_mode()
    minutes_str = ask_time()
    ending = ''

    if minutes_str == "1":
        ending = "ę"
    elif 1 < int(minutes_str[-1]) < 5:
        ending = "y"
    print(f'\nKomputer zostanie wyłączony za {minutes_str} minut{ending}.'
          '\n\t ...Zapisz otwarte pliki przed końcem odliczania, aby uniknąć utraty danych.'
          '\n\t\t ...W każdej chwili możesz przerwać odliczanie przez wyłączenie okna programu.')

    minutes_int = int(minutes_str)
    timer_secs = minutes_int * 60
    while timer_secs > 0:
        print(f'\n{minutes_int}', minutes_int, end="")
        timer_secs -= 60
        minutes_int -= 1
        time.sleep(60)

    os.system(f"{mode}")


shutdown_countdown()

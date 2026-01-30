"""
# Locallama.
/src/locallama_detroix23/modules/controls.py
"""

import sys

ESC: str = "\033"


def move_up(times: int, flush: bool = False) -> None:
    """
    Move the terminal cursor up `times`. Can write over text.
    """
    sys.stdout.write(f"{ESC}[{times}A")
    if flush:
        sys.stdout.flush()

def cursor_show(flush: bool = False) -> None:
    """
    Print in the console `<ESC>[?25h`.
    """  
    sys.stdout.write(f"{ESC}[?25h")
    if flush:
        sys.stdout.flush()

def cursor_hide(flush: bool = False) -> None:
    """
    Print in the console `<ESC>[?25l`.
    """  
    sys.stdout.write(f"{ESC}[?25l")
    if flush:
        sys.stdout.flush()
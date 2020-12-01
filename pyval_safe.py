#!/usr/bin/env python3

"""
Programme pour evaluer un expression
(version non sécuritaire et modulaire)

2020, Austin Brodeur
"""
from m_safe_eval import safe_eval as eval # noqa
import colorama
from colorama import Fore
colorama.init()
import sys
from math import * # noqa
from typing import NoReturn

def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def main() -> None:
    """Fonction Principale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None")
        print(Fore.CYAN + "Selon Austin Brodeur:",Fore.RESET,evaluation)
    except BaseException as ex:
        exexit(ex)


if __name__ == '__main__':
    main()
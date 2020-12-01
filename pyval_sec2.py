#!/usr/bin/env python3

"""
Programme pour evaluer un expression
(version sécuritaire et modulaire et ayant un timeout)

2020, Austin Brodeur
"""
from m_timeout_eval import timeout_eval as eval # noqa
import colorama
from colorama import Fore
colorama.init()
import sys
from math import * # noqa
from typing import NoReturn

def exexit(ex: Exception, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def main() -> None:
    """Fonction Principale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None",delai_sec=2.0)
        print(Fore.CYAN + "Selon Austin Brodeur:",Fore.RESET,evaluation)
    except TimeoutError:
        exexit(TimeoutError("Le délai d'exécution est dépassé."))
    except Exception as ex:
        exexit(ex)


if __name__ == '__main__':
    main()
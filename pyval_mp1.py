#!/usr/bin/env python3

"""
Programme pour evaluer un expression
(version sécuritaire et modulaire)

2020, Austin Brodeur
"""
import sys
from typing import NoReturn
import colorama
from colorama import Fore
colorama.init()
import pyval_safe
from multiprocessing import Process

DELAI_SEC = 2.0
def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)
def main() -> None:
    """fonction principale"""
    try:
        ps = Process(target=pyval_safe.main)
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le delai de {DELAI_SEC} secondes est écoulé")
        else:
            sys.exit(ps.exitcode)

    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
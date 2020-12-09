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

DELAI_SEC = 5.0
def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print("\n",Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)
def main() -> None:
    """fonction principale"""
    try:
        ps = Process(target=pyval_safe.main)
        ps.start()

        incrément = 0.1
        temps = 0.0

        while ps.is_alive() and temps < DELAI_SEC:
            if temps > 0.1:
                print('.', end='',flush=True)
            ps.join(incrément)
            temps += incrément

        if ps.is_alive():
            ps.terminate()
            print()
            raise TimeoutError(f"Le delai de {DELAI_SEC} secondes est écoulé")
        else:
            sys.exit(ps.exitcode)

    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

"""
Programme pour evaluer un expression
(version sécuritaire et modulaire)

2020, Austin Brodeur
"""
import sys
import time
from typing import NoReturn
import colorama
from colorama import Fore
import os
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

def print_forever(ceci: str, delai_sec: float) -> None:
    """afficher repetivement qqch"""
    try:
        while True:
            time.sleep(delai_sec)
            print(ceci, end='',flush=True)
    except KeyboardInterrupt:
        pass
def main() -> None:
    """fonction principale"""
    try:
        ps_eval = Process(target=pyval_safe.main)
        ps_eval.start()

        ps_dot = Process(target=print_forever, args=('.',0.1))
        ps_dot.start()

        print('délai:',DELAI_SEC,
              '--','main:', os.getpid(),
              '--','ps_eval:', ps_eval.pid,
              '--','ps_dot:', ps_dot.pid)
        ps_eval.join(DELAI_SEC)
        ps_dot.terminate()

        if ps_eval.is_alive():
            ps_eval.terminate()
            print()
            raise TimeoutError(f"Le delai de {DELAI_SEC} secondes est écoulé")
        else:
            sys.exit(ps_eval.exitcode)

    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
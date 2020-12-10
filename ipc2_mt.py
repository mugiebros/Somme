#!/usr/bin/env python3

"""
Évaluer une expression python dans un sous processeur

Par austin brodeur
"""
import sys
from m_safe_eval import safe_eval
from multiprocessing import Process
from typing import NoReturn
from threading import Thread
import colorama
from colorama import Fore
colorama.init()
DELAI_SEC = 2.0
ÉVALUATION = None
"""Variable globale pour le résultat"""
def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def pyval(expr: str) -> None:
    """
    évalue une exprésion
    retour via variable global
    """
    global ÉVALUATION
    try:
        ÉVALUATION = safe_eval(expr)
        print(expr, '=', ÉVALUATION)
    except BaseException as ex:
        exexit(ex)

def main() -> None:
    """fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or None
        th = Thread(target=pyval, args=(expr,))
        th.start()
        th.join(DELAI_SEC)
        if th.is_alive():
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        print(Fore.CYAN + "Selon Austin Brodeur:",Fore.RESET,ÉVALUATION)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
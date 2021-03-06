#!/usr/bin/env python3

"""
Évaluer une expression python dans un sous processeur

Par austin brodeur
"""
import sys
import ctypes
from m_safe_eval import safe_eval
from multiprocessing import Process, Value
from typing import NoReturn
import colorama
import pickle
from colorama import Fore
colorama.init()
DELAI_SEC = 2.0

def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def pyval(expr: str, filename: str) -> None:
    """
    évalue une expression
    retour via argument
    """
    try:
        évaluation = safe_eval(expr)
        print(expr, '=', évaluation)

    except BaseException as ex:
        évaluation = ex

    with open(filename, 'w+b') as f:
        pickle.dump(évaluation, f)

def main() -> None:
    """fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or None
        filename = "ipc6.bin"
        ps = Process(target=pyval, args=(expr,filename))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        with open(filename, "r+b") as f:
            évaluation = pickle.load(f)
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Fichier selon Austin Brodeur:",Fore.RESET,évaluation)
    except KeyboardInterrupt as ex:
        exexit(ex)
    except Exception as ex:
        exexit(ex)

if __name__ == '__main__':
    main()
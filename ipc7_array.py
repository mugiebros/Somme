#!/usr/bin/env python3

"""
Évaluer une expression python dans un sous processeur

Par austin brodeur
"""
import sys
import ctypes
from m_safe_eval import safe_eval
import multiprocessing as mp
from multiprocessing import Process, Value
from typing import NoReturn
import colorama
import pickle
from colorama import Fore
colorama.init()
DELAI_SEC = 2.0
ARRAY_SIZE = 2048
def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def pyval(expr: str, retour: mp.Array) -> None:
    """
    évalue une expression
    retour via argument
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    sérialisation: bytes = pickle.dumps(évaluation)
    if len(sérialisation) > ARRAY_SIZE:
        print(Fore.YELLOW, "[AB] ",
              Fore.RED, "PicklingError",
              Fore.YELLOW,
              f": La taille du résultat ({len(sérialisation)} octets) est trop grande pour le buffer interprocesseur (max = {ARRAY_SIZE}) ",
              file=sys.stderr, sep='')
        sys.exit(1)
    retour[:len(sérialisation)] = sérialisation

def main() -> None:
    """fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or None
        retour = mp.Array(ctypes.c_char, ARRAY_SIZE)
        ps = Process(target=pyval, args=(expr,retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        if ps.exitcode == 1:
            sys.exit(1)
        évaluation = pickle.loads(bytes(retour[:]))
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Array selon Austin Brodeur:",Fore.RESET,évaluation)
    except KeyboardInterrupt as ex:
        exexit(ex)
    except Exception as ex:
        exexit(ex)

if __name__ == '__main__':
    main()
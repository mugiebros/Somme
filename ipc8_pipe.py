#!/usr/bin/env python3

"""
Évaluer une expression python dans un sous processeur

Par austin brodeur
"""
import sys
import ctypes
from m_safe_eval import safe_eval
import multiprocessing as mp
from multiprocessing import Process, Value, Pipe
from multiprocessing.connection import Connection
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

def pyval(expr: str, pipe: Connection) -> None:
    """
    évalue une expression
    retour via argument
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    pipe.send(évaluation)
    pipe.close()

def main() -> None:
    """fonction principale"""
    ps: Optional[Process] = None
    try:
        expr = ' '.join(sys.argv[1:]) or None
        parent_conn, child_conn = Pipe()
        ps = Process(target=pyval, args=(expr,child_conn))
        ps.start()
        if not parent_conn.poll(DELAI_SEC):
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        évaluation = parent_conn.recv()
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Pipe selon Austin Brodeur:",Fore.RESET,évaluation)
    except BaseException as ex:
        exexit(ex)
    finally:
        ps and ps.terminate()
if __name__ == '__main__':
    main()
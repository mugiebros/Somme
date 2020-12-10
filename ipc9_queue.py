#!/usr/bin/env python3

"""
Évaluer une expression python dans un sous processeur

Par austin brodeur
"""
import sys
import ctypes
from m_safe_eval import safe_eval
import multiprocessing as mp
from multiprocessing import Process, Queue
from multiprocessing.connection import Connection
from typing import NoReturn
from queue import Empty
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

def pyval(expr: str, queue: Queue) -> None:
    """
    évalue une expression
    retour via argument
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    queue.put(évaluation)

def main() -> None:
    """fonction principale"""
    ps: Optional[Process] = None
    try:
        expr = ' '.join(sys.argv[1:]) or None
        queue = Queue()
        ps = Process(target=pyval, args=(expr, queue))
        ps.start()
        if ps.exitcode == 1:
            sys.exit(1)
        évaluation = queue.get(block=True,timeout=DELAI_SEC)
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Array selon Austin Brodeur:", Fore.RESET, évaluation)
    except Empty:
        exexit(TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé"))
    except BaseException as ex:
        exexit(ex)
    finally:
        ps and ps.terminate()


if __name__ == '__main__':
    main()
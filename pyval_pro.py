#!/usr/bin/env python3

"""
Programme pour evaluer un expression
(version sécuritaire et professionnelle et ayant un timeout)

2020, Austin Brodeur
"""
from m_timeout_eval import timeout_eval as eval # noqa
import colorama
from colorama import Fore
colorama.init()
import sys
from math import * # noqa
from typing import NoReturn
from timeit import default_timer as timer
import argparse
import math
SAFE_GLOBALS = {
    "__builtins__":{},
    **math.__dict__,
    "abs":abs,
    "min":min,
    "max":max,
    "sum":sum,
}
def parser_pro() -> argparse.Namespace:
    """
        arguments
    """
    parser = argparse.ArgumentParser(description="Évaluateur d'expression python -- 2020, par Austin Brodeur")
    parser.add_argument('code', help='expression a evaluer', nargs='+',default="")
    parser.add_argument('-d','--delai',metavar='DÉLAI',help="Délai pour le calcul (défaut 2 sec)",default=2.0)
    parser.add_argument("-m","--minute",help="Minuter la durée d'exécution",action="store_true")

    args = parser.parse_args()
    return args

def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

def sanitize(code: str) -> str:
    """assainit le code source insécure"""
    return code.replace('__','')

def main()-> None:
    """
        Fonction Principale
    """
    parser_pro()
    début = timer()
    if float(parser_pro().delai) <= 0:
        exexit(ValueError("Le délai doit être supérieur à 0"))
    elif float(parser_pro().delai) > 5:
        exexit(ValueError("Le délai doit être au plus de 5 secondes"))
    else:
        try:
            evaluation = eval(sanitize(' '.join(parser_pro().code)),__globals=SAFE_GLOBALS, delai_sec= parser_pro().delai)
            print(Fore.CYAN + "Selon Austin Brodeur:",Fore.RESET,evaluation)
        except TimeoutError:
            exexit(TimeoutError(f"Le délai d'exécution de {parser_pro().delai} secondes est écoulé."))
        except KeyboardInterrupt:
            exexit(KeyboardInterrupt("Interrompu par l'utilisateur"))
        except Exception as ex:
            exexit(ex)
        finally:
            if parser_pro().minute:
                print(Fore.LIGHTMAGENTA_EX + "Durée:",timer() - début, "sec",Fore.RESET)

if __name__ == '__main__':
    main()
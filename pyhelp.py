#!/usr/bin/env python3

"""
Programme pour afficher la documentation python

Par austin brodeur
"""
import sys
import colorama
from colorama import Fore
import re
import math
colorama.init()
GLOBALS = {"__builtins__":{} ,**math.__dict__,"abs":abs,"min":min,"max":max,"sum":sum}
LOCALS = {}
def main() -> None:
    """
        programme principale
    """
    patternpointFin = re.compile("^[A-Za-z0-9_-]*[.]$")
    if len(sys.argv[1:]) != 1:
        print(Fore.YELLOW + "[AB] " + Fore.RED + f"Le code s'attend a recevoir 1 argument, mais vous en avez fourni {len(sys.argv[1:])}",
              file=sys.stderr)
        print(Fore.YELLOW + "Usage: ./pyhelp.py sujet" + Fore.WHITE, file=sys.stderr)
        sys.exit(1)

    if sys.argv[1].count('.') == 1:
        pattern = re.compile("^[^.][.A-Za-z0-9_-]*$")
    else:
        pattern = re.compile("^[^.]([A-Za-z0-9_-]|[^.][.][^.])*[^.]$")

    if pattern.match(sys.argv[1]):
        print(Fore.YELLOW + "[AB] " + Fore.WHITE + "Affichage de l'aide pour: " + Fore.MAGENTA + f"{sys.argv[1]}" + Fore.GREEN,file=sys.stderr)
        try:
            exec(f""+sys.argv[1]+"()",GLOBALS,LOCALS)
        except Exception as exep:
            if exep.__str__() == f"name '{sys.argv[1]}' is not defined":
                print(Fore.YELLOW + "[AB] " + Fore.RED + f"{exep}")
            else:
                help(sys.argv[1])
    else:
        print(Fore.YELLOW + "[AB] " + Fore.RED + "Le sujet de l'aide n'est pas valide: " + Fore.MAGENTA + f"{sys.argv[1]}",
              file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()


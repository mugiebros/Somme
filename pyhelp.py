#!/usr/bin/env python3

"""
Programme pour afficher la documentation python

Par austin brodeur
"""
import sys
import colorama
from colorama import Fore
colorama.init()

def main() -> None:
    """
        programme principale
    """
    if len(sys.argv[1:]) != 1:
        print(Fore.YELLOW + "[AB] " + Fore.RED + f"Le code s'attend a recevoir 1 argument, mais vous en avez fourni {len(sys.argv[1:])}",
              file=sys.stderr)
        print(Fore.YELLOW + "Usage: ./pyhelp.py sujet" + Fore.WHITE, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()


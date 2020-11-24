#!/usr/bin/env python3


"""
programme pour compter les lignes

austin brodeur
"""

import re
import sys
import colorama

from colorama import Fore
colorama.init()

def main() -> None:
    """
        fonction principale
    """
    if sys.stdin.isatty():
        print("Aucune redirection d'entrée à traiter")
        return
    if len(sys.argv[1:]) > 1:
        print(Fore.RED + f"Le code s'attend a recevoir 1 argument, mais vous en avez fourni {len(sys.argv[1:])}",
              file=sys.stderr)
        print(Fore.YELLOW + "Usage: ./pygrep.py pattern" + Fore.WHITE, file=sys.stderr)
        sys.exit(1)
    compteurCo = 0
    lignes = sys.stdin.readlines()
    try:
        regexp = re.compile(sys.argv[1])
    except:
        print(Fore.RED + f"Le code s'attend a recevoir 1 argument, mais vous en avez fourni {len(sys.argv[1:])}",
              file=sys.stderr)
        print(Fore.YELLOW + "Usage: ./pygrep.py pattern" + Fore.WHITE, file=sys.stderr)
        sys.exit(1)

    for ligne in lignes:
        if regexp.search(ligne):
            print(ligne, end=" ")
            compteurCo += 1

    if compteurCo <= 0:
        print(Fore.YELLOW + f"[ aucune correspondances ]" + Fore.WHITE, file=sys.stderr)
    elif compteurCo == 1:
        print(Fore.YELLOW + f"[ {compteurCo} correspondance ]" + Fore.WHITE, file=sys.stderr)
    else:
        print(Fore.YELLOW + f"[ {compteurCo} correspondances ]" + Fore.WHITE, file=sys.stderr)


if __name__ == '__main__':
    main()

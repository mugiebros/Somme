#!/usr/bin/env python3

"""
programme evaluer la valeur

Austin Brodeur
"""
from math import *
import sys
import colorama
from colorama import Style, Fore

colorama.init()


def main() -> None:
    """
        fonction principalle
    """
    try:
        mot = ""
        arg = sys.argv
        for i in arg[1:]:
            mot += fr"{i}"
        print(Style.BRIGHT + Fore.CYAN + f"Selon abrodeur : {eval(mot, globals())}")
    except Exception as erreur:
        print(Style.BRIGHT + Fore.RED + str(erreur), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

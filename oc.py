#!/usr/bin/env python3

"""
fichier de lecture

Austin Brodeur
"""
import colorama
from colorama import Style, Fore

colorama.init()


def main() -> None:
    """
        main
    """
    try:
        with open("océans.txt") as fobj:
            bio = Style.BRIGHT + Fore.CYAN + fobj.read()

    except FileNotFoundError:
        bio = Style.BRIGHT + Fore.RED + "Le Fichier 'océans.txt' n'existe pas."

    print(bio)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
programme pour stocker txt dans un fichier

austin brodeur
"""

import argparse
import os.path
import colorama
from colorama import Fore

colorama.init()


def parse_arg() -> argparse.Namespace:
    """
    parse les arguments
    """
    parser = argparse.ArgumentParser(description="Commande pour créer des fichiers -- @2020, Par Austin Brodeur")
    parser.add_argument('FILE', help='Fichiers à créer', nargs='+')
    groupe = parser.add_mutually_exclusive_group()
    groupe.add_argument('-q', '--quiet', action='store_true', help='Ne pas spécifier si existe déjà')
    groupe.add_argument('-v', '--verbeux', action=r'store_true', help=r"Notifier le créateur")
    parser.add_argument('-t', '--texte', type=str, metavar='TXT', default="",
                        help='Texte a stocker dans les fichiers crées')

    args = parser.parse_args()
    return args


def main() -> None:
    """
    fonction principale
    """
    try:
        for i in parse_arg().FILE:
            if os.path.isfile(i) and parse_arg().quiet == False:
                print(Fore.YELLOW + "Le fichier existe déjà:" + Fore.CYAN + f"{i}")
            else:
                f = open(i, "w+")
                if parse_arg().verbeux:
                    print(Fore.WHITE + "Fichier Créé:" + Fore.CYAN + f"{i}")

                f.write(parse_arg().texte)
                f.close()


    except OSError as ex:
        print(Fore.RED + f"{type(ex)}: " + Fore.YELLOW + f"{ex}" + Fore.WHITE)
        exit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
Programme pour doubler un nomber

Austin Brodeur
"""

import getpass
import sys
import os
import colorama
from colorama import Fore, Style

colorama.init()


def main() -> None:
    """Fonction principale"""
    vérifier_usage()
    try:
        nombre = float(sys.argv[1])
        print(Style.BRIGHT + Fore.CYAN + 'Selon', getpass.getuser(), ':', nombre * 2)

    except ValueError:
        erreur(Style.BRIGHT + Fore.RED + f"L'argument '{sys.argv[1]}' n'est pas un nombre.")


def erreur(msg: object) -> object:
    """Afficher un message d'erreur, puis terminer le script
    :rtype: object
    """
    print(msg, file=sys.stderr)
    sys.exit(1)


def vérifier_usage() -> None:
    """
    vérifier l'usage du programme et en cas d'erreur,
    afficher un message d'erreur et un usag, puis terminer le tout
    :return:
    """
    nbargs = len(sys.argv) - 1
    if nbargs != 1:
        nom_script = os.path.join('.', os.path.basename(sys.argv[0]))
        erreur(
            Style.BRIGHT + Fore.RED + f"Le script s'attend a recevoir 1 argument, mais vous en avez fourni {nbargs}\n" +
            Style.BRIGHT + Fore.YELLOW + f"Usage: {nom_script} nombre")


if __name__ == '__main__':
    main()

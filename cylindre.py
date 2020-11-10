#!/usr/bin/env python3
"""
programme pour calculer des cylindre

austin brodeur
"""
import math
import argparse
import colorama
from colorama import Fore

colorama.init()


def parse_args() -> argparse.Namespace:
    """
        créé les arguments
    """

    parser = argparse.ArgumentParser(description="Calculateur de volume pour cylindre -- @2020, Par Austin Brodeur")

    parser.add_argument('-r', '--rayon', type=float, metavar='R', required=True, help='rayon du cylindre')

    parser.add_argument('-H', '--hauteur', type=float, metavar='H', required=True, help='hauteur du cylindre')
    parser.add_argument('-p', '--précision', type=int, metavar='P', default=20, help='Précision du calcul')
    groupe = parser.add_mutually_exclusive_group()
    groupe.add_argument('-q', '--quiet', action='store_true', help='afficher seulement le volume')
    groupe.add_argument('-v', '--verbeux', action=r'store_true', help=r"afficher le maximum d'info")

    args = parser.parse_args()
    return args


def volume_cylindre(rayon: float, hauteur: float) -> float:
    """
    calcule
    :param rayon:
    :param hauteur:
    :return:
    """
    vol = math.pi * (rayon ** 2) * hauteur
    return vol


def main() -> None:
    """
    fonction principale
    """
    volume = volume_cylindre(parse_args().rayon, parse_args().hauteur)
    parse_args()
    if parse_args().quiet:
        print(Fore.CYAN + f"{round(volume,parse_args().précision)}")
    elif parse_args().verbeux:
        print(Fore.RED +
              f"Le Volume d'un cylindre ayant un rayon de {parse_args().rayon} et une hauteur de {parse_args().hauteur} est de " + Fore.CYAN + f"{round(volume,parse_args().précision)}" + Fore.RED + " selon AB.")
    else:
        print(Fore.GREEN + f"Volume du cylindre selon AB: " + Fore.CYAN + f"{round(volume,parse_args().précision)}")


if __name__ == '__main__':
    main()

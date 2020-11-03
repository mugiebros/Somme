#!/usr/bin/env python3
import sys


def main() -> None:
    """Fonction principale"""

    if sys.stdin.isatty():
        print("Aucune redirection d'entrée à traiter")
        return

    lignes = sys.stdin.readlines()

    if not lignes:
        return

    for ligne in lignes[:-1]:
        print(ligne)
        for i in sys.argv[1:]:
            print(i)
    print(lignes[-1])


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
programme pour accéder aux variables d'environnement

Austin Brodeur
"""
import os
# import pprint
import getpass


def main() -> None:
    """Fonction Principale"""
    print(f"Il y a {len(os.environ)} variables d'environnement")
    print(f" - OS: {os.getenv('OS','Non défini')}")
    print(f" - HOME: {os.getenv('HOMEPATH',os.getenv('HOME','Non défini'))}")

    print()
    print("Code Portable:")
    print(f" - {os.name=}")
    print(f" - user: {getpass.getuser()}")
    print(f" - home: {os.path.expanduser('~')}")


if __name__ == '__main__':
    main()

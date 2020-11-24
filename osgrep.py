#!/usr/bin/env python3

"""
grep sans grep

austin brodeur
"""
import os
import sys
import shlex
def main() -> None:
    """Fonction principale"""
    args = shlex.join(sys.argv[1:])
    commande = "egrep " + args
    exitcode = os.system(commande)
    if exitcode:
        print("La commande exécutée était: " + commande)
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
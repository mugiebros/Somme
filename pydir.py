#!/usr/bin/env python3

"""
programme pour lister le py

austin brodeur
"""
import glob
import sys


def main() -> None:
    """Fonction principale"""
    try:
        finale = []
        liste = glob.glob("*.*")
        for i in sys.argv:
            if i == "pydir":
                sys.argv.remove(i)
                break
            else:
                sys.argv.remove(i)
        liste.sort()
        if len(sys.argv) == 0:
            finale = liste

        else:
            finale = intersection(sys.argv, liste)

        for i in finale:
            print(i)
    except ValueError:
        pass


def intersection(lst1, lst2):
    """
        trouver inter
    :param lst1:
    :param lst2:
    :return:
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


if __name__ == '__main__':
    main()

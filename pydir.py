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
        lol = sys.argv.copy()
        for i in lol:
            if i == "pydir":
                lol.remove(i)
                break
            else:
                lol.remove(i)
        liste.sort()
        if len(lol) == 0:
            finale = liste

        else:
            premier = False
            for i in sys.argv:
                if premier:
                    finale.extend(glob.glob(i))
                else:
                    premier = True
            finale.sort()
            finale = list(dict.fromkeys(finale))

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

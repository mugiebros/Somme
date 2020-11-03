#!/usr/bin/env python3

"""
echo en python

austin brodeur
"""
import sys


def main() -> None:
    """Programme principale"""
    mot = ""
    for i in sys.argv:
        if i == sys.argv[0]:
            print()
        else:
            mot += f"{i} "

    print(f"{mot}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
programe pour montre les infos temporelle

austin brodeur
"""
import datetime


def main() -> None:
    """Programme principal"""
    print(f"maintenant: {datetime.datetime.today()}")
    print(f"aujourd'hui: {datetime.date.today()}")
    print(f"demain: {datetime.date.today() + datetime.timedelta(1)}")
    print(f"avant-hier: {datetime.date.today() + datetime.timedelta(-2)}")
    print(f"noel: {datetime.date(2020, 12, 25)}")
    print(f"Noel dans: {(datetime.date(2020,12,25) - datetime.date.today()).days} jours")


if __name__ == '__main__':
    main()

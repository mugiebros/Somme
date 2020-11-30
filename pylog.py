#!/usr/bin/env python3

"""
programme pour écrire un message

par austin brodeur
"""
import csv
import pyinputplus as pyip
import colorama
from colorama import Fore
import pprint
from datetime import datetime
import sys
import whoami
import re
import argparse
import os
colorama.init()
def parse_arg() -> argparse.Namespace:
    """
    créé les arguments
    :return:
    """
    parser = argparse.ArgumentParser(description="Commande pour journaliser un message -- 2020, par Austin Brodeur")
    parser.add_argument('message', help='Message à journaliser', nargs='+',default="")
    parser.add_argument('-t',choices=["n","a","e"],help="Type de log",default="")
    parser.add_argument('--type',choices=["notification","avertissement","erreur"],help="Type de log",default="notification")
    parser.add_argument('-u','--user',metavar='USER',help="Nom de l'utilisateur",default=os.getlogin())

    args = parser.parse_args()
    return args

def main() -> None:
    datalog = ['dateheure', 'logtype', 'message', 'utilisateur']
    loghoy = ""
    data = ""
    if len(sys.argv[1:]) > 0:
        if re.match(r"^['A-Za-z0-9 _-]*['A-Za-z0-9_-]['A-Za-z0-9 _-]*$",parse_arg().user):
            now = datetime.today()
            if parse_arg().t == "":
                data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': parse_arg().type,
                        'message': " ".join(parse_arg().message),
                        'utilisateur': parse_arg().user}
            else:
                if parse_arg().t == "n":
                    loghoy = "notification"
                    data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': "notification",
                            'message': " ".join(parse_arg().message),
                            'utilisateur': parse_arg().user}
                elif parse_arg().t == "a":
                    loghoy = "avertissement"
                    data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': "avertissement",
                            'message': " ".join(parse_arg().message),
                            'utilisateur': parse_arg().user}
                elif parse_arg().t == "e":
                    loghoy = "erreur"
                    data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': "erreur",
                            'message': " ".join(parse_arg().message),
                            'utilisateur': parse_arg().user}
            pprint.pprint(data)
            try:
                with open('pylog.tsv', 'a', newline='') as tsvfile:
                    writer = csv.DictWriter(tsvfile, fieldnames=datalog,delimiter='\t')
                    if os.path.getsize('pylog.tsv') == 0:
                        writer.writeheader()
                    writer.writerow({'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': loghoy, 'message': " ".join(parse_arg().message), 'utilisateur': parse_arg().user})
            except Exception as exp:
                print(Fore.YELLOW + "[AB] " + Fore.RED + f"PermissionError " + Fore.YELLOW + f"{exp}")
        else:
            print(Fore.YELLOW + "[AB] " + Fore.RED +"ValueError"+Fore.WHITE+ "Lettres, chiffres, tirests, espaces, et apostrophes seulement dans le nom svp")
    else:
        print(Fore.YELLOW + "[AB] " + Fore.WHITE + "Svp, veuillez entrer votre message et facultativement son type et votre nom...")
        try:
            message = pyip.inputStr(prompt=Fore.BLUE + "Message: " + Fore.WHITE,limit=5)
        except  Exception as exep:
            print(Fore.YELLOW+"[AB] "+Fore.RED+f"RetryLimitException"+Fore.YELLOW+": La limite du nombre d'essais est atteinte."+Fore.WHITE)
            sys.exit(1)
        type = pyip.inputMenu(["notification","avertissement","erreur"],prompt=Fore.BLUE+"Type["+Fore.YELLOW+"1"+Fore.BLUE+"]: \n" + Fore.WHITE,default=1,limit=1,numbered=True)
        util = pyip.inputStr(prompt=Fore.BLUE + "Utilisateur ["+Fore.YELLOW+"abrodeur"+Fore.BLUE+"]: "+Fore.WHITE,
                             default= whoami,
                             limit=5,
                             blockRegexes=[("",Fore.YELLOW+ "[AB] " + Fore.WHITE + "Lettres, chiffres, tirests, espaces, et apostrophes seulement dans le nom svp")],
                             allowRegexes=[r"^['.A-Za-z0-9 _-]*['.A-Za-z0-9_-]['.A-Za-z0-9 _-]*$"])
        now = datetime.today()
        data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': type, 'message': message, 'utilisateur': util}
        pprint.pprint(data)
        try:
            with open('pylog.tsv', 'a', newline='') as tsvfile:
                writer = csv.DictWriter(tsvfile, fieldnames=datalog, delimiter='\t')
                if os.path.getsize('pylog.tsv') == 0:
                    writer.writeheader()
                writer.writerow({'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': type,
                                 'message': message, 'utilisateur': util})
        except Exception as exp :
            print(Fore.YELLOW + "[AB] " + Fore.RED +f"PermissionError "+Fore.YELLOW+ f"{exp.__cause__}")

if __name__ == '__main__':
    main()
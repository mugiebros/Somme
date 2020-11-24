#!/usr/bin/env python3

"""
programme pour écrire un message

par austin brodeur
"""
import pyinputplus as pyip
import colorama
from colorama import Fore
import pprint
from datetime import datetime
import sys
import os
colorama.init()

def main() -> None:
    print(Fore.YELLOW + "[AB] " + Fore.WHITE + "Svp, veuillez entrer votre message et facultativement son type et votre nom...")
    try:
        message = pyip.inputStr(prompt=Fore.BLUE + "Message: " + Fore.WHITE,limit=5)
    except  Exception as exep:
        print(Fore.YELLOW+"[AB] "+Fore.RED+f"RetryLimitException"+Fore.YELLOW+": La limite du nombre d'essais est atteinte."+Fore.WHITE)
        sys.exit(1)
    type = pyip.inputMenu(["notification","avertissement","erreur"],prompt=Fore.BLUE+"Type["+Fore.YELLOW+"1"+Fore.BLUE+"]: \n" + Fore.WHITE,default=1,limit=1,numbered=True)
    util = pyip.inputStr(prompt=Fore.BLUE + "Utilisateur ["+Fore.YELLOW+"abrodeur"+Fore.BLUE+"]: "+Fore.WHITE,
                         default="abrodeur",
                         limit=5,
                         blockRegexes=[("",Fore.YELLOW+ "[AB] " + Fore.WHITE + "Lettres, chiffres, tirests, espaces, et apostrophes seulement dans le nom svp")],
                         allowRegexes=[r"^['A-Za-z0-9 _-]*['A-Za-z0-9_-]['A-Za-z0-9 _-]*$"])
    now = datetime.today()
    data = {'dateheure': now.strftime("%Y/%m/%d %H:%M:%S"), 'logtype': type, 'message': message, 'utilisateur': util}
    pprint.pprint(data)

if __name__ == '__main__':
    main()
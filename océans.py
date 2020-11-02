#!/usr/bin/env python3

"""
programme pour écrire

Austin Brodeur
"""

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]

with open("océans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

with open("océans.txt", "a") as f:
    print(23 * "=", file=f)
    print("These are the 5 oceans.", file=f)

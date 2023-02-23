"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

import requests
import bs4
import sys

print(sys.argv)

if len(sys.argv) != 3:
    print("Zadej tri funkce")

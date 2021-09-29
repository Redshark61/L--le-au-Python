#coding: utf-8
import json
import colorama
from colorama import Fore, Back, Style
from os import system
from map.displayMap import displayMap


def map():
    colorama.init(autoreset=True)

    def clear(): return system('clear')

    # Récupérer la map et les coordonnées
    with open('data/map.json') as file:
        data = json.load(file)

    with open('data/coordinates.json') as file:
        coord = json.load(file)

    displayMap(data, coord)

    print('')
    userInput = input("Où souhaites-tu aller (nord, sud, est, oust): \n")

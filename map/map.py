#coding: utf-8
import json
import colorama
from colorama import Fore, Back, Style
from os import system
from map.displayMap import displayMap


def map():
    colorama.init(autoreset=True)

    def cls(): return system('cls')

    # Récupérer la map et les coordonnées
    with open('data/map.json') as file:
        data = json.load(file)

    with open('data/coordinates.json') as file:
        coord = json.load(file)

    playerX = coord['player']["coords"][0]
    playerY = coord['player']["coords"][1]

    print('')
    keepGoing = True

    west = ['OUEST', 'WEST', 'W', 'O']
    north = ['NORTH', 'NORD', 'N']
    south = ['SOUTH', 'SUD', 'S']
    east = ['EAST', 'EST', 'E']
    stop = ['STOP', 'EXIT', 'CLS']

    while keepGoing:

        # cls()
        displayMap(data, coord, playerX, playerY)
        userInput = input("Où souhaites-tu aller (nord, sud, est, oust): \n")
        if userInput.upper() in north:
            playerY -= 1
        elif userInput.upper() in south:
            playerY += 1
        elif userInput.upper() in east:
            playerX += 1
        elif userInput.upper() in west:
            playerX -= 1
        elif userInput.upper() in stop:
            keepGoing = False

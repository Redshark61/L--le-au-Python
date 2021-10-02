# coding: utf-8
from functions.Clear import clear
import json
from os import system
from map.displayMap import displayMap
import msvcrt


def map():

    def cls(): return system('cls')

    cls()

    # Récupérer la map et les coordonnées
    with open('data/map.json') as file:
        data = json.load(file)

    with open('data/coordinates.json') as file:
        coord = json.load(file)

    playerX = coord['player']["coords"][0]
    playerY = coord['player']["coords"][1]

    print('')
    char = ' '

    while ord(char) != 113:

        displayMap(data, coord, playerX, playerY)

        if msvcrt.kbhit:
            char = msvcrt.getch()

        if ord(char) == 72:
            playerY -= 1
        elif ord(char) == 80:
            playerY += 1
        elif ord(char) == 75:
            playerX -= 1
        elif ord(char) == 77:
            playerX += 1

    clear()

import colorama
from colorama import Fore, Back, Style
import os
import json


def displayMap(data, coord, playerX, playerY):

    os.system('')

    colors = {
        "brightGray": "\033[100m",
        "brightCyan": "\033[106m",
        "darkBlue": "\033[44m",
        "brightYellow": "\033[103m",
        "brightGreen": "\033[102m",
        "darkGray": "\033[42m",
        "red": "\033[91m",
        "endFor": "\033[39m",
        "endBack": "\033[49m"
    }

    # On remonte le curseur de la taille de la map + la où est le curseur acutellement
    print((len(data)+3) * "\033[A", end="")

    row = 0
    map = ''
    # Pour chaque ligne dans le json de la carte
    for i in data:
        col = 0

        # Pour chaque case dans le json de la carte
        for j in i:
            # Le caractère de base est 2 espaces
            char = '\u0020\u0020'

            # Si le coordonnée actuel est une coord de quête, alors on met une croix et pas un espace
            for item in coord:

                if item != "player":
                    if row == coord[item]['coords'][1] and col == coord[item]['coords'][0]:
                        symbol = coord[item]['mark'] + '\u0020'
                        char = colors['red']+symbol+colors['endFor']
                else:
                    if row == playerY and col == playerX:
                        symbol = coord["player"]['mark'] + '\u0020'
                        char = colors['red']+symbol+colors['endFor']

            # En fonction du code couleur de la case, on change le background
            if j == 1:
                map += colors["brightGray"] + char + colors["endBack"]
            elif j == 2:
                map += colors['brightCyan'] + char + colors["endBack"]
            elif j == 3:
                map += colors['darkBlue'] + char + colors["endBack"]
            elif j == 4:
                map += colors['brightYellow'] + char + colors["endBack"]
            elif j == 5:
                map += colors['brightGreen'] + char + colors["endBack"]
            elif j == 6:
                map += colors['darkGray'] + char + colors["endBack"]

            col += 1

        row += 1
        map += '\n'
    print(map)

import colorama
from colorama import Fore, Back, Style
import sys


def displayPlayer(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


def displayMap(data, coord, playerX, playerY):
    row = 0
    # Pour chaque ligne dans le json de la carte
    for index, i in enumerate(data):
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
                        char = Fore.RED+symbol
                else:
                    if row == playerY and col == playerX:
                        symbol = coord["player"]['mark'] + '\u0020'
                        char = Fore.RED+symbol

            # En fonction du code couleur de la case, on change le background
            if j == 1:
                print(Back.LIGHTBLACK_EX + char, end="", flush=True)
            elif j == 2:
                print(Back.LIGHTBLUE_EX + char, end="", flush=True)
            elif j == 3:
                print(Back.CYAN + char, end="", flush=True)
            elif j == 4:
                print(Back.YELLOW + char, end="", flush=True)
            elif j == 5:
                print(Back.GREEN + char, end="", flush=True)
            elif j == 6:
                print(Back.LIGHTGREEN_EX + char, end="", flush=True)

            col += 1

        row += 1
        if index > len(data) - 1:
            print('', end='\r')
        else:
            print('\r')

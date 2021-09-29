import json
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Récupérer la map et les coordonnées
with open('data/map.json') as file:
    data = json.load(file)

with open('data/coordinates.json') as file:
    coord = json.load(file)

# Mettre une ligne bleue à la fin en haut de la carte
for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')
row = 0

# Pour chaque ligne dans le json de la carte
for i in data:
    col = 0

    # Mettre du bleu au début de chaque ligne
    print(Back.CYAN + "\u0020\u0020", end="")

    # Pour chaque case dans le json de la carte
    for j in i:
        # Le caractère de base est 2 espaces
        char = '\u0020\u0020'

        # Si le coordonnée actuel est une coord de quête, alors on met une croix et pas un espace
        if row == coord['quest1'][1] and col == coord['quest1'][0]:
            char = 'X '

        # En fonction du code couleur de la case, on change le background
        if j == 1:
            print(Back.LIGHTBLACK_EX + char, end="")
        elif j == 2:
            print(Back.LIGHTBLUE_EX + char, end="")
        elif j == 3:
            print(Back.CYAN + char, end="")
        elif j == 4:
            print(Back.YELLOW + char, end="")
        elif j == 5:
            print(Back.GREEN + char, end="")
        elif j == 6:
            print(Back.LIGHTGREEN_EX + char, end="")

        col += 1

    row += 1
    print(Back.CYAN + char, end="")
    print('')

# On fini par une ligne bleue
for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')

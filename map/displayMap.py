import colorama
from colorama import Fore, Back, Style


def displayMap(data, coord):

    row = 0
    # Pour chaque ligne dans le json de la carte
    for i in data:
        col = 0

        # Pour chaque case dans le json de la carte
        for j in i:
            # Le caractère de base est 2 espaces
            char = '\u0020\u0020'

            # Si le coordonnée actuel est une coord de quête, alors on met une croix et pas un espace
            for quest in coord:

                if row == coord[quest]['coords'][1] and col == coord[quest]['coords'][0]:
                    emo = coord[quest]['mark'] + '\u0020'
                    char = Fore.RED+emo

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
        print('')

from functions.Colors import Colors
from functions.Position import *
from map.startQuest import startQuest
from map.emojiDecoder import emojiDecoder
import time


def displayMap(data: dict, coord: dict, playerX: int, playerY: int, questToDo: list, questDone: list) -> None:
    """
    Display the map using the map.json. Each number is for a particular color. By default, the characters are just 2 spaces
    but it can be emoji.

    It also stores the different quest already done, and handle if it needs to be done or not.
    """

    color = Colors
    color.init()

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

            # Si les coordonnés actuel sont une quête, mettre une coche verte si elle est faite
            if len(questDone) > 0:
                for quest in questDone:
                    if row == quest[1] and col == quest[0]:
                        char = emojiDecoder("e29c85")

            # Pour chaque position dans le json de coordonnés
            for item in coord:

                # Toutes les icônes doivent être converties de hex en string lisible par le terminal
                symbol = emojiDecoder(coord[item]['mark'])

                # Si ce n'est pas un joueur, on vérifie si la boucle affiche les coordonnés d'une position du json
                if item != "player":
                    if row == coord[item]['coords'][1] and col == coord[item]['coords'][0]:
                        char = symbol
                # Si c'est un joueur, on vérifie si la boucle affiche les coords du joueur
                else:
                    if row == playerY and col == playerX:
                        char = symbol

            # En fonction du code couleur de la case, on change le background
            if j == 1:
                map += color.setBackground("brightGray", char)
            elif j == 2:
                map += color.setBackground('brightCyan', char)
            elif j == 3:
                map += color.setBackground('darkBlue', char)
            elif j == 4:
                map += color.setBackground('brightYellow', char)
            elif j == 5:
                if row == playerY and col == playerX:
                    map += color.setBackground('darkGray', char)
                else:
                    map += color.setBackground('darkGray', emojiDecoder('f09f8cb4'))
            elif j == 6:
                map += color.setBackground('darkGray', char)

            col += 1

        row += 1
        map += '\n'
    print(map)
    for index, quest in enumerate(questToDo):
        quest = list(quest.keys())[0]
        if (playerY == questToDo[index][quest][1] and playerX == questToDo[index][quest][0]):
            questToDo, playerX = startQuest(coord, index, questToDo, playerX, playerY, quest, questDone)
            return questToDo, playerX
    return questToDo, playerX

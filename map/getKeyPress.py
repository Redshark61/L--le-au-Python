import msvcrt
from functions.Position import position
from map.displayMap import displayMap
from functions.emojiDecoder import emojiDecoder
from map.map import drawEnergy
from typing import Union
from functions.gainEnergy import gainEnergy
from functions.drawFood import drawFood
from functions.looseFood import looseFood


def getKeyPress(playerCoord: list, vitalSigns: dict[int], data: dict, coord: dict, questToDo: list[list], questDone: list[list], prevPlayerCoord: list, createdItems: dict, currentItems: dict, pickedUpItem: list) -> Union[bytes, int, int, int, int, int, int]:
    # Si une touche du clavier est pressé
    if msvcrt.kbhit:
        # Récupérer cett touche
        char = msvcrt.getch()

    if ord(char) == 72:  # Up
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[1] -= 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 80:  # Down
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[1] += 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 75:  # Left
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[0] -= 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 77:  # Right
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[0] += 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 49:  # 1
        char = ' '
        print(position(105, 6, 'Je dors...'+' '*10))
        playerFace = position(playerCoord[0]*2+1, playerCoord[1]+2, emojiDecoder('f09f98b4'))
        displayMap(data, coord, playerCoord, questToDo, questDone, prevPlayerCoord, vitalSigns, createdItems, currentItems, pickedUpItem, playerFace)
        while vitalSigns["energyMax"] < 100:
            vitalSigns["energyMax"] = gainEnergy(vitalSigns["energyMax"])
            vitalSigns["foodMax"] = looseFood(vitalSigns["foodMax"])
            drawEnergy(vitalSigns["energyMax"])
            drawFood(vitalSigns["foodMax"])
        print(position(105, 6, 'Je ne dors plus !'))

    return char, prevPlayerCoord, playerCoord, vitalSigns, currentItems, pickedUpItem

import msvcrt
from functions.Position import position
from map.displayMap import displayMap
from functions.emojiDecoder import emojiDecoder
from map.map import drawEnergy
from typing import Union
from functions.gainEnergy import gainEnergy
from functions.drawFood import drawFood
from functions.looseFood import looseFood
from collections import Counter
from map.inventory import inventory


def getKeyPress(inventoryOpen: bool, playerCoord: list, vitalSigns: dict[int], data: dict, coord: dict, questToDo: list[list], questDone: list[list], prevPlayerCoord: list, createdItems: dict, currentItems: dict, pickedUpItem: list, itemSelected: int, widthOfName: int, currentPosition: int, noDuplicateInventory) -> Union[bytes, int, int, int, int, int, int]:
    # Si une touche du clavier est pressé
    if msvcrt.kbhit:
        # Récupérer cett touche
        char = msvcrt.getch()

    if ord(char) == 72 and not inventoryOpen:  # Up
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[1] -= 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 80 and not inventoryOpen:  # Down
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[1] += 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 75 and not inventoryOpen:  # Left
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[0] -= 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3
    elif ord(char) == 77 and not inventoryOpen:  # Right
        prevPlayerCoord[1] = playerCoord[1]
        prevPlayerCoord[0] = playerCoord[0]
        playerCoord[0] += 1
        vitalSigns["foodMax"] -= 2
        vitalSigns["waterMax"] -= 2
        vitalSigns["energyMax"] -= 3

    # * Sleep
    elif ord(char) == 49 and not inventoryOpen:  # 1
        char = ' '
        print(position(105, 6, 'Je dors...' + ' ' * 10))
        playerFace = position(playerCoord[0] * 2 + 1, playerCoord[1] + 2, emojiDecoder('f09f98b4'))
        displayMap(data, coord, playerCoord, questToDo, questDone, prevPlayerCoord, vitalSigns, createdItems, currentItems, pickedUpItem, playerFace)
        while vitalSigns["energyMax"] < 100:
            vitalSigns["energyMax"] = gainEnergy(vitalSigns["energyMax"])
            vitalSigns["foodMax"] = looseFood(vitalSigns["foodMax"])
            drawEnergy(vitalSigns["energyMax"])
            drawFood(vitalSigns["foodMax"])
        print(position(105, 6, 'Je ne dors plus !'))

    char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns = inventory(char, inventoryOpen, noDuplicateInventory, itemSelected, currentPosition, pickedUpItem, vitalSigns)

    return char, prevPlayerCoord, playerCoord, vitalSigns, currentItems, pickedUpItem, inventoryOpen, itemSelected, widthOfName, currentPosition, noDuplicateInventory

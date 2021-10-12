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


def getKeyPress(inventoryOpen: bool, playerCoord: list, vitalSigns: dict[int], data: dict, coord: dict, questToDo: list[list], questDone: list[list], prevPlayerCoord: list, createdItems: dict, currentItems: dict, pickedUpItem: list, itemSelected: int, widthOfName: int, currentPosition: int) -> Union[bytes, int, int, int, int, int, int]:
    # Si une touche du clavier est pressé
    if msvcrt.kbhit:
        # Récupérer cett touche
        char = msvcrt.getch()

    # seen = set()
    # noDuplicateInventory = []
    # for d in pickedUpItem:
    #     t = tuple(d.items())
    #     if t not in seen:
    #         seen.add(t)
    #         noDuplicateInventory.append(d)
    noDuplicateInventory = Counter(item['name'] for item in pickedUpItem)
    noDuplicateInventory = [i for i in [*noDuplicateInventory.keys()]]

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

    # * Open inventory
    elif ord(char) == 50 and not inventoryOpen:  # ord(char) = 50 -> 2
        itemSelected = 0
        widthOfName = len(noDuplicateInventory[itemSelected])
        currentPosition = 3
        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
        inventoryOpen = True

    elif ord(char) == 77 and inventoryOpen:

        itemSelected += 1
        prevWidth = len(noDuplicateInventory[itemSelected-1])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))
        widthOfName = len(noDuplicateInventory[itemSelected])

        print(position(1, 1, f"{widthOfName}   "))

        currentPosition += prevWidth+5

        print(position(20, 1, f" = {str(currentPosition)}   "))

        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    elif ord(char) == 75 and inventoryOpen:

        itemSelected -= 1
        prevWidth = len(noDuplicateInventory[itemSelected])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))

        widthOfName = len(noDuplicateInventory[itemSelected])

        currentPosition = currentPosition-(widthOfName+5)

        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    # * Close inventory
    elif ord(char) == 50 and inventoryOpen:
        inventoryOpen = False
        currentPosition = 3
        print(position(3, 37, " "*20))

    return char, prevPlayerCoord, playerCoord, vitalSigns, currentItems, pickedUpItem, inventoryOpen, itemSelected, widthOfName, currentPosition

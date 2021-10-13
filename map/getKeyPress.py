import msvcrt
from typing import Union
from functions.Position import position
from map.displayMap import displayMap
from functions.emojiDecoder import emojiDecoder
from map.map import drawEnergy
from functions.gainEnergy import gainEnergy
from functions.drawFood import drawFood
from functions.looseFood import looseFood
from map.inventory import inventory
from functions import config


def getKeyPress(inventoryOpen: bool, noDuplicateInventory) -> Union[bytes, int, int, int, int, int, int]:
    # Si une touche du clavier est pressé
    if msvcrt.kbhit:
        # Récupérer cett touche
        config.char = msvcrt.getch()

    if ord(config.char) == 72 and not inventoryOpen:  # Up
        config.prevPlayerCoord[1] = config.playerCoord[1]
        config.prevPlayerCoord[0] = config.playerCoord[0]
        config.playerCoord[1] -= 1
        config.vitalSigns["foodMax"] -= 2
        config.vitalSigns["waterMax"] -= 2
        config.vitalSigns["energyMax"] -= 3
    elif ord(config.char) == 80 and not inventoryOpen:  # Down
        config.prevPlayerCoord[1] = config.playerCoord[1]
        config.prevPlayerCoord[0] = config.playerCoord[0]
        config.playerCoord[1] += 1
        config.vitalSigns["foodMax"] -= 2
        config.vitalSigns["waterMax"] -= 2
        config.vitalSigns["energyMax"] -= 3
    elif ord(config.char) == 75 and not inventoryOpen:  # Left
        config.prevPlayerCoord[1] = config.playerCoord[1]
        config.prevPlayerCoord[0] = config.playerCoord[0]
        config.playerCoord[0] -= 1
        config.vitalSigns["foodMax"] -= 2
        config.vitalSigns["waterMax"] -= 2
        config.vitalSigns["energyMax"] -= 3
    elif ord(config.char) == 77 and not inventoryOpen:  # Right
        config.prevPlayerCoord[1] = config.playerCoord[1]
        config.prevPlayerCoord[0] = config.playerCoord[0]
        config.playerCoord[0] += 1
        config.vitalSigns["foodMax"] -= 2
        config.vitalSigns["waterMax"] -= 2
        config.vitalSigns["energyMax"] -= 3

    # * Sleep
    elif ord(config.char) == 49 and not inventoryOpen:  # 1
        config.char = ' '
        print(position(105, 6, 'Je dors...' + ' ' * 10))
        playerFace = position(config.playerCoord[0] * 2 + 1, config.playerCoord[1] + 2, emojiDecoder('f09f98b4'))
        displayMap(playerFace)
        while config.vitalSigns["energyMax"] < 100:
            config.vitalSigns["energyMax"] = gainEnergy(config.vitalSigns["energyMax"])
            config.vitalSigns["foodMax"] = looseFood(config.vitalSigns["foodMax"])
            drawEnergy(config.vitalSigns["energyMax"])
            drawFood(config.vitalSigns["foodMax"])
        print(position(105, 6, 'Je ne dors plus !'))

    inventoryOpen = inventory(inventoryOpen, noDuplicateInventory)

    return inventoryOpen, noDuplicateInventory

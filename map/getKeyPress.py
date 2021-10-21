import msvcrt
from typing import Union
from functions.Position import position
from map.displayMap import displayMap
from functions.emojiDecoder import emojiDecoder
from map.mapLoop import drawEnergy
from functions.gainEnergy import gainEnergy
from functions.drawHealth import drawFood
from functions.looseFood import looseFood
from map.inventory import inventory
from functions import config
from map.movement import movement


def getKeyPress(inventoryOpen: bool, noDuplicateInventory: list[tuple]) -> Union[bool, list[tuple]]:
    """
    Handle all of the keypress.
    """
    # If a key is pressed
    if msvcrt.kbhit:
        # Get that key
        config.char = msvcrt.getch()

    # * Movement
    if ord(config.char) == 72 and not inventoryOpen:  # Up
        movement(y=-1)
    elif ord(config.char) == 80 and not inventoryOpen:  # Down
        movement(y=1)
    elif ord(config.char) == 75 and not inventoryOpen:  # Left
        movement(x=-1)
    elif ord(config.char) == 77 and not inventoryOpen:  # Right
        movement(x=1)

    # * Sleep
    elif ord(config.char) == 49 and not inventoryOpen:  # 1
        config.char = ' '
        print(position(105, 9, 'Je dors...' + ' ' * 10))
        playerFace = position(config.playerCoord[0] * 2 + 1, config.playerCoord[1] + 1, emojiDecoder('f09f98b4'))
        displayMap(playerFace)
        while config.vitalSigns["energyMax"] < config.energyMax and config.vitalSigns['foodMax'] > 20:
            config.vitalSigns["energyMax"] = gainEnergy(config.vitalSigns["energyMax"])
            config.vitalSigns["foodMax"] = looseFood(config.vitalSigns["foodMax"])
            drawEnergy(config.vitalSigns["energyMax"])
            drawFood(config.vitalSigns["foodMax"])
        if config.vitalSigns['energyMax'] > config.energyMax:
            config.vitalSigns['energyMax'] = config.energyMax
        print(position(105, 9, 'Je ne dors plus !'))

    inventoryOpen = inventory(inventoryOpen, noDuplicateInventory)

    return inventoryOpen, noDuplicateInventory

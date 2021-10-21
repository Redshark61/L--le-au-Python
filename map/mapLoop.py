# coding: utf-8
import json
import time
import copy
from collections import Counter
from datetime import datetime
from functions.Clear import clear
from functions.drawRightPanel import drawRightPanel
from functions.emojiDecoder import emojiDecoder
from map.displayMap import displayMap
from functions.Position import position, printBox
from functions.checkMod import checkMod
from functions.drawHealth import drawFood, drawWater, drawEnergy
from map.getKeyPress import getKeyPress
from map.closeInventory import closeInventory
from functions import config
from functions.saveFunctions.checkSave import checkSave
from map.displayKey import displayKey
from map.finalTrailer import finalTrailer


def mapLoop(saveName) -> None:

    clear()
    checkSave(saveName)
    config.saveName = saveName

    # Get the json map
    config.data = checkMod('map')

    # Previous coords are a deepcopy of the current coords
    config.prevPlayerCoord = copy.deepcopy(config.playerCoord)

    inventoryOpen = False

    # Print the right and bottom panel, and the vital sign (food, water, energy)
    printBox(103, 1, 50, 38)
    printBox(1, 30, 101, 9)
    drawFood(config.vitalSigns["foodMax"])
    drawWater(config.vitalSigns["waterMax"])
    drawEnergy(config.vitalSigns["energyMax"])
    print(position(3, 34, '-'*98))
    drawRightPanel()

    # While the 'q' letter is not pressed
    while ord(config.char) != 113:

        # Display the map
        isQuestDone = displayMap()
        # Display the key (if there are)
        displayKey()

        # Leave the game if the player is on the lock
        if config.isLeaving:
            finalTrailer()
            return

        # Refresh if the player just did a quest
        if isQuestDone:
            displayMap()
            isQuestDone = False

        # If the inventory is empty, empty everything
        inventoryX = 3
        if len(config.pickedUpItem) == 0:
            inventoryOpen = closeInventory(inventoryOpen)
            noDuplicateInventory = []
            numbersOfItem = []
        else:
            # Get the number of each item in the list of dict pickedUpItem
            numbersOfItem = Counter(item['name'] for item in config.pickedUpItem)
            print(position(3, 35, ' '*40))
            print(position(3, 36, ' '*40))
            # Convert into list of tuples
            listOfTuple = [*numbersOfItem.items()]
            listOfTuple.sort(key=lambda x: x[0])
            # Print each item above its number
            for key, value in listOfTuple:
                print(position(inventoryX, 35, key))
                print(position(inventoryX, 36, str(value).center(len(key), ' ')))
                inventoryX += len(key) + 5
                noDuplicateInventory = listOfTuple

        # Get the key press
        inventoryOpen, noDuplicateInventory = getKeyPress(inventoryOpen, noDuplicateInventory)

        drawFood(config.vitalSigns["foodMax"])
        drawWater(config.vitalSigns["waterMax"])
        drawEnergy(config.vitalSigns["energyMax"])

        # Conditions to die
        if config.vitalSigns["foodMax"] <= 0 or config.vitalSigns["waterMax"] <= 0 or config.vitalSigns["energyMax"] <= 0:
            print(position(105, 10, 'Vous êtes mort !'))
            playerFace = position(config.playerCoord[0]*2+1, config.playerCoord[1]+1, emojiDecoder('f09f9280'))
            displayMap(playerFace)
            time.sleep(5)
            return

        save(saveName)

    return


def save(saveName):
    today = datetime.now()

    with open(saveName, encoding='utf-8') as f:
        savedData = json.load(f)
    # Save everything into the file
    savedData['playerCoord'] = config.playerCoord
    savedData['currentDate'] = today.strftime("%d/%m/%Y %H:%M:%S")
    savedData['key'] = config.key
    savedData['health'] = config.vitalSigns
    savedData['inventory'] = config.pickedUpItem
    savedData['itemPosition'] = config.createdItems
    savedData['currentItems'] = config.currentItems
    savedData['questDone'] = config.questDone
    savedData['questToDo'] = config.questToDo
    savedData['inventorySize'] = config.inventorySize
    savedData['playerSkinName'] = config.skinName
    savedData['playerSkinMark'] = config.playerMark

    with open(saveName, 'w', encoding='utf-8') as f:
        json.dump(savedData, f, indent=4)

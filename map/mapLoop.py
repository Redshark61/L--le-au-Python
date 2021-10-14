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


def mapLoop(saveName) -> None:

    clear()

    checkSave(saveName)

    # Récupérer la map
    config.data = checkMod('map')

    config.prevPlayerCoord = copy.deepcopy(config.playerCoord)

    print('')
    # global char
    inventoryOpen = False

    printBox(103, 1, 50, 38)
    printBox(1, 30, 101, 9)

    drawFood(config.vitalSigns["foodMax"])
    drawWater(config.vitalSigns["waterMax"])
    drawEnergy(config.vitalSigns["energyMax"])
    print(position(3, 34, '-'*98))
    drawRightPanel()
    # Tant que le code de la touche pressé n'est pas 113 (q)
    while ord(config.char) != 113:

        # Afficher la carte
        isQuestDone = displayMap()

        if isQuestDone:
            displayMap()
            isQuestDone = False

        inventoryX = 3
        if len(config.pickedUpItem) == 0:
            inventoryOpen = closeInventory(inventoryOpen)
            noDuplicateInventory = []
            numbersOfItem = []
        else:
            print(position(1, 1, ' '*40))
            numbersOfItem = Counter(item['name'] for item in config.pickedUpItem)
            print(position(3, 35, ' '*40))
            print(position(3, 36, ' '*40))
            listOfTuple = [*numbersOfItem.items()]
            listOfTuple.sort(key=lambda x: x[0])
            for key, value in listOfTuple:
                print(position(inventoryX, 35, key))
                print(position(inventoryX, 36, str(value).center(len(key), ' ')))
                inventoryX += len(key) + 5
                noDuplicateInventory = listOfTuple

        inventoryOpen, noDuplicateInventory = getKeyPress(inventoryOpen, noDuplicateInventory)
        drawFood(config.vitalSigns["foodMax"])
        drawWater(config.vitalSigns["waterMax"])
        drawEnergy(config.vitalSigns["energyMax"])

        if config.vitalSigns["foodMax"] <= 0 or config.vitalSigns["waterMax"] <= 0 or config.vitalSigns["energyMax"] <= 0:
            print(position(105, 10, 'Vous êtes mort !'))
            playerFace = position(config.playerCoord[0]*2+1, config.playerCoord[1]+2, emojiDecoder('f09f9280'))
            displayMap(playerFace)
            time.sleep(5)
            return

    save(saveName)

    return


def save(saveName):
    today = datetime.now()

    with open(saveName, encoding='utf-8') as f:
        savedData = json.load(f)

    savedData['playerCoord'] = config.playerCoord
    savedData['currentDate'] = today.strftime("%d/%m/%Y %H:%M:%S")
    savedData['key'] = config.key
    savedData['health'] = config.vitalSigns
    savedData['inventory'] = config.pickedUpItem
    savedData['itemPosition'] = config.createdItems
    savedData['currentItems'] = config.currentItems
    savedData['questDone'] = config.questDone
    savedData['questToDo'] = config.questToDo

    with open(saveName, 'w', encoding='utf-8') as f:
        json.dump(savedData, f, indent=4)

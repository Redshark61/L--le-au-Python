# coding: utf-8
import time
import copy
from collections import Counter
from functions.Clear import clear
from functions.emojiDecoder import emojiDecoder
from map.displayMap import displayMap
from functions.Position import position, printBox
from functions.checkMod import checkMod
from functions.drawFood import drawFood
from functions.drawWater import drawWater
from functions.drawEnergy import drawEnergy
from map.getKeyPress import getKeyPress
from map.randomItemPosition import randomItemPosition
from map.closeInventory import closeInventory
import functions.config as config


def map() -> None:

    clear()

    # Récupérer la map
    config.data = checkMod('map')

    # Récupérer les coordonnés
    config.coord = checkMod('coordinates')

    config.createdItems, config.currentItems = randomItemPosition()
    config.pickedUpItem = []

    # Coordonnés du joueur
    config.playerCoord.append(config.coord['player']["coords"][0])
    config.playerCoord.append(config.coord['player']["coords"][1])
    config.prevPlayerCoord = copy.deepcopy(config.playerCoord)

    print('')
    # global char
    config.questToDo = []
    config.questDone = []
    inventoryOpen = False

    printBox(103, 1, 50, 38)
    printBox(1, 30, 101, 9)

    for quest in config.coord:
        if quest != 'player':
            config.questToDo.append({quest: config.coord[quest]['coords']})

    drawFood(config.vitalSigns["foodMax"])
    drawWater(config.vitalSigns["waterMax"])
    drawEnergy(config.vitalSigns["energyMax"])
    print(position(3, 34, '-'*98))
    print(position(105, 2, "L'île aux Pythons !".center(47, ' ')))
    print(position(105, 3, "-"*47))
    print(position(105, 4, "1 - Dormir"))
    print(position(105, 5, " "*40))
    print(position(105, 5, "2 - Ouvrir Inventaire"))

    # Tant que le code de la touche pressé n'est pas 113 (q)
    while ord(config.char) != 113:

        # Afficher la carte
        isQuestDone = displayMap()

        drawFood(config.vitalSigns["foodMax"])
        drawWater(config.vitalSigns["waterMax"])
        drawEnergy(config.vitalSigns["energyMax"])
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

        if config.vitalSigns["foodMax"] < 0 or config.vitalSigns["waterMax"] < 0 or config.vitalSigns["energyMax"] < 0:
            print(position(105, 10, 'Vous êtes mort !'))
            playerFace = position(config.playerCoord[0]*2+1, config.playerCoord[1]+2, emojiDecoder('f09f9280'))
            displayMap(playerFace)
            time.sleep(5)
            return

    return

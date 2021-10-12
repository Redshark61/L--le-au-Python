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


def map() -> None:

    clear()

    # Récupérer la map
    data = checkMod('map')

    # Récupérer les coordonnés
    coord = checkMod('coordinates')

    createdItems, currentItems = randomItemPosition()
    pickedUpItem = []

    # Coordonnés du joueur
    playerCoord = []
    playerCoord.append(coord['player']["coords"][0])
    playerCoord.append(coord['player']["coords"][1])
    prevPlayerCoord = copy.deepcopy(playerCoord)

    print('')
    char = ' '
    questToDo = []
    questDone = []
    inventoryOpen = False
    itemSelected, toBePosition, currentPosition = 0, 0, 0
    noDuplicateInventory = []

    printBox(103, 1, 50, 38)
    printBox(1, 30, 101, 9)
    vitalSigns = {
        "energyMax": 100,
        "foodMax": 100,
        "waterMax": 100
    }

    for quest in coord:
        if quest != 'player':
            questToDo.append({quest: coord[quest]['coords']})

    drawFood(vitalSigns["foodMax"])
    drawWater(vitalSigns["waterMax"])
    drawEnergy(vitalSigns["energyMax"])
    print(position(3, 34, '-'*98))
    print(position(105, 2, "L'île aux Pythons !".center(47, ' ')))
    print(position(105, 3, "-"*47))
    print(position(105, 4, "1 - Dormir"))
    print(position(105, 5, " "*40))
    print(position(105, 5, "2 - Ouvrir Inventaire"))

    # Tant que le code de la touche pressé n'est pas 113 (q)
    while ord(char) != 113:

        # Afficher la carte
        questToDo, playerCoord, isQuestDone, vitalSigns, currentItems, pickedUpItem = displayMap(
            data, coord, playerCoord, questToDo, questDone, prevPlayerCoord, vitalSigns, createdItems, currentItems, pickedUpItem)

        drawFood(vitalSigns["foodMax"])
        drawWater(vitalSigns["waterMax"])
        drawEnergy(vitalSigns["energyMax"])
        if isQuestDone:
            displayMap(data, coord, playerCoord, questToDo, questDone, prevPlayerCoord, vitalSigns, createdItems, currentItems, pickedUpItem)
            isQuestDone = False

        inventoryX = 3
        if len(pickedUpItem) == 0:
            char, inventoryOpen, currentPosition = closeInventory(char, inventoryOpen, currentPosition)
            noDuplicateInventory = []
            numbersOfItem = []
        else:
            print(position(1, 1, ' '*40))
            numbersOfItem = Counter(item['name'] for item in pickedUpItem)
            print(position(3, 35, ' '*40))
            print(position(3, 36, ' '*40))
            listOfTuple = [*numbersOfItem.items()]
            listOfTuple.sort(key=lambda x: x[0])
            for key, value in listOfTuple:
                print(position(inventoryX, 35, key))
                print(position(inventoryX, 36, str(value).center(len(key), ' ')))
                inventoryX += len(key) + 5
                noDuplicateInventory = listOfTuple

        # We get a dict wich store how many time there is each item
        # noDuplicateInventory = Counter(item['name'] for item in pickedUpItem)
        # We just get the keys

        char, prevPlayerCoord, playerCoord, vitalSigns, currentItems, pickedUpItem, inventoryOpen, itemSelected, toBePosition, currentPosition, noDuplicateInventory = getKeyPress(inventoryOpen,
                                                                                                                                                                                   playerCoord, vitalSigns, data, coord, questToDo, questDone, prevPlayerCoord, createdItems, currentItems, pickedUpItem, itemSelected, toBePosition, currentPosition, noDuplicateInventory)

        if vitalSigns["foodMax"] < 0 or vitalSigns["waterMax"] < 0 or vitalSigns["energyMax"] < 0:
            print(position(105, 10, 'Vous êtes mort !'))
            playerFace = position(playerCoord[0]*2+1, playerCoord[1]+2, emojiDecoder('f09f9280'))
            displayMap(data, coord, playerCoord, questToDo, questDone, prevPlayerCoord, vitalSigns, createdItems, currentItems, pickedUpItem, playerFace)
            time.sleep(5)
            return

    return

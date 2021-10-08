# coding: utf-8
import time
from functions.Clear import clear
from functions.emojiDecoder import emojiDecoder
from map.displayMap import displayMap
from functions.Position import position, printBox
from functions.checkMod import checkMod
from functions.drawFood import drawFood
from functions.drawWater import drawWater
from functions.drawEnergy import drawEnergy
from map.getKeyPress import getKeyPress
import random


def map() -> None:

    clear()

    # Récupérer la map
    data = checkMod('map')

    # Récupérer les coordonnés
    coord = checkMod('coordinates')

    items = checkMod("items")

    createdItems = []
    currentItems = items

    for item in currentItems:
        for i in range(currentItems[item]["number"]):
            if currentItems[item]['spawn'] == "generic":
                itemPosX = random.randint(10, 80)
                itemPosY = random.randint(9, 20)
                createdItems.append({item: [itemPosX, itemPosY]})

    # Coordonnés du joueur
    playerX = coord['player']["coords"][0]
    playerY = coord['player']["coords"][1]
    prevPlayerY = playerY
    prevPlayerX = playerX

    print('')
    char = ' '
    questToDo = []
    questDone = []

    printBox(103, 1, 50, 38)
    printBox(1, 30, 101, 9)
    energyMax, foodMax, waterMax = 100, 100, 100

    for quest in coord:
        if quest != 'player':
            questToDo.append({quest: coord[quest]['coords']})

    drawFood(foodMax)
    drawWater(waterMax)
    drawEnergy(energyMax)
    print(position(3, 34, '-'*98))

    # Tant que le code de la touche pressé n'est pas 113 (q)
    while ord(char) != 113:

        # Afficher la carte
        questToDo, playerX, playerY, isQuestDone, foodMax, waterMax, currentItems = displayMap(
            data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY, foodMax, waterMax, createdItems, currentItems)
        drawFood(foodMax)
        drawWater(waterMax)
        drawEnergy(energyMax)
        if isQuestDone:
            displayMap(data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY, foodMax, waterMax, createdItems, currentItems)
            isQuestDone = False

        print(position(105, 2, "L'île aux Python !".center(47, ' ')))
        print(position(105, 3, "-"*47))
        print(position(105, 4, "1 - Dormir"))

        char, prevPlayerX, prevPlayerY, playerX, playerY, energyMax, foodMax, waterMax, currentItems = getKeyPress(
            playerX, playerY, foodMax, waterMax, energyMax, data, coord, questToDo, questDone, prevPlayerX, prevPlayerY, createdItems, currentItems)

        if foodMax < 0 or waterMax < 0 or energyMax < 0:
            print(position(105, 10, 'Vous êtes mort !'))
            playerFace = position(playerX*2+1, playerY+2, emojiDecoder('f09f9280'))
            displayMap(data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY,  foodMax, waterMax, createdItems, currentItems, playerFace)
            time.sleep(5)
            return

    return

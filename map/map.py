# coding: utf-8
from functions.Clear import clear
from map.displayMap import displayMap
import msvcrt
from functions.Position import position, printBox
from functions.checkMod import checkMod


def map() -> None:

    clear()

    # Récupérer la map
    data = checkMod('map')

    # Récupérer les coordonnés
    coord = checkMod('coordinates')

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
    for quest in coord:
        if quest != 'player':
            questToDo.append({quest: coord[quest]['coords']})

    # Tant que le code de la touche pressé n'est pas 113 (q)
    while ord(char) != 113:

        # Afficher la carte
        questToDo, playerX, playerY, isQuestDone = displayMap(data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY)
        if isQuestDone:
            displayMap(data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY)
            isQuestDone = False

        print(position(105, 2, "C'est la carte, c'est la carte..."))

        # Si une touche du clavier est pressé
        if msvcrt.kbhit:
            # Récupérer cett touche
            char = msvcrt.getch()

        if ord(char) == 72:  # Up
            prevPlayerY = playerY
            prevPlayerX = playerX
            playerY -= 1
        elif ord(char) == 80:  # Down
            prevPlayerY = playerY
            prevPlayerX = playerX
            playerY += 1
        elif ord(char) == 75:  # Left
            prevPlayerY = playerY
            prevPlayerX = playerX
            playerX -= 1
        elif ord(char) == 77:  # Right
            prevPlayerY = playerY
            prevPlayerX = playerX
            playerX += 1

    clear()

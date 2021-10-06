# coding: utf-8
from functions.Clear import clear
import json
from os import system
from map.displayMap import displayMap
import msvcrt
from functions.Position import position, printBox


def map() -> None:

    clear()

    # Récupérer la map
    with open('data/map.json') as file:
        data = json.load(file)

    # Récupérer les coordonnés
    with open('data/coordinates.json') as file:
        coord = json.load(file)

    # Coordonnés du joueur
    playerX = coord['player']["coords"][0]
    playerY = coord['player']["coords"][1]

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
        questToDo, playerX, isQuestDone = displayMap(data, coord, playerX, playerY, questToDo, questDone)
        if isQuestDone:
            displayMap(data, coord, playerX, playerY, questToDo, questDone)
            isQuestDone = False

        print(position(105, 2, "C'est la carte, c'est la carte..."))

        # Si une touche du clavier est pressé
        if msvcrt.kbhit:
            # Récupérer cett touche
            char = msvcrt.getch()

        if ord(char) == 72:  # Up
            playerY -= 1
        elif ord(char) == 80:  # Down
            playerY += 1
        elif ord(char) == 75:  # Left
            playerX -= 1
        elif ord(char) == 77:  # Right
            playerX += 1

    clear()

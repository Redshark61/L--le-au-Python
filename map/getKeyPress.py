import msvcrt
from functions.Position import position
from map.displayMap import displayMap
from functions.emojiDecoder import emojiDecoder
from map.map import drawEnergy
from typing import Union
from functions.gainEnergy import gainEnergy


def getKeyPress(playerX: int, playerY: int, foodMax: int, waterMax: int, energyMax: int, data: dict, coord: dict, questToDo: list[list], questDone: list[list], prevPlayerX: int, prevPlayerY: int, createdItems: dict, currentItems: dict, pickedUpItem: list) -> Union[bytes, int, int, int, int, int, int]:
    # Si une touche du clavier est pressé
    if msvcrt.kbhit:
        # Récupérer cett touche
        char = msvcrt.getch()

    if ord(char) == 72:  # Up
        prevPlayerY = playerY
        prevPlayerX = playerX
        playerY -= 1
        foodMax -= 2
        waterMax -= 2
        energyMax -= 3
    elif ord(char) == 80:  # Down
        prevPlayerY = playerY
        prevPlayerX = playerX
        playerY += 1
        foodMax -= 2
        waterMax -= 2
        energyMax -= 3
    elif ord(char) == 75:  # Left
        prevPlayerY = playerY
        prevPlayerX = playerX
        playerX -= 1
        foodMax -= 2
        waterMax -= 2
        energyMax -= 3
    elif ord(char) == 77:  # Right
        prevPlayerY = playerY
        prevPlayerX = playerX
        playerX += 1
        foodMax -= 2
        waterMax -= 2
        energyMax -= 3
    elif ord(char) == 49:  # 1
        char = ' '
        print(position(105, 6, 'Je dors...'+' '*10))
        playerFace = position(playerX*2+1, playerY+2, emojiDecoder('f09f98b4'))
        displayMap(data, coord, playerX, playerY, questToDo, questDone, prevPlayerX, prevPlayerY, foodMax, waterMax, createdItems, currentItems, pickedUpItem, playerFace)
        while energyMax < 100:
            energyMax = gainEnergy(energyMax)
            drawEnergy(energyMax)
        print(position(105, 6, 'Je ne dors plus !'))

    return char, prevPlayerX, prevPlayerY, playerX, playerY, energyMax, foodMax, waterMax, currentItems, pickedUpItem

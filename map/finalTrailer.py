import os
import time
import random
from functions.Clear import clear
from functions.checkMod import checkMod
from functions.Colors import Colors
from functions.emojiDecoder import emojiDecoder
from functions.Position import position
from functions import config


def finalTrailer():
    print(config.hiddenCursor)
    clear()
    color = Colors()
    color.init()
    mapEndData = checkMod('mapEnd')
    line = len(mapEndData)-1
    shake = False
    shakeIndex = 0
    index = 10
    for _ in range(len(mapEndData)):
        if line >= 11:
            time.sleep(0.2)
        else:
            shake = True

        if shake:
            for _ in range(50):
                time.sleep(0.15)
                shake = True
                line, shakeIndex = displayMapEnd(mapEndData, color,  line, shake, shakeIndex, index)
                shakeIndex = 0 if shakeIndex == 1 else 1
                index = 0 if index == 10 else index+1
            shake = False
            break
        else:
            line, shakeIndex = displayMapEnd(mapEndData, color,  line, shake, shakeIndex, index)

    time.sleep(1)
    Endcredits()


def displayMapEnd(mapEndData, color, line, shake, shakeIndex, index):
    mapEnd = ''
    print(position(1, 1, ''))
    for indexI, value in enumerate(mapEndData):
        if shake and shakeIndex == 0:
            mapEnd += f'{color.colorBgEnd} {color.colorBgEnd}'
        elif shake and shakeIndex == 1:
            mapEnd += ''

        for indexJ, j in enumerate(value):
            if indexI == line and indexJ == 24 and line >= 5:
                if j in ("e1", "e5"):
                    bgColor = "darkYellow"
                elif j == "e2":
                    bgColor = "brightGreen"
                elif j == "e3":
                    bgColor = "brightCyan"
                elif j == "e4":
                    bgColor = "brightYellow"
                elif j == "e6":
                    bgColor = "brightYellow"
                mapEnd += color.setBackground(bgColor, emojiDecoder("f09fa4a0"))
                line -= 1 if line > 5 and index == 10 else 0
            elif j == 'e1':
                fireCoords = randomFire(mapEndData)
                for i in fireCoords:
                    if i[0] == indexJ and i[1] == indexI:
                        fireColor = 'red'
                        break
                    fireColor = 'darkYellow'
                mapEnd += color.setBackground(fireColor, "  ")
            elif j == 'e2':
                mapEnd += color.setBackground("brightGreen", "  ")
            elif j == 'e3':
                mapEnd += color.setBackground("brightCyan", "  ")
            elif j == 'e4':
                mapEnd += color.setBackground("brightYellow", "  ")
            elif j == "e5":
                if indexI == line:
                    mapEnd += color.setBackground("darkYellow", emojiDecoder("f09fa4a0"))
                    line -= 1
                else:
                    mapEnd += color.setBackground("darkYellow", emojiDecoder("f09f9fab"))
            elif j == "e6":
                mapEnd += color.setBackground("brightYellow", emojiDecoder("f09f928e"))

        if shake and shakeIndex == 0:
            mapEnd += f"{color.colorsBg['darkYellow']} {color.colorBgEnd}"
        elif shake and shakeIndex == 1:
            mapEnd += f"{color.colorBgEnd}{' '*11}{color.colorBgEnd}"

        mapEnd += '\n'

    print(mapEnd)

    return line, shakeIndex


def Endcredits():
    clear()
    time.sleep(0.5)
    credit = [
        ["Merci d'avoir joué à mon jeu", 0],
        ["J'espère que ça vous à plu", 0],
        ["Merci à Alain pour ses cours incroyable", 0],
        ["Merci à toutes la classe pour leur aide et leur soutien", 0],
        ["Je n'aurais rien fait sans eux", 0],
        ["(C'est faux)", 0],
        ["(Je me débrouille mieux tout seul)", 0],
        ["Merci à mon génie démesuré", 0],
    ]
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]
    currentHeight = 0
    for index, value in enumerate(credit):
        print(position(0, height-value[1], value[0].center(width, ' ')))
        time.sleep(0.8)
        value[1] += 1
        currentHeight += 1
        for i in range(index):
            credit[i][1] += 1

    currentHeight += 1
    while currentHeight <= height:
        clear()
        currentHeight += 1
        for i in range(len(credit)-1, -1, -1):
            print(position(0, height-currentHeight+credit[i][1], credit[len(credit)-1-i][0].center(width, ' ')))
        time.sleep(0.8)


def randomFire(mapEndData):
    fireCoords = []
    for _ in range(5):
        fireX = random.randint(0, len(mapEndData[0])-1)
        fireY = random.randint(0, len(mapEndData)-1)
        if mapEndData[fireY][fireX] != 'e1':
            continue
        fireCoords.append([fireX, fireY])
        fireX, fireY = 0, 0
    return fireCoords

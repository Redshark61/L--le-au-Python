import time
from functions.Clear import clear
from functions.checkMod import checkMod
from functions.Colors import Colors
from functions.emojiDecoder import emojiDecoder
from functions.Position import position


def finalCinematic():
    clear()
    color = Colors()
    color.init()
    mapEndData = checkMod('mapEnd')
    first = True
    line = len(mapEndData)-1
    # first, line = displayMapEnd(mapEndData, color, first, line)
    # time.sleep(5)
    for _ in range(len(mapEndData)):
        time.sleep(0.1)
        first, line = displayMapEnd(mapEndData, color,  first, line)

    input('')


def displayMapEnd(mapEndData, color, first, line):
    mapEnd = ''
    print(position(1, 1, ''))
    for indexI, i in enumerate(mapEndData):
        for indexJ, j in enumerate(i):
            if indexI == line and indexJ == 24 and line >= 5:
                # print("here")
                mapEnd += color.setBackground("darkYellow", emojiDecoder("f09fa4a0"))
                line -= 1 if line > 5 else 0
            elif j == 'e1':
                mapEnd += color.setBackground("darkYellow", "  ")
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

        mapEnd += '\n'

    print(mapEnd)

    return first, line

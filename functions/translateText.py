import os
import time
from functions.Clear import clear
from functions.Position import position
from functions.Colors import Colors


def translateTextUp(text: list, delay: int | float) -> None:
    """
    Print a text as a star wars like effect (translation from bottom to top).

    `text` is the text you want to display. Each line is a new item in the list
    """
    color = Colors()
    color.init()
    clear()
    list1 = []
    for i in text:
        list1.append([i, 0])

    time.sleep(0.5)
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]
    currentHeight = 0
    for index, value in enumerate(list1):
        print(position(0, height-value[1], value[0].center(width, ' ')))
        time.sleep(delay)
        value[1] += 1
        currentHeight += 1
        for i in range(index):
            list1[i][1] += 1

    currentHeight += 1
    while currentHeight <= height:
        clear()
        currentHeight += 1
        for i in range(len(list1)-1, -1, -1):
            print(position(0, height-currentHeight+list1[i][1], list1[len(list1)-1-i][0].center(width, ' ')))
        time.sleep(delay)

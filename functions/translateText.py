import os
import time
from functions.Clear import clear
from functions.Position import position
from functions.Colors import Colors


def translateTextUp(text: list, delay: int | float) -> None:
    """
    Print a text as a star wars like effect (translation from bottom to top).

    `text` is the list of lines you want to display. Each line is a new item in the list
    """

    # Init variables and colors
    color = Colors()
    color.init()
    clear()
    list1 = []

    # Create a list wich store list -> [line, position]
    for i in text:
        list1.append([i, 0])

    time.sleep(0.5)
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]
    currentHeight = 0

    # Loop through all the line in list1
    for index, value in enumerate(list1):
        # Print it
        print(position(0, height-value[1], value[0].center(width, ' ')))
        time.sleep(delay)
        # Increase its position, so it will be printed higher
        value[1] += 1
        currentHeight += 1
        # Also increase of all the previous lines
        for i in range(index):
            list1[i][1] += 1

    currentHeight += 1
    # While you haven't reached the top of the screen
    while currentHeight <= height:
        clear()
        currentHeight += 1
        for i in range(len(list1)-1, -1, -1):
            print(position(0, height-currentHeight+list1[i][1], list1[len(list1)-1-i][0].center(width, ' ')))
        time.sleep(delay)

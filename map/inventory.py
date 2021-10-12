from typing import Union
from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def inventory(char: bytes, inventoryOpen: bool, noDuplicateInventory: list, itemSelected: int, currentPosition: int) -> Union[bytes, bool]:

    # * Open inventory
    if ord(char) == 50 and not inventoryOpen:  # ord(char) = 50 -> 2
        itemSelected = 0
        widthOfName = len(noDuplicateInventory[itemSelected])
        currentPosition = 3
        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
        inventoryOpen = True

    elif ord(char) == 77 and inventoryOpen:

        itemSelected += 1
        prevWidth = len(noDuplicateInventory[itemSelected-1])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))
        widthOfName = len(noDuplicateInventory[itemSelected])
        currentPosition += prevWidth+5
        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    elif ord(char) == 75 and inventoryOpen:

        itemSelected -= 1
        prevWidth = len(noDuplicateInventory[itemSelected])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))

        widthOfName = len(noDuplicateInventory[itemSelected])

        currentPosition = currentPosition-(widthOfName+5)

        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    # * Close inventory
    elif ord(char) == 50 and inventoryOpen:
        inventoryOpen = False
        currentPosition = 3
        print(position(3, 37, " "*40))

    return char, inventoryOpen, itemSelected, currentPosition

from typing import Union
import time
from functions.Position import position
from functions.emojiDecoder import emojiDecoder

from map.closeInventory import closeInventory


def inventory(char: bytes, inventoryOpen: bool, noDuplicateInventory: list, itemSelected: int, currentPosition: int, pickedUpItem, vitalSigns) -> Union[bytes, bool, int, int]:

    # * Open inventory
    if ord(char) == 50 and not inventoryOpen:  # ord(char) = 50 -> 2
        isEmpty = openInventory(noDuplicateInventory)
        itemSelected = 0
        if isEmpty:
            inventoryOpen = False
            return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns
        inventoryOpen = True

    elif ord(char) == 77 and inventoryOpen:  # Right element
        itemSelected, noDuplicateInventory, currentPosition = rightInventory(itemSelected, noDuplicateInventory, currentPosition)

    elif ord(char) == 75 and inventoryOpen:  # Left element
        itemSelected, noDuplicateInventory, currentPosition = leftInventory(itemSelected, noDuplicateInventory, currentPosition)

    elif ord(char) == 51 and inventoryOpen:  # Eat element
        print(position(3, 35, ' '*40))
        print(position(3, 36, ' '*40))

        for index, value in enumerate(pickedUpItem):
            itemName = value["name"]
            if itemName == noDuplicateInventory[itemSelected][0]:

                if itemName == noDuplicateInventory[itemSelected][0] and value["type"] == "food":
                    vitalSigns['foodMax'] += pickedUpItem[itemSelected]['nutrition']
                if itemName == noDuplicateInventory[itemSelected][0] and value["type"] == "liquid":
                    vitalSigns['waterMax'] += pickedUpItem[itemSelected]['nutrition']
                print(position(1, 1, ' '*40))

                if len(pickedUpItem) == 1:
                    pickedUpItem = []
                    return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns
                else:
                    del pickedUpItem[index]
                    print(position(1, 40, ' '*900))

                    stillInInventory = False
                    for item in pickedUpItem:

                        if item['name'] == itemName:
                            stillInInventory = True
                            print(position(1, 1, 'still in !'))
                            break
                    if not stillInInventory:
                        if itemSelected == 0:
                            break
                        itemSelected, noDuplicateInventory, currentPosition = leftInventory(itemSelected, noDuplicateInventory, currentPosition)
                    break

    # * Close inventory
    elif ord(char) == 50 and inventoryOpen:
        char, inventoryOpen, currentPosition = closeInventory(char, inventoryOpen, currentPosition)

    return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns


def openInventory(noDuplicateInventory):
    if len(noDuplicateInventory) == 0:
        print(position(105, 7, "Ton inventaire est vide !"))
        time.sleep(2)
        print(position(105, 7, " "*40))
        return True

    print(position(105, 7, "-"*47))
    print(position(105, 5, "2 - Fermer l'inventaire"))
    print(position(105, 8, "3 - Consommer"))
    itemSelected = 0
    widthOfName = len(noDuplicateInventory[itemSelected][0])
    currentPosition = 3
    print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return False


def leftInventory(itemSelected, noDuplicateInventory, currentPosition):
    itemSelected -= 1
    prevWidth = len(noDuplicateInventory[itemSelected][0])
    print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))

    widthOfName = len(noDuplicateInventory[itemSelected][0])

    currentPosition = currentPosition-(widthOfName+5)

    print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return itemSelected, noDuplicateInventory, currentPosition


def rightInventory(itemSelected, noDuplicateInventory, currentPosition):
    itemSelected += 1
    prevWidth = len(noDuplicateInventory[itemSelected-1][0])
    print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))
    widthOfName = len(noDuplicateInventory[itemSelected][0])
    currentPosition += prevWidth+5
    print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    return itemSelected, noDuplicateInventory, currentPosition

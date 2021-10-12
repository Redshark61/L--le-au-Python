from typing import Union
import time
from functions.Position import position
from functions.emojiDecoder import emojiDecoder

from map.closeInventory import closeInventory


def inventory(char: bytes, inventoryOpen: bool, noDuplicateInventory: list, itemSelected: int, currentPosition: int, pickedUpItem, vitalSigns) -> Union[bytes, bool, int, int]:
    print(position(3, 37, " "*40))

    # * Open inventory
    if ord(char) == 50 and not inventoryOpen:  # ord(char) = 50 -> 2
        if len(noDuplicateInventory) == 0:
            print(position(105, 7, "Ton inventaire est vide !"))
            time.sleep(2)
            print(position(105, 7, " "*40))
            return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns

        else:
            print(position(105, 7, "-"*47))
            print(position(105, 5, "2 - Fermer l'inventaire"))
            print(position(105, 8, "3 - Consommer"))
            itemSelected = 0
            widthOfName = len(noDuplicateInventory[itemSelected][0])
            currentPosition = 3
            print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
            inventoryOpen = True

    elif ord(char) == 77 and inventoryOpen:

        itemSelected += 1
        prevWidth = len(noDuplicateInventory[itemSelected-1][0])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))
        widthOfName = len(noDuplicateInventory[itemSelected][0])
        currentPosition += prevWidth+5
        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    elif ord(char) == 75 and inventoryOpen:

        itemSelected -= 1
        prevWidth = len(noDuplicateInventory[itemSelected][0])
        print(position(currentPosition, 37, ' '.center(prevWidth, ' ')))

        widthOfName = len(noDuplicateInventory[itemSelected][0])

        currentPosition = currentPosition-(widthOfName+5)

        print(position(currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    elif ord(char) == 51 and inventoryOpen:
        print(position(3, 35, ' '*40))
        print(position(3, 36, ' '*40))

        for index, value in enumerate(pickedUpItem):
            if pickedUpItem[index]["name"] == noDuplicateInventory[itemSelected][0]:

                if pickedUpItem[index]["name"] == noDuplicateInventory[itemSelected][0] and pickedUpItem[index]["type"] == "food":
                    vitalSigns['foodMax'] += pickedUpItem[itemSelected]['nutrition']
                if pickedUpItem[index]["name"] == noDuplicateInventory[itemSelected][0] and pickedUpItem[index]["type"] == "liquid":
                    vitalSigns['waterMax'] += pickedUpItem[itemSelected]['nutrition']
                print(position(1, 1, ' '*40))

                if len(pickedUpItem) == 1:
                    pickedUpItem = []
                    return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns

                else:
                    del pickedUpItem[index]
                break

    # * Close inventory
    elif ord(char) == 50 and inventoryOpen:
        char, inventoryOpen, currentPosition = closeInventory(char, inventoryOpen, currentPosition)

    return char, inventoryOpen, itemSelected, currentPosition, pickedUpItem, vitalSigns

import time
from functions.Position import position
from functions.emojiDecoder import emojiDecoder
from functions import config
from map.closeInventory import closeInventory
from map.eating import eating


def inventory(inventoryOpen: bool, noDuplicateInventory: list[tuple]) -> bool:

    # * Open inventory
    if ord(config.char) == 50 and not inventoryOpen:  # ord(config.char) = 50 -> 2
        isEmpty = openInventory(noDuplicateInventory)
        config.itemSelected = 0
        if isEmpty:
            inventoryOpen = False
            return inventoryOpen
        inventoryOpen = True

    elif ord(config.char) == 77 and inventoryOpen:  # Right element
        noDuplicateInventory = rightInventory(noDuplicateInventory)

    elif ord(config.char) == 75 and inventoryOpen:  # Left element
        noDuplicateInventory = leftInventory(noDuplicateInventory)

    elif ord(config.char) == 51 and inventoryOpen:  # Eat element
        print(position(3, 35, ' '*40))
        print(position(3, 36, ' '*40))

        for index, value in enumerate(config.pickedUpItem):
            itemName = value["name"]
            if itemName == noDuplicateInventory[config.itemSelected][0]:
                eating(noDuplicateInventory, itemName, value)

                if len(config.pickedUpItem) == 1:
                    config.pickedUpItem = []
                    return inventoryOpen
                del config.pickedUpItem[index]

                stillInInventory = False
                for item in config.pickedUpItem:

                    if item['name'] == itemName:
                        stillInInventory = True
                        break
                if not stillInInventory:
                    if config.itemSelected == 0:
                        break
                    leftInventory(noDuplicateInventory)
                break

    # * Close inventory
    elif ord(config.char) == 50 and inventoryOpen:
        inventoryOpen = closeInventory(inventoryOpen)

    return inventoryOpen


def openInventory(noDuplicateInventory: list[tuple]) -> list[tuple]:
    if len(noDuplicateInventory) == 0:
        print(position(105, 7, "Ton inventaire est vide !"))
        time.sleep(2)
        print(position(105, 7, " "*40))
        return True

    print(position(105, 7, "-"*47))
    print(position(105, 5, "2 - Fermer l'inventaire"))
    print(position(105, 8, "3 - Consommer"))
    config.itemSelected = 0
    widthOfName = len(noDuplicateInventory[config.itemSelected][0])
    config.currentPosition = 3
    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return False


def leftInventory(noDuplicateInventory: list[tuple]) -> list[tuple]:
    config.itemSelected -= 1
    prevWidth = len(noDuplicateInventory[config.itemSelected][0])
    print(position(config.currentPosition, 37, ' '.center(prevWidth, ' ')))

    widthOfName = len(noDuplicateInventory[config.itemSelected][0])

    config.currentPosition = config.currentPosition-(widthOfName+5)

    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return noDuplicateInventory


def rightInventory(noDuplicateInventory: list[tuple]) -> list[tuple]:
    config.itemSelected += 1
    prevWidth = len(noDuplicateInventory[config.itemSelected-1][0])
    print(position(config.currentPosition, 37, ' '.center(prevWidth, ' ')))
    widthOfName = len(noDuplicateInventory[config.itemSelected][0])
    config.currentPosition += prevWidth+5
    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    return noDuplicateInventory

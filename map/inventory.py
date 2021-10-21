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
        config.inventorySize -= 1

        # Loop through all the items picked up
        for index, value in enumerate(config.pickedUpItem):
            itemName = value["name"]

            # When the name of the element s the same as the element selected, eat it
            if itemName == noDuplicateInventory[config.itemSelected][0]:
                # He can't eat (ate=False) if he is full
                ate, foodType = eating(noDuplicateInventory, itemName, value)

                if ate:
                    print(position(105, 11, " "*40))
                    # If he ate the last item
                    if len(config.pickedUpItem) == 1:
                        # Empty the list to be sure
                        config.pickedUpItem = []
                        return inventoryOpen
                    # Else just delete the item
                    del config.pickedUpItem[index]

                    # By default we assume item is not in the inventory
                    stillInInventory = False
                    for item in config.pickedUpItem:
                        # If the item is still in the inventory jsut return
                        if item['name'] == itemName:
                            stillInInventory = True
                            break
                    # Else go left (or dont move if the item selected is already on the left)
                    if not stillInInventory:
                        if config.itemSelected == 0:
                            break
                        leftInventory(noDuplicateInventory)
                    break

                print(position(105, 11, " "*40))
                print(position(105, 11, f"Tu n'as pas envie de {'manger' if foodType == 'food' else 'boire'}"))

    # * Close inventory
    elif ord(config.char) == 50 and inventoryOpen:
        inventoryOpen = closeInventory(inventoryOpen)

    return inventoryOpen


def openInventory(noDuplicateInventory: list[tuple]) -> bool:
    """
    Open the inventory
    """
    if len(noDuplicateInventory) == 0:
        print(position(105, 9, "Ton inventaire est vide !"))
        time.sleep(2)
        print(position(105, 9, " "*40))
        return True

    # Update the right panel
    print(position(105, 9, "-"*47))
    print(position(105, 5, "2 - Fermer l'inventaire"))
    print(position(105, 10, "3 - Consommer"))

    config.itemSelected = 0
    widthOfName = len(noDuplicateInventory[config.itemSelected][0])
    config.currentPosition = 3
    # Print an arrow under the name of the selected item
    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return False


def leftInventory(noDuplicateInventory: list[tuple]) -> list[tuple]:
    """
    Move the arrow on the left
    """
    if config.itemSelected == 0:
        return noDuplicateInventory
    # Get the item on the left
    config.itemSelected -= 1
    prevWidth = len(noDuplicateInventory[config.itemSelected][0])
    # Erase the previous arrow
    print(position(config.currentPosition, 37, ' '.center(prevWidth, ' ')))

    widthOfName = len(noDuplicateInventory[config.itemSelected][0])

    config.currentPosition = config.currentPosition-(widthOfName+5)
    # Print the new arrow
    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))
    return noDuplicateInventory


def rightInventory(noDuplicateInventory: list[tuple]) -> list[tuple]:
    """
    Move the arrow on the right
    """
    if config.itemSelected == len(noDuplicateInventory)-1:
        return noDuplicateInventory

    config.itemSelected += 1
    prevWidth = len(noDuplicateInventory[config.itemSelected-1][0])
    print(position(config.currentPosition, 37, ' '.center(prevWidth, ' ')))
    widthOfName = len(noDuplicateInventory[config.itemSelected][0])
    config.currentPosition += prevWidth+5
    print(position(config.currentPosition, 37, emojiDecoder('e2ac86').center(widthOfName, ' ')))

    return noDuplicateInventory

from functions.Position import position


def closeInventory(char, inventoryOpen, currentPosition):
    # * Close inventory
    inventoryOpen = False
    currentPosition = 3
    print(position(105, 5, " "*40))
    print(position(105, 5, "2 - Ouvrir Inventaire"))
    print(position(105, 7, " "*47))
    print(position(105, 8, " "*47))
    print(position(3, 37, " "*40))
    print(position(3, 38, " "*40))
    print(position(3, 36, " "*40))

    return char, inventoryOpen, currentPosition

from functions.Position import position
from functions import config
from functions.drawRightPanel import drawRightPanel


def closeInventory(inventoryOpen: bool) -> bool:
    """Close inventory"""
    inventoryOpen = False
    config.currentPosition = 3
    drawRightPanel()
    # Clean the inventory
    print(position(3, 37, " "*40))
    print(position(3, 38, " "*40))
    print(position(3, 36, " "*40))

    return inventoryOpen

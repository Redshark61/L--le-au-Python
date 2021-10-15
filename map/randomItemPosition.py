import random
from functions.checkMod import checkMod


def randomItemPosition() -> list[dict]:
    """
    Return a list of dictionnairies containing coordonates of each item on the map
    like :

    createdItems = [
        'item' : [X,Y],
        'item' : [X,Y]
    ]
    """
    items = checkMod("items")
    mapCoord = checkMod("map")

    createdItems = []
    currentItems = items
    # For each item wich needs to be created
    for item in currentItems:
        # We create the number of item desired
        for _ in range(currentItems[item]["number"]):
            itemPosX = 0
            itemPosY = 0
            if currentItems[item]['spawn'] == "generic":
                while mapCoord[itemPosY][itemPosX] == 2 or mapCoord[itemPosY][itemPosX] == 3:
                    itemPosX = random.randint(0, len(mapCoord[0])-1)
                    itemPosY = random.randint(0, len(mapCoord)-1)
                createdItems.append({item: [itemPosX, itemPosY]})

    return createdItems, currentItems

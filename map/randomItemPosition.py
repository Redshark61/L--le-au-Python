from functions.checkMod import checkMod
import random


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

    createdItems = []
    currentItems = items

    for item in currentItems:
        for i in range(currentItems[item]["number"]):
            if currentItems[item]['spawn'] == "generic":
                itemPosX = random.randint(10, 80)
                itemPosY = random.randint(9, 20)
                createdItems.append({item: [itemPosX, itemPosY]})

    return createdItems, currentItems

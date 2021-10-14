from functions.Position import position
from functions import config


def eating(noDuplicateInventory: list[tuple], itemName: str, value: dict):
    if itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "food":
        config.vitalSigns['foodMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    if itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "liquid":
        config.vitalSigns['waterMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    print(position(1, 1, ' '*40))

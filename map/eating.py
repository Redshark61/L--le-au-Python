from functions import config


def eating(noDuplicateInventory: list[tuple], itemName: str, value: dict):
    if itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "food" and config.vitalSigns['foodMax']+value['nutrition'] <= 100:
        config.vitalSigns['foodMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    elif itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "liquid" and config.vitalSigns['waterMax']+value['nutrition'] <= 100:
        config.vitalSigns['waterMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    else:
        return False
    return True

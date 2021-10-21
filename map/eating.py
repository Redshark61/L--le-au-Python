from functions import config


def eating(noDuplicateInventory: list[tuple], itemName: str, value: dict) -> bool | str:
    """
    Function to eat or drink
    """

    # If it's food and he is not full
    if itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "food" and config.vitalSigns['foodMax']+value['nutrition'] <= 100:
        config.vitalSigns['foodMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    # If it's water and he is not full
    elif itemName == noDuplicateInventory[config.itemSelected][0] and value["type"] == "liquid" and config.vitalSigns['waterMax']+value['nutrition'] <= 100:
        config.vitalSigns['waterMax'] += config.pickedUpItem[config.itemSelected]['nutrition']
    else:
        return False, value["type"]

    return True, value["type"]

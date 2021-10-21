import json
from functions import config
from functions.checkMod import checkMod
from map.randomItemPosition import randomItemPosition


def checkSave(saveName: str) -> None:
    """
    Check if there is a save, and initalize all the variables
    """

    # Open the save file
    with open(saveName, encoding='utf-8') as f:
        savedData = json.load(f)

    # If there is a full save, get all the data
    if len(savedData) > 2:
        config.playerName = savedData['playerName']
        config.coord = checkMod('coordinates')
        config.playerCoord = savedData['playerCoord']
        config.key = savedData['key']
        config.vitalSigns = savedData['health']
        config.pickedUpItem = savedData['inventory']
        config.currentItems = savedData['currentItems']
        config.createdItems = savedData['itemPosition']
        config.questDone = savedData['questDone']
        config.questToDo = savedData['questToDo']
        config.inventorySize = savedData['inventorySize']
        config.playerMark = savedData['playerSkinMark']
    # If there is nothing (just the name of the player)
    else:
        # Set everything as default
        config.playerName = savedData['playerName']
        config.coord = checkMod('coordinates')
        config.playerCoord.append(config.coord['player']["coords"][0])
        config.playerCoord.append(config.coord['player']["coords"][1])
        config.pickedUpItem = []
        config.createdItems, config.currentItems = randomItemPosition()
        config.questDone = []
        for quest in config.coord:
            if quest != 'player':
                config.questToDo.append({quest: config.coord[quest]['coords']})

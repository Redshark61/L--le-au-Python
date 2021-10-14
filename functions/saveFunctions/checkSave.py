import json
import time
from functions import config
from functions.checkMod import checkMod
from map.randomItemPosition import randomItemPosition


def checkSave(saveName):

    with open(saveName, encoding='utf-8') as f:
        savedData = json.load(f)

    if len(savedData) > 2:
        config.coord = checkMod('coordinates')
        config.playerCoord = savedData['playerCoord']
        config.key = savedData['key']
        config.vitalSigns = savedData['health']
        config.pickedUpItem = savedData['inventory']
        config.currentItems = savedData['currentItems']
        config.createdItems = savedData['itemPosition']
        config.questDone = savedData['questDone']
        config.questToDo = savedData['questToDo']
    else:

        # Récupérer les coordonnés
        config.coord = checkMod('coordinates')
        config.playerCoord.append(config.coord['player']["coords"][0])
        config.playerCoord.append(config.coord['player']["coords"][1])
        config.pickedUpItem = []
        config.createdItems, config.currentItems = randomItemPosition()
        config.questDone = []
        for quest in config.coord:
            if quest != 'player':
                config.questToDo.append({quest: config.coord[quest]['coords']})

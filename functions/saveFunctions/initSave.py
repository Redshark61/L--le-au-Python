import json
from datetime import datetime
from functions import config

today = datetime.now()


def initSave():
    playerName = input("Quel est ton nom :\n")
    currentDate = today.strftime("%d/%m/%Y %H:%M:%S")
    save = {
        "playerName": playerName,
        "currentDate": currentDate
    }
    saveName = f"save-{playerName}.json"
    with open(f'./saves/{saveName}', 'w', encoding='utf-8') as f:
        json.dump(save, f, indent=4)
    print(config.hiddenCursor)
    return saveName

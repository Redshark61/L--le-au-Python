import json
from datetime import date
from functions import config

today = date.today()


def initSave():
    playerName = input("Quel est ton nom :\n")
    currentDate = today.strftime("%d/%m/%Y %H:%M:%S")
    save = {
        "playerName": playerName,
        "currentDate": currentDate
    }
    with open(f'./saves/save-{playerName}.json', 'w', encoding='utf-8') as f:
        json.dump(save, f)
    print(config.hiddenCursor)

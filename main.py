from datetime import datetime
import time
import json
import os
from functions.checkMod import checkMod
from functions.emojiDecoder import emojiDecoder
from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config


def main() -> None:

    saveName = checkSaveFiles()
    # finalTrailer()
    mapLoop(saveName)
    clear()


def checkSaveFiles():
    clear()
    # Begining of the program
    saveInSavesFolder = os.listdir('./saves')
    skinData = checkMod('playerStats')

    # If there are no save, create one and launch the game
    if len(saveInSavesFolder) == 0:
        print("no save")
        saveName = initSave(skinData)
    else:
        # If there is only one save
        if len(saveInSavesFolder) == 1:
            saveName = oneSave(saveInSavesFolder, skinData)
        elif len(saveInSavesFolder) > 1:
            saveName = multipleSave(saveInSavesFolder, skinData)

    print(config.hiddenCursor)
    return saveName


def initSave(skinData):
    today = datetime.now()
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

    print("Quel skin choisis-tu ?")

    index = 1
    for _, value in skinData.items():
        print(f"{index} - {emojiDecoder(value['mark'])}")
        index += 1

    print(config.visibleCursor)

    while True:
        try:
            skinChoice = int(input('- '))
            skinChoice = list(skinData.keys())[skinChoice-1]
            break
        except ValueError:
            print("Je n'ai pas compris")

    setPlayerData(skinData, skinChoice)

    print(config.hiddenCursor)

    return "./saves/"+saveName


def oneSave(saveInSavesFolder, skinData):
    with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
        save = json.load(f)

    print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. Que veux-tu faire ?\n")
    choice = input("1 - Jouer\n2 - Supprimer\n3 - Créer une nouvelle partie\n")
    clear()
    match choice:
        case '1':
            saveName = f"./saves/{saveInSavesFolder[0]}"
            setPlayerData(skinData, save['playerSkinName'])
        case '2':
            isRemoved = deleteSave(saveInSavesFolder, 0)
            clear()
            if isRemoved:
                saveName = initSave(skinData)
            else:
                saveName = checkSaveFiles()
        case '3':
            saveName = initSave(skinData)
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            saveName = oneSave(saveInSavesFolder, save['playerSkinName'])
    return saveName


def multipleSave(saveInSavesFolder, skinData):
    with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
        save = json.load(f)

    print("Il y a plusieurs sauvegarde, que veux-tu faire ?")
    choice = input("1 - Sélectionner une partie\n2 - Créer une nouvelle partie\n")
    clear()
    match choice:
        case '1':
            for index, file in enumerate(saveInSavesFolder):
                print(f"{index + 1} - {file[5:-5]}")
            fileChoice = int(input(''))
            clear()
            print(f"Tu as choisis {saveInSavesFolder[int(fileChoice)-1][5:-5]}")
            saveName = choiceSave(saveInSavesFolder, fileChoice, skinData, save['playerSkinName'])
        case '2':
            saveName = initSave(skinData)
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            multipleSave(saveInSavesFolder, skinData)
    return saveName


def deleteSave(saveInSavesFolder, fileChoice):
    print(f"Es-tu sûr de vouloir effacer la sauvegarde de {saveInSavesFolder[int(fileChoice)-1][5:-5]}")
    confirm = input("o - Oui\nn - Non\n").lower()
    match confirm:
        case 'o':
            clear()
            os.remove(f"./saves/{saveInSavesFolder[int(fileChoice)-1]}")
            return True
        case 'n':
            clear()
            return False
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            deleteSave(saveInSavesFolder, fileChoice)


def choiceSave(saveInSavesFolder, fileChoice, skinData, skinChoice):
    choice = input("Que veux-tu en faire ?\n1 - Jouer\n2 - Supprimer\n")
    clear()
    match choice:
        case '1':
            setPlayerData(skinData, skinChoice)
            return f"./saves/{saveInSavesFolder[int(fileChoice)-1]}"
        case '2':
            isRemoved = deleteSave(saveInSavesFolder, fileChoice)
            if isRemoved:
                saveName = checkSaveFiles()
            else:
                saveName = multipleSave(saveInSavesFolder, skinData)
            return saveName
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            choiceSave(saveInSavesFolder, fileChoice, skinData, skinChoice)


def setPlayerData(skinData, skinChoice):
    config.inventoryMax = skinData[skinChoice]['inventoryMax']
    config.energyWhileSleeping = skinData[skinChoice]['energyWhileSleeping']
    config.looseFoodSleep = skinData[skinChoice]['looseFoodSleep']
    config.looseFoodPerStep = skinData[skinChoice]['looseFoodPerStep']
    config.looseWaterPerStep = skinData[skinChoice]['looseWaterPerStep']
    config.looseEnergiePerStep = skinData[skinChoice]['looseEnergiePerStep']
    config.playerMark = skinData[skinChoice]['mark']
    config.energyMax = skinData[skinChoice]['energyMax']
    config.foodMax = skinData[skinChoice]['foodMax']
    config.waterMax = skinData[skinChoice]['waterMax']
    config.skinName = skinChoice

    config.vitalSigns = {
        "energyMax": skinData[skinChoice]['energyMax'],
        "foodMax": skinData[skinChoice]['foodMax'],
        "waterMax": skinData[skinChoice]['waterMax']
    }

    coordData = checkMod('coordinates')
    coordData['player']['mark'] = config.playerMark

    with open("coordinates.json", 'w', encoding='utf-8') as f:
        json.dump(coordData, f)


if __name__ == "__main__":
    clear()
    main()

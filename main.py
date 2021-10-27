from datetime import datetime
import time
import json
import os
from functions import config
from functions.Clear import clear
from map.mapLoop import mapLoop
from introductions import introduction
from functions.emojiDecoder import emojiDecoder
from functions.checkMod import checkMod


def main() -> None:

    # Chek if there are saves, and initalize if not
    saveName = checkSaveFiles()
    mapLoop(saveName)
    clear()


def checkSaveFiles():
    clear()

    # Get the list of all the saves
    saveInSavesFolder = os.listdir('./saves')
    # Get the data for each possible skin
    skinData = checkMod('playerStats')

    # If there are no save, create one and launch the game
    if len(saveInSavesFolder) == 0:
        saveName = initSave(skinData)
    else:
        # If there is only one save
        if len(saveInSavesFolder) == 1:
            saveName = oneSave(saveInSavesFolder, skinData)
        # If there are multiple saves
        elif len(saveInSavesFolder) > 1:
            saveName = multipleSave(saveInSavesFolder, skinData)

    print(config.hiddenCursor)
    return saveName

# Initalize saves


def initSave(skinData):
    # Get the current date and player name
    today = datetime.now()
    playerName = input("Quel est ton nom :\n")
    currentDate = today.strftime("%d/%m/%Y %H:%M:%S")
    save = {
        "playerName": playerName,
        "currentDate": currentDate
    }
    # Create a name for the save
    saveName = f"save-{playerName}.json"

    # Open it and start wrinting in it
    with open(f'./saves/{saveName}', 'w', encoding='utf-8') as f:
        json.dump(save, f, indent=4)
    print(config.hiddenCursor)

    print("Quel skin choisis-tu ?")

    # Display all the possible skins
    index = 1
    for _, value in skinData.items():
        print(f"{index} - {emojiDecoder(value['mark'])}")
        index += 1

    print(config.visibleCursor)

    # Let the player choose a skin
    while True:
        try:
            skinChoice = int(input('- '))
            skinChoice = list(skinData.keys())[skinChoice-1]
            break
        except ValueError:
            print("Je n'ai pas compris")

    # Configure all the variable depending on the skin choose
    setPlayerData(skinData, skinChoice)

    print(config.hiddenCursor)

    clear()
    # Let the player choose if he want to see the tutorial or not
    wannaSeeTuto = ''
    while wannaSeeTuto.upper() not in ('O', 'N'):
        wannaSeeTuto = input("Veux-tu voir le tutoriel ? (o/n) : \n")
    match wannaSeeTuto.upper():
        case 'O':
            introduction()
            return "./saves/"+saveName
        case 'N':
            return "./saves/"+saveName

# There is only one save


def oneSave(saveInSavesFolder, skinData):
    # Open it
    with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
        save = json.load(f)

    print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. Que veux-tu faire ?\n")
    choice = input("1 - Jouer\n2 - Supprimer\n3 - Créer une nouvelle partie\n")
    clear()
    # The player choose if he wants to play, delete, or create a new game
    match choice:
        case '1':
            # If he wanna play, configure all the variables
            saveName = f"./saves/{saveInSavesFolder[0]}"
            setPlayerData(skinData, save['playerSkinName'])
        case '2':
            # Delete the save
            isRemoved = deleteSave(saveInSavesFolder, 0)
            clear()
            if isRemoved:
                # Beacuse there was only one save, now it's removed he need to create a new game
                saveName = initSave(skinData)
            else:
                # If he didnt removed the save, start again
                saveName = checkSaveFiles()
        case '3':
            # Create a new save
            saveName = initSave(skinData)
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            saveName = oneSave(saveInSavesFolder, save['playerSkinName'])
    return saveName


def multipleSave(saveInSavesFolder, skinData):
    # Open the save
    with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
        save = json.load(f)

    print("Il y a plusieurs sauvegarde, que veux-tu faire ?")
    choice = input("1 - Sélectionner une partie\n2 - Créer une nouvelle partie\n")
    # If the choice is wrong
    while choice not in ('1', '2', '3'):
        clear()
        print("Je n'ai pas compris")
        choice = input("1 - Sélectionner une partie\n2 - Créer une nouvelle partie\n")

    clear()
    # If he wanna choose a game
    if choice == '1':
        for index, file in enumerate(saveInSavesFolder):
            print(f"{index + 1} - {file[5:-5]}")
        fileChoice = int(input(''))
        clear()
        print(f"Tu as choisis {saveInSavesFolder[int(fileChoice)-1][5:-5]}")
        # Make him decide what to do with this save
        saveName = choiceSave(saveInSavesFolder, fileChoice, skinData, save['playerSkinName'])
    # Create a new game
    elif choice == '2':
        saveName = initSave(skinData)

    return saveName


def deleteSave(saveInSavesFolder, fileChoice):
    # Ask if he want to delete
    print(f"Es-tu sûr de vouloir effacer la sauvegarde de {saveInSavesFolder[int(fileChoice)-1][5:-5]}")
    confirm = input("o - Oui\nn - Non\n").lower()
    match confirm:
        case 'o':
            # If yes, delete everything
            clear()
            os.remove(f"./saves/{saveInSavesFolder[int(fileChoice)-1]}")
            return True
        case 'n':
            # Else do nothing
            clear()
            return False
        case _:
            print("Je n'ai pas compris")
            time.sleep(2)
            clear()
            deleteSave(saveInSavesFolder, fileChoice)


def choiceSave(saveInSavesFolder, fileChoice, skinData, skinChoice):
    # The choices for a save
    choice = input("Que veux-tu en faire ?\n1 - Jouer\n2 - Supprimer\n")
    clear()
    match choice:
        case '1':
            # If he wanna play, return the path of the save
            setPlayerData(skinData, skinChoice)
            return f"./saves/{saveInSavesFolder[int(fileChoice)-1]}"
        case '2':
            # If he wanna delete
            isRemoved = deleteSave(saveInSavesFolder, fileChoice)
            if isRemoved:
                # Recheck for save whan it's deleted
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


if __name__ == "__main__":
    clear()
    main()

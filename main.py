from datetime import datetime
import time
import json
import os
from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config


def main() -> None:

    saveName = checkSaveFiles()

    mapLoop(saveName)
    clear()


def checkSaveFiles():
    clear()
    # Begining of the program
    saveInSavesFolder = os.listdir('./saves')
    print(saveInSavesFolder)

    # If there are no save, create one and launch the game
    if len(saveInSavesFolder) == 0:
        print("no save")
        saveName = initSave()
    else:
        # If there is only one save
        if len(saveInSavesFolder) == 1:
            saveName = oneSave(saveInSavesFolder)
        elif len(saveInSavesFolder) > 1:
            saveName = multipleSave(saveInSavesFolder)

    print(config.hiddenCursor)
    return saveName


def initSave():
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
    return "./saves/"+saveName


def oneSave(saveInSavesFolder):
    with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
        save = json.load(f)

    print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. Que veux-tu faire ?\n")
    choice = input("1 - Jouer\n2 - Supprimer\n3 - Créer une nouvelle partie\n")
    clear()
    match choice:
        case '1':
            saveName = f"./saves/{saveInSavesFolder[0]}"
        case '2':
            isRemoved = deleteSave(saveInSavesFolder, 0)
            clear()
            if isRemoved:
                saveName = initSave()
            else:
                saveName = checkSaveFiles()
        case '3':
            saveName = initSave()
    return saveName


def multipleSave(saveInSavesFolder):
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
            # saveName = f"./saves/{saveInSavesFolder[int(fileChoice)-1]}"
            saveName = choiceSave(saveInSavesFolder, fileChoice)
        case '2':
            saveName = initSave()
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


def choiceSave(saveInSavesFolder, fileChoice):
    choice = input("Que veux-tu en faire ?\n1 - Jouer\n2 - Supprimer\n")
    clear()
    match choice:
        case '1':
            return f"./saves/{saveInSavesFolder[int(fileChoice)-1]}"
        case '2':
            isRemoved = deleteSave(saveInSavesFolder, fileChoice)
            if isRemoved:
                saveName = checkSaveFiles()
            else:
                saveName = multipleSave(saveInSavesFolder)

            return saveName


if __name__ == "__main__":
    clear()
    main()

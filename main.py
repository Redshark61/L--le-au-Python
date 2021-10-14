import json
import os
from functions.saveFunctions.deleteSave import deleteSave
from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config
from functions.saveFunctions.initSave import initSave
from functions.saveFunctions.choiceSave import choiceSave


def main() -> None:
    # Begining of the program
    saveInSavesFolder = os.listdir('./saves')

    if len(saveInSavesFolder) == 0:
        saveName = initSave()

    else:
        if len(saveInSavesFolder) == 1:
            with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
                save = json.load(f)

            print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. Que veux-tu faire ?\n")
            choice = input("1 - Jouer\n2 - Supprimer\n3 - Créer une nouvelle partie\n")
            clear()
            match choice:
                case '1':
                    saveName = f"./saves/{saveInSavesFolder[0]}"
                case '2':
                    deleteSave(saveInSavesFolder, 0)
                    clear()
                    saveName = initSave()
                case '3':
                    saveName = initSave()
        else:
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
                    saveName = f"./saves/{saveInSavesFolder[int(fileChoice)-1]}"
                    choiceSave(saveInSavesFolder, fileChoice)
                case '2':
                    saveName = initSave()

    print(config.hiddenCursor)

    mapLoop(saveName)
    clear()


if __name__ == "__main__":
    clear()
    main()

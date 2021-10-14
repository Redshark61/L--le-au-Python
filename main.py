import json
import os
from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config
from functions.saveFunctions.initSave import initSave


def main() -> None:
    # Begining of the program
    saveInSavesFolder = os.listdir('./saves')

    if len(saveInSavesFolder) == 0:
        initSave()

    else:
        if len(saveInSavesFolder) == 1:
            with open(f"./saves/{saveInSavesFolder[0]}", encoding='utf-8') as f:
                save = json.load(f)

            print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. La charger ?\n")
            choice = input("1 - oui\n2 - non\n")
            match choice:
                case '1':
                    pass
                case '2':
                    initSave()
        else:
            print("Il y a plusieurs sauvegarde, laquelle veux-tu sélectionner ?")
            for index, file in enumerate(saveInSavesFolder):
                print(f"{index + 1} - {file[5:-5]}")
            choice = input('')

    print(config.hiddenCursor)

    mapLoop()
    clear()


if __name__ == "__main__":
    clear()
    main()

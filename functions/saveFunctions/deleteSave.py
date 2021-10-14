import os


def deleteSave(saveInSavesFolder, fileChoice):
    print(f"Es-tu sûr de vouloir effacer la sauvegarde de {saveInSavesFolder[int(fileChoice)-1][5:-5]}")
    confirm = input("o - Oui\nn - Non\n").lower()
    match confirm:
        case 'o':
            os.remove(f"./saves/{saveInSavesFolder[fileChoice]}")
        case 'n':
            return

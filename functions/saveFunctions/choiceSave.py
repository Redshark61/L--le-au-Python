from functions.saveFunctions.deleteSave import deleteSave


def choiceSave(saveInSavesFolder, fileChoice):
    choice = input("Que veux-tu en faire ?\n1 - Jouer\n2 - Supprimer\n")
    match choice:
        case '1':
            pass
        case '2':
            deleteSave(saveInSavesFolder, fileChoice)

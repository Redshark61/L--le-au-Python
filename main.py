import json
import os.path
from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config


def main() -> None:
    # Begining of the program

    if os.path.isfile('./save.json'):
        with open('save.json', encoding='utf-8') as f:
            save = json.load(f)

        print(f"Il y a déjà une sauvegarde au nom de {save['playerName']}. La charger ?\n")
        choice = input("1 - oui\n2 - non\n")
        match choice:
            case '1':
                pass
            case '2':
                playerName = input("Quel est ton nom :\n")
                with open('save.json', 'w', encoding='utf-8') as f:
                    json.dump({"playerName": playerName}, f)
                print(config.hiddenCursor)
    mapLoop()
    clear()


if __name__ == "__main__":
    clear()
    main()

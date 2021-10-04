from functions.Colors import Colors
from functions.Clear import clear
import time


def displayMap(data: dict, coord: dict, playerX: int, playerY: int, questDone: list) -> None:

    color = Colors
    color.init()

    # On remonte le curseur de la taille de la map + la où est le curseur acutellement
    print((len(data)+3) * "\033[A", end="")

    row = 0
    map = ''
    # Pour chaque ligne dans le json de la carte
    for i in data:
        col = 0

        # Pour chaque case dans le json de la carte
        for j in i:
            # Le caractère de base est 2 espaces
            char = '\u0020\u0020'

            # Pour chaque position dans le json de coordonnés
            for item in coord:

                # Toutes les icônes doivent être converties de hex en string lisible par le terminal
                string = coord[item]['mark']
                byteArray = bytearray.fromhex(string)
                mark = byteArray.decode()
                symbol = mark

                # Si ce n'est pas un joueur, on vérifie si la boucle affiche les coordonnés d'une position du json
                if item != "player":
                    if row == coord[item]['coords'][1] and col == coord[item]['coords'][0]:
                        char = color.setForeground('red', symbol)
                # Si c'est un joueur, on vérifie si la boucle affiche les coords du joueur
                else:
                    if row == playerY and col == playerX:
                        char = color.setForeground('red', symbol)

            for quest in questDone:
                if row == quest[1] and col == quest[0]:
                    string = "e29c85"
                    byteArray = bytearray.fromhex(string)
                    mark = byteArray.decode()
                    char = mark

            # En fonction du code couleur de la case, on change le background
            if j == 1:
                map += color.setBackground("brightGray", char)
            elif j == 2:
                map += color.setBackground('brightCyan', char)
            elif j == 3:
                map += color.setBackground('darkBlue', char)
            elif j == 4:
                map += color.setBackground('brightYellow', char)
            elif j == 5:
                map += color.setBackground('brightGreen', char)
            elif j == 6:
                map += color.setBackground('darkGray', char)

            col += 1

        row += 1
        map += '\n'
    print(map)

    for item in coord:
        if (playerY == coord[item]['coords'][1] and playerX == coord[item]['coords'][0]) and item != 'player':
            if len(questDone) == 0:
                questDone.append(coord[item]['coords'])
                module = __import__(f"{coord[item]['folder']}.{coord[item]['mainFile']}", fromlist=[None])
                module.main()
                return questDone
            else:
                for quest in questDone:
                    if (playerY != quest[1] and playerX != quest[0]):
                        continue
                    else:
                        return questDone
                questDone.append(coord[item]['coords'])
                module = __import__(f"{coord[item]['folder']}.{coord[item]['mainFile']}", fromlist=[None])
                module.main()
                return questDone
    return questDone

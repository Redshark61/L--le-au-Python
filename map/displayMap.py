from functions.Colors import Colors


def displayMap(data, coord, playerX, playerY):

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

            # Si le coordonnée actuel est une coord de quête, alors on met une croix et pas un espace
            for item in coord:

                if item != "player":
                    if row == coord[item]['coords'][1] and col == coord[item]['coords'][0]:
                        symbol = coord[item]['mark'] + '\u0020'
                        char = color.setForeground('red', symbol)
                else:
                    if row == playerY and col == playerX:
                        symbol = coord["player"]['mark'] + '\u0020'
                        char = color.setForeground('red', symbol)

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

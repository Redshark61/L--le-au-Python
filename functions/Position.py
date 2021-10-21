def position(x: int, y: int, text: str) -> str:
    """
    Permet d'afficher un texte aux coordonnées x et y
    """
    return f"\033[{y};{x}H{text}"


def printBox(xStart: int, YStart: int, width: int, height: int) -> int:
    """
    Permet d'afficher une boite aux coordonnées `x` et `y` (en haut à gauche) de longueur `width` et hauteur `height`
    """

    # Ligne du haut
    for i in range(xStart+1, xStart+width):
        print(f"\033[{YStart};{i}H\u2550")

    # Ligne du bas
    for i in range(xStart+1, xStart+width):
        print(f"\033[{YStart+height};{i}H\u2550")

    # Ligne de gauche
    for i in range(YStart+1, YStart+height):
        print(f"\033[{i};{xStart}H\u2551")

    # Ligne de droite
    for i in range(YStart, YStart+height):
        print(f"\033[{i};{xStart+width}H\u2551")

    # Les quatres angles
    print(f"\033[{YStart};{xStart}H\u2554")
    print(f"\033[{YStart};{xStart+width}H\u2557")
    print(f"\033[{YStart+height};{xStart}H\u255a")
    print(f"\033[{YStart+height};{xStart+width}H\u255d")


def clearBoxWithLine(line: int, n: int) -> int:
    """
    Return the number of line you need to add if you want to display long text inside a box, and clear the box if the text is too long
    """
    if line+n >= 30:
        for i in range(105, 153):
            for j in range(2, 36):
                print(position(x=i, y=j, text=" "))
        return 0
    return line + n


def clearBox():
    """
    Clear the right panel
    """
    for i in range(105, 153):
        for j in range(2, 36):
            print(position(x=i, y=j, text=" "))


def clearBottomPanel():
    """
    Clear the bottom panel
    """
    for i in range(3, 100):
        for j in range(31, 40):
            print(position(x=i, y=j, text=" "))

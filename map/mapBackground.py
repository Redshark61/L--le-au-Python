from functions.emojiDecoder import emojiDecoder
from functions import config


def mapBackground(color: type, char: str, map: str, j: int, row: int, col: int) -> str:
    """
    Function wich return a map (string) by checking the number of the current cell (j) and chnaging it's color, or symbol to be displayed
    """

    # Stone floor
    if j == 1:
        map += color.setBackground("brightGray", char)
    # River
    elif j == 2:
        map += color.setBackground('brightCyan', char)
    # Sea
    elif j == 3:
        map += color.setBackground('darkBlue', char)
    # Sand
    elif j == 4:
        map += color.setBackground('brightYellow', char)
    # Palm tree
    elif j == 5:
        # If the cell is a palm tree, but the player stand here, then dont display the tree, but player's emoji
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            map += color.setBackground('darkGreen', char)
        else:
            map += color.setBackground('darkGreen', emojiDecoder('f09f8cb4'))
    # Ground
    elif j == 6:
        map += color.setBackground('darkGreen', char)
    # River bridge
    elif j == 7:
        # Same as the palm tree
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            map += color.setBackground('brightCyan', char)
        else:
            map += color.setBackground('brightCyan', emojiDecoder('f09f9fab'))
    # Bridge on lava displayed
    elif j == 10 and config.key == 3:
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            map += color.setBackground('darkYellow', char)
        else:
            map += color.setBackground('darkYellow', emojiDecoder('f09f9fab'))
    # Birdge on lava not displayed
    elif j == 10 and config.key < 3:
        map += color.setBackground('darkYellow', char)
    # Lava
    elif j == 8:
        map += color.setBackground('darkYellow', char)
    # Lock closed
    elif j == 9 and config.key < 3:
        map += color.setBackground('darkYellow', emojiDecoder("f09f9492"))
    # Lock opened
    elif j == 9 and config.key == 3:
        map += color.setBackground('darkYellow', emojiDecoder("f09f9493"))
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            config.isLeaving = True
            return map

    return map

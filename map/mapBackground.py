from functions.emojiDecoder import emojiDecoder
from functions import config


def mapBackground(color: type, char: str, map: str, j: int, row: int, col: int) -> str:
    """
    Function wich return a map (string) by checking the number of the current cell (j) and chnaging it's color, or symbol to be displayed
    """
    if j == 1:
        map += color.setBackground("brightGray", char)
    elif j == 2:
        map += color.setBackground('brightCyan', char)
    elif j == 3:
        map += color.setBackground('darkBlue', char)
    elif j == 4:
        map += color.setBackground('brightYellow', char)
    elif j == 5:
        # If the cell is a palm tree, but the player stand here, then dont display the tree, but player's emoji
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            map += color.setBackground('darkGreen', char)
        else:
            map += color.setBackground('darkGreen', emojiDecoder('f09f8cb4'))
    elif j == 6:
        map += color.setBackground('darkGreen', char)
    elif j == 7:
        if row == config.playerCoord[1] and col == config.playerCoord[0]:
            map += color.setBackground('brightCyan', char)
        else:
            map += color.setBackground('brightCyan', emojiDecoder('f09f9fab'))

    return map

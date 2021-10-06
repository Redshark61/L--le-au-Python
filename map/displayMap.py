from functions.Colors import Colors
from functions.Position import *
from map.startQuest import startQuest
from map.emojiDecoder import emojiDecoder


def displayMap(data: dict, coord: dict, playerX: int, playerY: int, questToDo: list, questDone: list) -> None:
    """
    Display the map using the map.json. Each number is for a particular color. By default, the characters are just 2 spaces
    but it can be emoji.

    It also stores the different quest already done, and handle if it needs to be played or not.
    """

    color = Colors
    color.init()

    # Move the cursor all the way to the top + where he currently is
    print((len(data)+3) * "\033[A", end="")

    row = 0
    map = ''
    # for each line of the map
    for i in data:
        col = 0

        # For each cell of the line
        for j in i:
            # Main character is 2 spaces
            char = '\u0020\u0020'

            # If current cell is a played quest, then check it
            if len(questDone) > 0:
                for quest in questDone:
                    if row == quest[1] and col == quest[0]:
                        char = emojiDecoder("e29c85")  # Green check

            # For every positioned element in the json
            for item in coord:

                # Every emoji needs to be convert from hex to string in order to properly display
                symbol = emojiDecoder(coord[item]['mark'])

                # If the current cell is not a player, then we change its value to an emojie, if needed
                if item != "player":
                    if row == coord[item]['coords'][1] and col == coord[item]['coords'][0]:
                        char = symbol
                # If the current cell is the player, then we change its char to be the player's emoji
                else:
                    if row == playerY and col == playerX:
                        char = symbol

            # Change the background depending on the color code of the json map
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
                if row == playerY and col == playerX:
                    map += color.setBackground('darkGray', char)
                else:
                    map += color.setBackground('darkGray', emojiDecoder('f09f8cb4'))
            elif j == 6:
                map += color.setBackground('darkGray', char)

            col += 1

        row += 1
        map += '\n'
    print(map)

    # Once the map is displayed, we check if the player's position is a quest to do
    for index, quest in enumerate(questToDo):
        quest = list(quest.keys())[0]
        # If it is, then we play the quest
        if (playerY == questToDo[index][quest][1] and playerX == questToDo[index][quest][0]):
            questToDo, playerX = startQuest(coord, index, questToDo, playerX, playerY, quest, questDone)
    # In either case we return the questToDo and the next player's position
    return questToDo, playerX

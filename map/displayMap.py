from functions.Colors import Colors
from functions.Position import position
from map.startQuest import startQuest
from functions.emojiDecoder import emojiDecoder
from map.printMonkeys import printMonkeys
from map.mapBackground import mapBackground
from functions import config


def displayMap(playerFace: str = None) -> None:
    """
    Display the mapBg using the mapBg.json. Each number is for a particular color. By default, the characters are just 2 spaces
    but it can be emoji.

    It also stores the different quest already done, and handle if it needs to be played or not.
    """

    color = Colors()
    color.init()

    # Move the cursor all the way to the top
    print(position(1, 0, ''))

    row = 0
    mapBg = ''
    isQuestDone = False

    # for each line of the mapBg
    for i in config.data:
        col = 0

        # For each cell of the line
        for j in i:
            # Main character is 2 spaces
            char = '\u0020\u0020'

            for index, _ in enumerate(config.createdItems):
                name = list(config.createdItems[index].keys())[0]
                currentitemPosX = config.createdItems[index][name][0]
                currentitemPosY = config.createdItems[index][name][1]
                for baseItem in config.currentItems:
                    if name == baseItem:
                        if col == currentitemPosX and row == currentitemPosY:
                            char = emojiDecoder(config.currentItems[name]["mark"])
                        if currentitemPosX == config.playerCoord[0] and currentitemPosY == config.playerCoord[1]:
                            config.pickedUpItem.append(config.currentItems[name])
                            del config.createdItems[index]
                            break

            # For every positioned element in the json
            for element in config.coord:

                # Every emoji needs to be convert from hex to string in order to properly display
                symbol = emojiDecoder(config.coord[element]['mark'])

                # If the current cell is not a player, then we change its value to an emojie, if needed
                if element != "player":
                    if row == config.coord[element]['coords'][1] and col == config.coord[element]['coords'][0]:
                        char = symbol
                # If the current cell is the player, then we change its char to be the player's emoji
                else:
                    if row == config.playerCoord[1] and col == config.playerCoord[0]:
                        if j == 3 or j == 2 or j == 8:
                            config.playerCoord[0] = config.prevPlayerCoord[0]
                            config.playerCoord[1] = config.prevPlayerCoord[1]
                            return
                        elif playerFace is not None:
                            char = playerFace
                        else:
                            char = symbol

            if len(config.questDone) > 0:
                for quest in config.questDone:
                    if row == quest[1] and col == quest[0]:
                        char = emojiDecoder("e29c85")  # Green check

            # Change the background depending on the color code of the json mapBg
            mapBg = mapBackground(color, char, mapBg, j, row, col)

            col += 1

        row += 1
        mapBg += '\n'
    print(mapBg)

    # Once the mapBg is displayed, we check if the player's position is a quest to do
    for index, quest in enumerate(config.questToDo):
        quest = list(quest.keys())[0]

        # If it is, then we play the quest
        if (config.playerCoord[1] == config.questToDo[index][quest][1] and config.playerCoord[0] == config.questToDo[index][quest][0]):
            if list(config.questToDo[index].keys())[0] == 'fizzBuzz':
                printMonkeys(color, index, quest)

            isQuestDone = startQuest(index, quest)

    return isQuestDone

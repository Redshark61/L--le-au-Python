from functions.Colors import Colors
from functions.Position import position
from map.startQuest import startQuest
from functions.emojiDecoder import emojiDecoder
from map.printMonkeys import printMonkeys
from map.mapBackground import mapBackground
from functions import config


def displayMap(playerFace: str = None) -> bool:
    """
    Display the mapBg using mapBg.json. Each number is for a particular color. By default, the characters are just 2 spaces
    but it can be emoji.

    It also stores the different quest already done, and handle if it needs to be played or not.
    """

    color = Colors()
    color.init()

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

            # Loop through all the items still created
            for index, _ in enumerate(config.createdItems):
                # Get name and position
                name = list(config.createdItems[index].keys())[0]
                currentitemPosX = config.createdItems[index][name][0]
                currentitemPosY = config.createdItems[index][name][1]
                # If the position currently printed is same s the item
                if col == currentitemPosX and row == currentitemPosY:
                    # Then dont print space but the image of the item
                    char = emojiDecoder(config.currentItems[name]["mark"])

                # If the position of the item is the same as the player
                if currentitemPosX == config.playerCoord[0] and currentitemPosY == config.playerCoord[1]:
                    # If the inventory is not full
                    if config.inventorySize < config.inventoryMax:
                        config.inventorySize += config.currentItems[name]["size"]
                        config.pickedUpItem.append(config.currentItems[name])
                        # Delete the item from the items on the map
                        del config.createdItems[index]
                        break
                    # Else you are full
                    print(position(3, 38, color.setBackground('red', 'Tu es plein')))

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
                        # If the player want to walk on river, sea or lava
                        if j in (3, 2, 8):
                            config.playerCoord[0] = config.prevPlayerCoord[0]
                            config.playerCoord[1] = config.prevPlayerCoord[1]
                            return
                        # Set the player face
                        if playerFace is not None:
                            char = playerFace
                        else:
                            char = emojiDecoder(config.playerMark)

            # If there are quest done
            if len(config.questDone) > 0:
                for quest in config.questDone:
                    # If the current quest is done, check it
                    if row == quest[1] and col == quest[0]:
                        char = emojiDecoder("e29c85")  # Green check

            # Change the background depending on the color code of the json mapBg
            mapBg = mapBackground(color, char, mapBg, j, row, col)

            col += 1

        row += 1
        mapBg += '\n'

    print(position(1, 1, mapBg))

    # Once the mapBg is displayed, we check if the player's position is a quest to do
    for index, quest in enumerate(config.questToDo):
        quest = list(quest.keys())[0]

        # If it is, then we play the quest
        if (config.playerCoord[1] == config.questToDo[index][quest][1] and config.playerCoord[0] == config.questToDo[index][quest][0]):
            # If the quest is the fizzbuzz, display monkyes around the player
            if list(config.questToDo[index].keys())[0] == 'fizzBuzz':
                printMonkeys(color, index, quest)

            isQuestDone = startQuest(index, quest)

    return isQuestDone

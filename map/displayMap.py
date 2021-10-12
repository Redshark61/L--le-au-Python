from functions.Colors import Colors
from functions.Position import *
from map.startQuest import startQuest
from functions.emojiDecoder import emojiDecoder
from map.printMonkeys import printMonkeys
from map.mapBackground import mapBackground


def displayMap(data: dict, coord: dict, playerCoord: list, questToDo: list, questDone: list, prevPlayerCoord: int, vitalSigns: dict[int], createdItems, currentItems, pickedUpItem, playerFace: str = None) -> None:
    """
    Display the map using the map.json. Each number is for a particular color. By default, the characters are just 2 spaces
    but it can be emoji.

    It also stores the different quest already done, and handle if it needs to be played or not.
    """

    color = Colors
    color.init()

    # Move the cursor all the way to the top
    print(position(1, 0, ''))

    row = 0
    map = ''
    isQuestDone = False

    # for each line of the map
    for i in data:
        col = 0

        # For each cell of the line
        for j in i:
            # Main character is 2 spaces
            char = '\u0020\u0020'

            for index, item in enumerate(createdItems):
                name = list(createdItems[index].keys())[0]
                currentitemPosX = createdItems[index][name][0]
                currentitemPosY = createdItems[index][name][1]
                for baseItem in currentItems:
                    if name == baseItem:
                        if col == currentitemPosX and row == currentitemPosY:
                            char = emojiDecoder(currentItems[name]["mark"])
                        if currentitemPosX == playerCoord[0] and currentitemPosY == playerCoord[1]:
                            pickedUpItem.append(currentItems[name])
                            if currentItems[name]["type"] == "goodFood":
                                vitalSigns['foodMax'] += currentItems[name]['food']
                                del createdItems[index]
                            if currentItems[name]["type"] == "goodDrink":
                                vitalSigns['waterMax'] += currentItems[name]['water']
                                del createdItems[index]
                            break

            # For every positioned element in the json
            for element in coord:

                # Every emoji needs to be convert from hex to string in order to properly display
                symbol = emojiDecoder(coord[element]['mark'])

                # If the current cell is not a player, then we change its value to an emojie, if needed
                if element != "player":
                    if row == coord[element]['coords'][1] and col == coord[element]['coords'][0]:
                        char = symbol
                # If the current cell is the player, then we change its char to be the player's emoji
                else:
                    if row == playerCoord[1] and col == playerCoord[0]:
                        if j == 3 or j == 2:
                            return questToDo, prevPlayerCoord, isQuestDone, vitalSigns, currentItems, pickedUpItem
                        elif playerFace != None:
                            char = playerFace
                        else:
                            char = symbol

            if len(questDone) > 0:
                for quest in questDone:
                    if row == quest[1] and col == quest[0]:
                        char = emojiDecoder("e29c85")  # Green check

            # Change the background depending on the color code of the json map
            map = mapBackground(color, char, map, j, row, col, playerCoord)

            col += 1

        row += 1
        map += '\n'
    print(map)

    # Once the map is displayed, we check if the player's position is a quest to do
    for index, quest in enumerate(questToDo):
        quest = list(quest.keys())[0]

        # If it is, then we play the quest
        if (playerCoord[1] == questToDo[index][quest][1] and playerCoord[0] == questToDo[index][quest][0]):
            if list(questToDo[index].keys())[0] == 'fizzBuzz':
                printMonkeys(color, questToDo, index, quest)

            questToDo, playerCoord[1], isQuestDone = startQuest(coord, index, questToDo, playerCoord[1], quest, questDone)

    # In either case we return the questToDo and the next player's position
    return questToDo, playerCoord, isQuestDone, vitalSigns, currentItems, pickedUpItem

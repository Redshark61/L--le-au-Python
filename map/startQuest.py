import time
from functions.Position import clearBox
from functions import config
from functions.drawRightPanel import drawRightPanel


def startQuest(index: int, quest: dict) -> bool:
    clearBox()
    # Import the given file
    module = __import__(f"{config.coord[quest]['folder']}.{config.coord[quest]['mainFile']}", fromlist=[None])
    hasWon = module.main()
    config.vitalSigns['foodMax'] = config.foodMax - 20
    config.vitalSigns['waterMax'] = config.waterMax - 20
    isQuestDone = True
    # If he has won he get a key and the quest is not to do anymore
    if hasWon:
        config.questDone.append(config.questToDo[index][quest])
        config.questToDo.pop(index)
        config.key += 1
        time.sleep(2)

    config.playerCoord[1] += 1

    clearBox()
    drawRightPanel()
    return isQuestDone

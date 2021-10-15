import time
from typing import Union
from functions.Position import clearBox
import functions.config as config
from functions.drawRightPanel import drawRightPanel


def startQuest(index: int, quest: dict) -> Union[list[dict], int, bool]:
    clearBox()
    module = __import__(f"{config.coord[quest]['folder']}.{config.coord[quest]['mainFile']}", fromlist=[None])
    hasWon = module.main()
    config.vitalSigns['foodMax'] = 90
    config.vitalSigns['waterMax'] = 90
    isQuestDone = True
    if hasWon:
        config.questDone.append(config.questToDo[index][quest])
        config.questToDo.pop(index)
        config.key += 1
        time.sleep(2)

    config.playerCoord[1] += 1

    clearBox()
    drawRightPanel()
    return isQuestDone

import time
from typing import Union
from functions.Position import clearBox
import functions.config as config


def startQuest(index: int, quest: dict) -> Union[list[dict], int, bool]:
    clearBox()
    module = __import__(f"{config.coord[quest]['folder']}.{config.coord[quest]['mainFile']}", fromlist=[None])
    hasWon = module.main()
    isQuestDone = True
    if hasWon:
        config.questDone.append(config.questToDo[index][quest])
        config.questToDo.pop(index)
        time.sleep(2)

    config.playerCoord[1] += 1

    clearBox()
    return isQuestDone

import time
from functions.Position import clearBox
from typing import Union


def startQuest(coord: dict, index: int, questToDo: list[dict], playerX: int, playerY: int, quest: dict, questDone: list) -> Union[list[dict], int, bool]:
    clearBox()
    module = __import__(f"{coord[quest]['folder']}.{coord[quest]['mainFile']}", fromlist=[None])
    hasWon = module.main()
    isQuestDone = True
    if hasWon:
        questDone.append(questToDo[index][quest])
        questToDo.pop(index)
        time.sleep(2)

    clearBox()
    return questToDo, playerY+1, isQuestDone

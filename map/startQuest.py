import time
from functions.Position import clearBox


def startQuest(coord, index, questToDo, playerX, playerY, quest, questDone):
    clearBox()
    module = __import__(f"{coord[quest]['folder']}.{coord[quest]['mainFile']}", fromlist=[None])
    isWon = module.main()
    if isWon:
        questDone.append(questToDo[index][quest])
        questToDo.pop(index)
        time.sleep(2)
        clearBox()

    return questToDo, playerX+1

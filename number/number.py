import os
from random import randint
import time
from functions import config
from functions.Position import clearBox, position, clearBoxWithLine
from functions.checkLength import checkLength
from functions.checkMod import checkMod


def main() -> None:

    fileName = os.path.basename(__file__)[:-3]
    text = checkLength(fileName)
    for index, line in enumerate(text):
        print(position(105, 4+index+1, line), flush=True)
        time.sleep(0.2)

    clearBox()

    data = checkMod("number")
    maxTry = data["maxTry"]
    maxRandom = data["maxRandom"]
    numberOfGame = data["numberOfGame"]

    tried = 0
    for _ in range(numberOfGame):
        clearBox()
        answer = ''
        rand = randint(0, maxRandom)

        line = -3
        while(answer != rand and tried < maxTry):
            line = clearBoxWithLine(line, 3)
            print(config.visibleCursor)
            print(position(x=105, y=3, text='Quel est mon nombre ?'))
            answer = int(input(position(x=105, y=4+line, text='')))
            print(config.hiddenCursor)

            tried += 1
            if(answer < rand and tried < maxTry):
                print(position(x=105, y=5+line, text="Mon nombre est plus grand"))
                print(position(x=105, y=6+line, text=f"Attention, tu n'as plus que {maxTry-tried} essais"))
            elif(answer > rand and tried < maxTry):
                print(position(x=105, y=5+line, text="Mon nombre est plus petit"))
                print(position(x=105, y=6+line, text=f"Attention, tu n'as plus que {maxTry-tried} essais"))
            elif(answer == rand and tried <= maxTry):
                print(position(x=105, y=6+line, text="Tu as gagné !"))
                break
        else:
            print(position(x=105, y=6+line, text="Tu as perdu !"))
            time.sleep(2)
            return False

    return True

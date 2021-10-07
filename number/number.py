import os
from random import randint
import time
from functions.Position import *
from functions.checkLength import checkLength


def main() -> None:

    fileName = os.path.basename(__file__)[:-3]
    text = checkLength(fileName)
    for index, line in enumerate(text):
        print(position(105, 4+index+1, line), flush=True)
        time.sleep(0.2)

    clearBox()

    print("\x1b[?25h")
    tried = 0
    for i in range(3):
        answer = ''
        rand = randint(0, 100)

        line = -3
        while(answer != rand or tried >= 20):
            line = clearBoxWithLine(line, 3)
            print(position(x=105, y=3, text='Quel est mon nombre ?'))
            answer = int(input(position(x=105, y=4+line, text='')))

            if(answer < rand):
                tried += 1
                print(position(x=105, y=5+line, text="Mon nombre est plus grand"))
                print(position(x=105, y=6+line, text=f"Attention, tu n'as plus que {20-tried} essais"))
            elif(answer > rand):
                tried += 1
                print(position(x=105, y=5+line, text="Mon nombre est plus petit"))
                print(position(x=105, y=6+line, text=f"Attention, tu n'as plus que {20-tried} essais"))
            else:
                print(position(x=105, y=6+line, text="Tu as gagné !"))
                time.sleep(2)
                clearBox()
                print('\x1b[?25l')

    return True

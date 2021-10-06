from random import randint
from functions.Position import *


def main() -> None:
    print("\x1b[?25h")
    answer = ''
    rand = randint(0, 100)

    line = -2
    while(answer != rand):
        line = clearBoxWithLine(line, 2)
        print(position(x=105, y=3, text='Quel est mon nombre ?'))
        answer = int(input(position(x=105, y=4+line, text='')))

        if(answer < rand):
            print(position(x=105, y=5+line, text="Mon nombre est plus grand"))
        elif(answer > rand):
            print(position(x=105, y=5+line, text="Mon nombre est plus petit"))
        else:
            print(position(x=105, y=5+line, text="Tu as gagné !"))
            print('\x1b[?25l')

            return True

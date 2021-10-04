from random import randint
from .. import functions


def number() -> None:
    answer = ''
    rand = randint(0, 100)

    while(answer != rand):
        answer = int(input('Quel est mon nombre ? \n'))

        if(answer < rand):
            print("Mon nombre est plus grand")
        elif(answer > rand):
            print("Mon nombre est plus petit")
        else:
            print("Tu as gagné !")


if __name__ == '__main__':
    functions.Clear.clear()
    number()

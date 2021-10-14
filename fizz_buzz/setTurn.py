from functions.Position import position
from fizz_buzz import configFizzBuzz as conf


def setTurn(data: dict, lineTurn: int):

    # Si l'conf.index du joueur est compris entre 0 et le nombre de singes max,
    # alors cela signifie que c'est un singe qui joue
    if 'singe' in conf.index:
        conf.turnData = data["monkeys"]
        conf.turn = "monkey"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du singe"))

    # Sinon si l'conf.index est l'avant dernier, alors c'est le boss qui joue
    elif conf.index == 'boss':
        conf.turnData = data['boss']
        conf.turn = "boss"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du boss"))

    # Sinon c'est le joueur qui joue
    else:
        conf.turnData = data['player']
        conf.turn = "player"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du joueur"))

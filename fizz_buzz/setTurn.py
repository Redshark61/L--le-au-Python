from functions.Position import position
from fizz_buzz import configFizzBuzz as conf


def setTurn(data: dict, lineTurn: int) -> None:
    """
    Set the turn of the player, if it's the monkeys, player or boss
    """

    # if it's the turn of a monkey
    if 'singe' in conf.index:
        conf.turnData = data["monkeys"]
        conf.turn = "monkey"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du singe"))

    # if it's the turn of the boss
    elif conf.index == 'boss':
        conf.turnData = data['boss']
        conf.turn = "boss"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du boss"))

    # if it's the turn of the player
    else:
        conf.turnData = data['player']
        conf.turn = "player"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du joueur"))

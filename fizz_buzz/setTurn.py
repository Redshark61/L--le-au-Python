from functions.Position import position


def setTurn(index: str, data: dict, lineTurn: int) -> tuple[dict, str]:

    # Si l'index du joueur est compris entre 0 et le nombre de singes max,
    # alors cela signifie que c'est un singe qui joue
    if 'singe' in index:
        turnData = data["monkeys"]
        turn = "monkey"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du singe"))

    # Sinon si l'index est l'avant dernier, alors c'est le boss qui joue
    elif index == 'boss':
        turnData = data['boss']
        turn = "boss"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du boss"))

    # Sinon c'est le joueur qui joue
    else:
        turnData = data['player']
        turn = "player"
        print(position(x=105, y=3+lineTurn, text="C'est au tour du joueur"))

    return turnData, turn

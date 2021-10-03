def setTurn(index: int, data: dict, turns: list) -> tuple[dict, str]:

    # Si l'index du joueur est compris entre 0 et le nombre de singes max,
    # alors cela signifie que c'est un singe qui joue
    if index >= 0 and index < data['monkeys']['number']:
        turnData = data["monkeys"]
        turn = "monkey"
        print("C'est au tour du singe")

    # Sinon si l'index est l'avant dernier, alors c'est le boss qui joue
    elif index == len(turns)-2:
        turnData = data['boss']
        turn = "boss"
        print("C'est au tour du boss")

    # Sinon c'est le joueur qui joue
    else:
        turnData = data['player']
        turn = "player"
        print("C'est au tour du joueur")

    return turnData, turn

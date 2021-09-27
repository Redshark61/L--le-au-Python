def setTurn(index, data, numberMonkeys, turns):
    if index >= 0 and index < data['monkeys']['number']:
        turnData = data["monkeys"]
        turn = "monkey"
        print("C'est au tour du singe")
    elif index == len(turns)-2:
        turnData = data['boss']
        turn = "boss"
        print("C'est au tour du boss")
    else:
        turnData = data['player']
        turn = "player"
        print("C'est au tour du joueur")

    return turnData, turn

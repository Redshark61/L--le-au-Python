def setTurn(index, data):
    if index >= 0 and index < 9:
        turnData = data["monkeys"]
        turn = "monkey"
        print("C'est au tour du singe")
    elif index > 9 and index < 10:
        turnData = data['boss']
        turn = "boss"
        print("C'est au tour du boss")
    else:
        turnData = data['player']
        turn = "player"
        print("C'est au tour du joueur")

    return turnData, turn

def deletePlayer(index: str, turn: str, playerLeft: list, numberMonkeys: int, isPlayerWrong: bool) -> tuple[bool, list, int]:
    # Si c'était au tour d'un singe, on supprime le premier élément (qui de toute façon est un singe)
    if turn == "monkey":
        del playerLeft[index]
        numberMonkeys -= 1

    # Si c'était au tour du boss, on supprime l'avant dernier élément
    elif turn == "boss":
        del playerLeft[index]

    # Si c'était au tour du joueur, on supprime le dernier élément
    else:
        isPlayerWrong = True

    return isPlayerWrong, playerLeft, numberMonkeys

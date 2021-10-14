from fizz_buzz import configFizzBuzz as conf


def deletePlayer():
    # Si c'était au tour d'un singe, on supprime le premier élément (qui de toute façon est un singe)
    if conf.turn == "monkey":
        del conf.playerLeft[conf.index]
        conf.numberMonkeys -= 1

    # Si c'était au tour du boss, on le supprime
    elif conf.turn == "boss":
        del conf.playerLeft[conf.index]
        conf.numberMonkeys -= 1

    # Si c'était au tour du joueur, on supprime le dernier élément
    else:
        conf.isPlayerWrong = True

    if conf.numberMonkeys == 0:
        return True
    return False

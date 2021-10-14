from fizz_buzz import configFizzBuzz as conf


def deletePlayer() -> bool:
    # If the current player is a monkey or the boss, we just delete him
    if conf.turn == "monkey" or conf.turn == "boss":
        del conf.playerLeft[conf.index]
        conf.numberMonkeys -= 1

    # else it's the player, and he is wrong
    else:
        conf.isPlayerWrong = True

    if conf.numberMonkeys == 0:
        return True
    return False

from random import randint
from functions.Position import position
from fizz_buzz.deletePlayer import deletePlayer
from fizz_buzz import configFizzBuzz as conf


def checkChances(line, color, typeGame, n=''):
    if randint(0, 100) < conf.chance:
        print(position(x=105, y=4+line, text=color.setForeground('brightYellow', conf.turnData[typeGame]+str(n)+"\n")))
    else:
        print(position(x=105, y=4+line, text=color.setForeground('red', conf.turnData['loose'])))
        noMoreMonkeys = deletePlayer()
        if conf.isPlayerWrong or noMoreMonkeys:
            return True
    return False

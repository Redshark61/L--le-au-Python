from random import randint
from functions.Colors import Colors
from functions.Position import position
from fizz_buzz.deletePlayer import deletePlayer
from fizz_buzz import configFizzBuzz as conf


def checkChances(line: int, color: Colors, typeGame: str, n: str = '') -> bool:
    """
    Get the line to know were the text will be printed, the color to print colors and the type of turn : fizz, buzz, fizzbuzz or the number. If it's the number, you must pass the ``n`` parameter.
    """
    # If the player play
    if randint(0, 100) < conf.chance:
        print(position(x=105, y=4+line, text=color.setForeground('brightYellow', conf.turnData[typeGame]+str(n)+"\n")))
    # If he loose
    else:
        print(position(x=105, y=4+line, text=color.setForeground('red', conf.turnData['loose'])))
        noMoreMonkeys = deletePlayer()
        if conf.isPlayerWrong or noMoreMonkeys:
            return True
    return False

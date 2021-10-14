#coding: utf-8
import os.path
import time
import copy
from random import randint
from fizz_buzz.jsonFetch import jsonFetch
from fizz_buzz.setTurn import setTurn
from functions.Colors import Colors
from functions.Position import position, clearBoxWithLine, clearBox
from functions.checkLength import checkLength
from fizz_buzz import configFizzBuzz as conf
from fizz_buzz.checkChances import checkChances


def main() -> None:
    conf.numberMonkeys, conf.chance = 0, 0
    conf.playerLeft, conf.turnData = [], []
    conf.index, conf.turn = '', ''
    conf.isPlayerWrong = False

    # Enable the colors to be displayed
    color = Colors()
    color.init()

    # Get the story associated to the file
    fileName = os.path.basename(__file__)[:-3]
    text = checkLength(fileName)

    # Print the story
    for index, line in enumerate(text):
        print(position(105, 4+index+1, line), flush=True)
        time.sleep(0.2)

    # Cleat the right panel
    clearBox()

    # Get all the data from the json
    maxMonkey, minMonkey, maxBoss, minBoss, maxPlayer, minPlayer, data = jsonFetch()

    # Chances to win are random
    chanceMonkey = randint(minMonkey, maxMonkey+1)
    chanceBoss = randint(minBoss, maxBoss+1)
    chancePlayer = randint(minPlayer, maxPlayer+1)

    n = 1

    # Creation of the turn list wich store who is playing, and what is its chances
    turns = {}
    for i in range(data['monkeys']['number']):
        turns['singe'+str(i)] = chanceMonkey
    turns['boss'] = chanceBoss
    turns['joueur'] = chancePlayer

    # We create a deep copy of the turns list bcz we need to be able to pop player from the list without breaking the loop
    conf.playerLeft = copy.deepcopy(turns)
    conf.isPlayerWrong = False
    line = -4
    while conf.numberMonkeys > 0 and not conf.isPlayerWrong:

        # For each player
        for conf.index, conf.chance in turns.items():
            time.sleep(1)

            line = clearBoxWithLine(line, 4)
            print("\033[40m")
            setTurn(data, line)

            # If it's FizzBuzz
            if n % 3 == 0 and n % 5 == 0:
                hasFail = checkChances(line, color, 'winFizzBuzz')

            # If it's Fizz
            elif n % 3 == 0:
                hasFail = checkChances(line, color, 'winFizz')

            # If it's Buzz
            elif n % 5 == 0:
                hasFail = checkChances(line, color, 'winBuzz')

            # If it's the number
            else:
                hasFail = checkChances(line, color, 'play', n)

            # If there is a reason to stop the loop (no more monkeys or player wrong)
            if hasFail:
                break
            print(position(x=105, y=5+line, text=f"Il reste {conf.numberMonkeys} singes"))
            n += 1
        # Update the list of players left
        turns = copy.deepcopy(conf.playerLeft)

    # If there is no more monkeys, it's a win
    if conf.numberMonkeys == 0:
        print(position(x=105, y=5+line, text=color.setForeground('brightGreen', 'Tous les singes ont été éliminé ! Tu as gagné !')))
        return True
    # Otherwise it's a loose
    print(position(x=105, y=5+line, text=color.setForeground('red', "Tu as perdu !")))
    time.sleep(2)
    return False

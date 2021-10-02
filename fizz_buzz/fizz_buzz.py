import json
from random import randint
from fizz_buzz.setTurn import setTurn
import os.path
import copy
from functions.Colors import Colors


def fizzBuzz():

    color = Colors
    color.init()

    if os.path.isfile("mods/fizzBuzz.json"):
        with open('mods/fizzBuzz.json') as file:
            data = json.load(file)
    else:
        with open("data/fizzBuzz.json") as file:
            data = json.load(file)

    numberMonkeys = data["monkeys"]["number"] + 1

    maxMonkey = data["monkeys"]["maxChance"]
    minMonkey = data["monkeys"]["minChance"]

    maxBoss = data["boss"]["maxChance"]
    minBoss = data["boss"]["minChance"]

    maxPlayer = data["player"]["maxChance"]
    minPlayer = data["player"]["minChance"]

    chanceMonkey = randint(minMonkey, maxMonkey+1)
    chanceBoss = randint(minBoss, maxBoss+1)
    chancePlayer = randint(minPlayer, maxPlayer+1)

    n = 1
    playerIsWrong = False

    turns = [chanceMonkey]*(data['monkeys']['number']) + \
        [chanceBoss, chancePlayer]

    playerLeft = copy.deepcopy(turns)
    while numberMonkeys > 0 and not playerIsWrong:

        for index, chance in enumerate(turns):

            turnData, turn = setTurn(index, data, numberMonkeys, turns)

            if n % 3 == 0 and n % 5 == 0:
                if randint(0, 100) < chance:
                    print(color.setForeground('brightCyan', turnData["winFizz"] + turnData["winBuzz"]))

                else:
                    print(color.setForeground('red', turnData['loose']))

                    if turn == "monkey":
                        del playerLeft[0]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del playerLeft[-2]

                    else:
                        playerIsWrong = True
                        break

            elif n % 3 == 0:

                if randint(0, 100) < chance:
                    print(color.setForeground('brightCyan', turnData["winFizz"]))

                else:
                    print(color.setForeground('red', turnData['loose']))

                    if turn == "monkey":
                        del playerLeft[0]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del playerLeft[-2]

                    else:
                        playerIsWrong = True
                        break

            elif n % 5 == 0:

                if randint(0, 100) < chance:
                    print(color.setForeground('brightCyan', turnData["winBuzz"]))
                else:
                    print(color.setForeground('red', turnData['loose']))

                    if turn == "monkey":
                        del playerLeft[0]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del playerLeft[-2]

                    else:
                        playerIsWrong = True
                        break

            else:

                if randint(0, 100) < chance:
                    print(color.setForeground('brightYellow', turnData['play'] + str(n) + "\n"))

                else:
                    print(color.setForeground('red', turnData['loose']))

                    if turn == "monkey":
                        del playerLeft[0]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del playerLeft[-2]

                    else:
                        playerIsWrong = True
                        break

            print(f"Il reste {numberMonkeys} singes")
            n += 1
        turns = copy.deepcopy(playerLeft)

    if numberMonkeys == 0:
        print(color.setForeground('brightGreen', 'Tous les singes ont été éliminé ! \nTu as gagné !'))
    else:
        print(color.setForeground('red', "Tu as perdu !"))

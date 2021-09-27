import json
from random import randint
from fizz_buzz.setTurn import setTurn
import colorama
from colorama import Fore, Back, Style
import os.path
import copy

colorama.init(autoreset=True)


def fizzBuzz():
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
                    print(Fore.LIGHTCYAN_EX +
                          turnData["winFizz"] + turnData["winBuzz"])

                else:
                    print(Fore.RED + turnData['loose'])

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
                    print(Fore.LIGHTCYAN_EX + turnData["winFizz"])

                else:
                    print(Fore.RED + turnData['loose'])

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
                    print(Fore.LIGHTCYAN_EX + turnData["winBuzz"])

                else:
                    print(Fore.RED + turnData['loose'])

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
                    print(Fore.LIGHTYELLOW_EX +
                          turnData['play'] + str(n) + "\n")

                else:
                    print(Fore.RED + turnData['loose'])

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
        print(Fore.GREEN + 'Tous les singes ont été éliminé ! \n Tu as gagné !')
    else:
        print(Fore.RED + "Tu as perdu")

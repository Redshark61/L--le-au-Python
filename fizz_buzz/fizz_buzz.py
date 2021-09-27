import json
from random import randint
from fizz_buzz.setTurn import setTurn
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def fizzBuzz():
    with open('data/fizzBuzz.json') as file:
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

    n = 0
    playerIsWrong = False

    turns = [chanceMonkey]*9 + [chanceBoss, chancePlayer]
    while numberMonkeys > 0 and not playerIsWrong:

        for index, chance in enumerate(turns):

            turnData, turn = setTurn(index, data)

            if n % 3 == 0 and n % 5 == 0:
                if randint(0, 100) < chance:
                    print(Fore.LIGHTCYAN_EX +
                          turnData["winFizz"] + turnData["winBuzz"])

                else:
                    print(Fore.RED + turnData['loose'])

                    if turn == "monkey":
                        del turns[index]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del turns[index]

                    else:
                        playerIsWrong = True
                        break

            elif n % 3 == 0:

                if randint(0, 100) < chance:
                    print(Fore.LIGHTCYAN_EX + turnData["winFizz"])

                else:
                    print(Fore.RED + turnData['loose'])

                    if turn == "monkey":
                        del turns[index]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del turns[index]

                    else:
                        playerIsWrong = True
                        break

            elif n % 5 == 0:

                if randint(0, 100) < chance:
                    print(Fore.LIGHTCYAN_EX + turnData["winBuzz"])

                else:
                    print(Fore.RED + turnData['loose'])

                    if turn == "monkey":
                        del turns[index]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del turns[index]

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
                        del turns[index]
                        numberMonkeys -= 1

                    elif turn == "boss":
                        del turns[index]

                    else:
                        playerIsWrong = True
                        break

            print(f"Il reste {numberMonkeys} singes")
            n += 1

    if numberMonkeys == 0:
        print(Fore.GREEN + 'Tous les singes ont été éliminé ! \n Tu as gagné !')
    else:
        print(Fore.RED + "Tu as perdu")

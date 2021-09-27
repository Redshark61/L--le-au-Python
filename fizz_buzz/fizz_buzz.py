import json
from random import randint
from setTurn import setTurn

with open('../data/fizzBuzz.json') as file:
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


def fizzBuzz(numberMonkeys,
             maxMonkey,
             minMonkey,
             maxBoss,
             minBoss,
             maxPlayer,
             minPlayer,
             chanceMonkey,
             chanceBoss,
             chancePlayer
             ):

    n = 0
    playerIsWrong = False

    turns = [chanceMonkey]*9 + [chanceBoss, chancePlayer]
    while numberMonkeys > 0 and not playerIsWrong:

        for index, chance in enumerate(turns):

            turnData, turn = setTurn(index, data)

            if n % 3 == 0 and n % 5 == 0:
                if randint(0, 100) < chance:
                    print(turnData["winFizz"] + turnData["winBuzz"])

                else:
                    print(turnData['loose'])

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
                    print(turnData["winFizz"])

                else:
                    print(turnData['loose'])

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
                    print(turnData["winBuzz"])

                else:
                    print(turnData['loose'])

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
                    print(n)

                else:
                    print(turnData['loose'])

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
        print('Tous les singes ont été éliminé ! \n Tu as gagné !')
    else:
        print("Tu as perdu")


fizzBuzz(numberMonkeys, maxMonkey,
         minMonkey,
         maxBoss,
         minBoss,
         maxPlayer,
         minPlayer,
         chanceMonkey,
         chanceBoss,
         chancePlayer)

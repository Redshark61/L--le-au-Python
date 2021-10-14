from functions.checkMod import checkMod
from fizz_buzz import configFizzBuzz as conf


def jsonFetch():
    data = checkMod("fizzBuzz")

    # Mise en place des variables de base
    conf.numberMonkeys = data["monkeys"]["number"] + 1

    maxMonkey = data["monkeys"]["maxChance"]
    minMonkey = data["monkeys"]["minChance"]

    maxBoss = data["boss"]["maxChance"]
    minBoss = data["boss"]["minChance"]

    maxPlayer = data["player"]["maxChance"]
    minPlayer = data["player"]["minChance"]

    return maxMonkey, minMonkey, maxBoss, minBoss, maxPlayer, minPlayer, data

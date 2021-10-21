from functions.checkMod import checkMod
from fizz_buzz import configFizzBuzz as conf


def jsonFetch() -> int | int | int | int | int | int | dict:
    """
    Fetch all the data from fizzBuzz.json and return all the chances for each player, as well as the data dict
    """
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

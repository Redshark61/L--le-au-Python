import os.path
import json


def checkMod(name: int) -> dict:
    """
    Enter the name of the data file, and you will automaticly get the data
    from the mods folder if there is, or the data folder if ther is no mods
    """
    if os.path.isfile(f"mods/{name}.json"):
        with open(f'mods/{name}.json') as file:
            data = json.load(file)
    else:
        with open(f"data/{name}.json") as file:
            data = json.load(file)

    return data

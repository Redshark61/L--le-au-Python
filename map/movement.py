from functions import config


def movement(x: int = 0, y: int = 0):
    config.prevPlayerCoord[1] = config.playerCoord[1]
    config.prevPlayerCoord[0] = config.playerCoord[0]
    config.playerCoord[1] += y
    config.playerCoord[0] += x
    config.vitalSigns["foodMax"] -= 2
    config.vitalSigns["waterMax"] -= 2
    config.vitalSigns["energyMax"] -= 3

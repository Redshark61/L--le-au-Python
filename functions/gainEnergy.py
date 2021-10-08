import time
from functions.Position import position


def gainEnergy(energy):
    energy += 3
    time.sleep(0.5)
    return energy

import time
from functions import config


def gainEnergy(energy: int) -> int:
    """
    Increase the energy
    """
    energy += config.energyWhileSleeping
    time.sleep(0.2)
    return energy

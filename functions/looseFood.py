from functions import config


def looseFood(food):
    """
    Decrease your food
    """
    return food - config.looseFoodSleep

from functions import config


def looseFood(food: int) -> int:
    """
    Decrease your food
    """
    return food - config.looseFoodSleep

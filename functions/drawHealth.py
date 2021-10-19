import math
from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def drawWater(water: int) -> None:
    """
    Draw the water bar
    """
    waterDrop = emojiDecoder("f09f92a7")
    print(position(3, 32, f'Soif :    {waterDrop*int(water/10) if water % 10 == 0 else waterDrop*(int(water/10)+1)}{" "*10}'))
    print(position(35, 32, '   '))
    print(position(35, 32, str(water)))


def drawFood(food: int) -> None:
    """
    Draw the food bar
    """
    halfSteak = emojiDecoder('f09f8d96')
    fullSteak = emojiDecoder('f09f8d97')
    numberOfFullSteak = (fullSteak*int(food/10))
    hungerBar = f'Faim :    {" " if food<=0 else numberOfFullSteak if food % 10 == 0 else numberOfFullSteak+halfSteak}{" "*10}'
    print(position(3, 31, hungerBar))
    print(position(35, 31, '   '))
    print(position(35, 31, str(food)))


def drawEnergy(energy: int) -> None:
    """
    Draw the energy bar
    """
    energyIcon = emojiDecoder('e29aa1')
    numberOfIcon = energyIcon*(math.ceil(energy/10))
    print(position(3, 33, f'Energie : {" " if energy <= 0 else numberOfIcon}{" "*10}'))
    print(position(35, 33, '   '))
    print(position(35, 33, f"{str(energy) if energy>0 else '0'}"))

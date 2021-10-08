from functions.Position import position
from functions.emojiDecoder import emojiDecoder
import math


def drawWater(water: int, message: str = '') -> None:
    waterDrop = emojiDecoder("f09f92a7")
    print(position(3, 32, f'Soif : {waterDrop*int(water/10) if water % 10 == 0 else waterDrop*(int(water/10)+1)}{message}{" "*10}'))

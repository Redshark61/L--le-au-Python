from functions.Position import position
from functions.emojiDecoder import emojiDecoder
import math


def drawFood(food: int, message: str = '') -> None:
    # food /= 10
    halfSteak = emojiDecoder('f09f8d96')
    fullSteak = emojiDecoder('f09f8d97')
    print(position(3, 31, f'Faim : {" " if food<=0 else (fullSteak*int(food/10)) if food % 10 == 0 else (fullSteak*(int(food/10))+halfSteak)}{message}{" "*10}'))

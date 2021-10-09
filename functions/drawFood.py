from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def drawFood(food: int, message: str = '') -> None:
    halfSteak = emojiDecoder('f09f8d96')
    fullSteak = emojiDecoder('f09f8d97')
    numberOfFullSteak = (fullSteak*int(food/10))
    hungerBar = f'Faim : {" " if food<=0 else numberOfFullSteak if food % 10 == 0 else numberOfFullSteak+halfSteak}{message}{" "*10}'
    print(position(3, 31, hungerBar))
    print(position(35, 31, '   '))
    print(position(35, 31, str(food)))

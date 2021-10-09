from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def drawEnergy(energy: int, message: str = '') -> None:
    energyIcon = emojiDecoder('e29aa1')
    numberOfIcon = energyIcon*(int(energy/10))
    print(position(3, 33, f'Energie : {" " if energy <= 0 else numberOfIcon}{message}{" "*10}'))
    print(position(35, 33, '   '))
    print(position(35, 33, str(energy)))

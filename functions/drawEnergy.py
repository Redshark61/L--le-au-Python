from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def drawEnergy(energy: int, message: str = '') -> None:
    energyIcon = emojiDecoder('e29aa1')
    print(position(3, 33, f'Energie : {" " if energy < 0 else energyIcon*(int(energy/10)+1)}{message}{" "*10}'))

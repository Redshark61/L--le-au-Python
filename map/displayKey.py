from functions import config
from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def displayKey():
    if config.key > 0:
        for i in range(config.key):
            print(position(80-i, 35, f"Clé : {config.key} {emojiDecoder('f09f979d')}"))

import os
from random import randint
import string
import time
from cesar.encode import encode
from cesar.decode import decode
from functions.Position import clearBox, position
from functions import config
from functions.Colors import Colors
from functions.checkLength import checkLength

# Alphabet
alphabet = string.ascii_lowercase
alphabet = list(alphabet)

# Player name (requested at the beginning of the game)
name = config.playerName
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""

randomLetter = alphabet[randint(0, 25)]

# Initalization of the colors
color = Colors()
color.init()


def main():
    """
    Main function wich runs the caesar code quest
    """

    # Get the story associated to the file
    fileName = os.path.basename(__file__)[:-3]
    text = checkLength(fileName)

    # Print the story
    for index, line in enumerate(text):
        print(position(105, 4+index+1, line), flush=True)
        time.sleep(2)

    clearBox()

    tried = 5
    decodedInput = ''
    code = alphabet.index(randomLetter)

    print(position(105, 2, 'Règles :'.center(47, '-')))
    print(position(105, 3, '- Ne rentre rien pour avoir le Zen décodé'))
    print(position(105, 4, '- Rentre une lettre pour essayer de trouver le'))
    print(position(105, 5, '  cryptage du Zen'))
    print(position(105, 6, '- Rentre plusieurs lettres pour décoder ton nom'))

    # We print the zen of python
    for index, value in enumerate(zen.split('\n')):
        coded = encode(value, code, alphabet)
        print(position(x=105, y=8+index, text=coded))

    # While the name is not decoded, or the player has no more tries
    while decodedInput != name.lower() and tried >= 0:
        print(config.hiddenCursor)
        print(position(x=105, y=12, text="Entre une lettre : "))
        print(config.visibleCursor)
        letter = str(input(position(x=105, y=13, text='')))
        print(config.hiddenCursor)

        # If he doesn't type anything, we  display the zen without any encoding
        if letter == '':
            for index, value in enumerate(zen.split('\n')):
                print(position(x=105, y=14+index+1, text=value))

        # If there is only one letter, we display the zen coded with the previous letter
        elif len(letter) == 1:
            code = alphabet.index(letter)+1
            for index, value in enumerate(zen.split('\n')):
                coded = encode(value, code, alphabet)
                print(position(x=105, y=14+index+1, text=coded))

        # Else, the plyer try to decode his name
        elif len(letter) > 1:
            tryInput = letter
            code = alphabet.index(randomLetter)
            print(config.hiddenCursor)
            decodedInput = decode(tryInput, code, alphabet)
            if decodedInput != name.lower():
                print(position(x=105, y=20, text=f'Même pas proche ! => {decodedInput}'))
                tried -= 1
                print(position(x=105, y=21, text=color.setBackground('red', f'plus que {tried} essai !')))

    print(position(x=105, y=21, text=' '*40))
    print(position(x=105, y=21, text=color.setBackground('brightGreen', 'Bravo, tu as trouvé !')))

    return True

import string
from cesar.encode import encode
from cesar.decode import decode
from functions.Position import position, clearBoxWithLine

alphabet = string.ascii_lowercase
alphabet = list(alphabet)
name = 'Timothee'
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""


def main(line=-10):
    print("\x1b[?25h")
    line = clearBoxWithLine(line, 10)
    print(position(x=105, y=3+line, text="Entre une lettre : "))
    letter = input(position(x=105, y=4+line, text=''))
    code = alphabet.index(letter)+1

    for index, value in enumerate(zen.split('\n')):
        coded = encode(value, code, alphabet)
        print(position(x=105, y=5+index+1+line, text=coded))

    decodedInput = ''

    while decodedInput != name.lower():
        print(position(x=105, y=8+line, text='Rentre un code pour deviner ton nom :'))
        tryInput = input(position(x=105, y=9+line, text=''))
        decodedInput = decode(tryInput, code, alphabet)
        if decodedInput != name.lower():
            print(position(x=105, y=10+line, text=f'Même pas proche ! {decodedInput}'))
        line = clearBoxWithLine(line, 3)

    print(position(x=105, y=10+line, text='Bravo, tu as trouvé !'))
    print('\x1b[?25l')

    return True

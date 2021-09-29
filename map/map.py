import json
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


with open('data/map.json') as file:
    data = json.load(file)

with open('data/coordinates.json') as file:
    coord = json.load(file)

for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')
row = 0
for i in data:
    col = 0
    print(Back.CYAN + "\u0020\u0020", end="")
    for j in i:
        char = '\u0020\u0020'
        if row == coord['quest1'][1] and col == coord['quest1'][0]:
            char = 'X '
        if j == 1:
            print(Back.LIGHTBLACK_EX + char, end="")
        elif j == 2:
            print(Back.LIGHTBLUE_EX + char, end="")
        elif j == 3:
            print(Back.CYAN + char, end="")
        elif j == 4:
            print(Back.YELLOW + char, end="")
        elif j == 5:
            print(Back.GREEN + char, end="")
        elif j == 6:
            print(Back.LIGHTGREEN_EX + char, end="")
        col += 1
    row += 1
    print(Back.CYAN + char, end="")
    print('')

for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')

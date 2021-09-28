import json
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

with open('data/map.json') as file:
    data = json.load(file)

for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')

for i in data:
    print(Back.CYAN + "\u0020\u0020", end="")
    for j in i:
        if j == 1:
            print(Back.LIGHTBLACK_EX + "\u0020\u0020", end="")
        elif j == 2:
            print(Back.LIGHTBLUE_EX + "\u0020\u0020", end="")
        elif j == 3:
            print(Back.CYAN + "\u0020\u0020", end="")
        elif j == 4:
            print(Back.YELLOW + "\u0020\u0020", end="")
        elif j == 5:
            print(Back.GREEN + "\u0020\u0020", end="")
        elif j == 6:
            print(Back.LIGHTGREEN_EX + "\u0020\u0020", end="")
    print(Back.CYAN + "\u0020\u0020", end="")
    print('')

for i in range(51):
    print(Back.CYAN + "\u0020\u0020", end="")
print('')

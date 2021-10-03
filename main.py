from fizz_buzz.fizz_buzz import fizzBuzz
from number import number
from map.map import map
from functions.Clear import clear


def main() -> None:
    print("Que veux-tu faire ?")
    print("1 - FizzBuzz")
    print("2 - Devine le nombre")
    print("3 - Afficher la carte")
    print("q - Quitter")
    entry = input("")
    clear()

    if entry == "1":
        fizzBuzz()
    elif entry == "2":
        number()
    elif entry == "3":
        map()
    elif entry.upper() == "Q":
        return
    main()


if __name__ == "__main__":
    clear()
    main()

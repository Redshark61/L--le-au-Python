from fizz_buzz.fizz_buzz import fizzBuzz
from number import number
from map.map import map


def main():
    print("Que veux-tu faire ?")
    print("1 - FizzBuzz")
    print("2 - Devine le nombre")
    print("3 - Afficher la carte")
    entry = input("")

    if entry == "1":
        fizzBuzz()
    elif entry == "2":
        number()
    elif entry == "3":
        map()


if __name__ == "__main__":
    main()

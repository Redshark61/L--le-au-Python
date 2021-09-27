from fizz_buzz.fizz_buzz import fizzBuzz
from number import number


def main():
    print("Que veux-tu faire ?")
    print("1 - FizzBuzz")
    print("2 - Devine le nombre")
    entry = input("")

    if entry == "1":
        fizzBuzz()
    elif entry == "2":
        number()


if __name__ == "__main__":
    main()

from map.map import map
from functions.Clear import clear


def main() -> None:
    # Begining of the program
    print('\x1b[?25l')
    map()


if __name__ == "__main__":
    clear()
    main()

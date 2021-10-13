from map.map import map
from functions.Clear import clear
from functions import config


def main() -> None:
    # Begining of the program
    print(config.hiddenCursor)
    map()
    clear()


if __name__ == "__main__":
    clear()
    main()

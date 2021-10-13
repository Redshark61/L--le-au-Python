from map.mapLoop import mapLoop
from functions.Clear import clear
from functions import config


def main() -> None:
    # Begining of the program
    print(config.hiddenCursor)
    mapLoop()
    clear()


if __name__ == "__main__":
    clear()
    main()

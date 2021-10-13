coord, data, playerCoord, questToDo, prevPlayerCoord, questDone, createdItems, currentItems, pickedUpItem = [], [], [], [], [], [], [], [], []
char = ' '
itemSelected, toBePosition, currentPosition = 0, 0, 0

noDuplicateInventory = []
vitalSigns = {
    "energyMax": 100,
    "foodMax": 100,
    "waterMax": 100
}

visibleCursor = '\033[?25h'
hiddenCursor = '\033[?25l'

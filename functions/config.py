# Map data
coord, data, playerCoord, questToDo, prevPlayerCoord, questDone, createdItems, currentItems, pickedUpItem = [], [], [], [], [], [], [], [], []
char = ' '

# Inventory
itemSelected, toBePosition, currentPosition = 0, 0, 0
noDuplicateInventory = []

# Health
vitalSigns = {
    "energyMax": 100,
    "foodMax": 100,
    "waterMax": 100
}

# Cursors
visibleCursor = '\033[?25h'
hiddenCursor = '\033[?25l'

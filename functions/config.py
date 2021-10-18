# Map data
coord, data, playerCoord, questToDo, prevPlayerCoord, questDone, createdItems, currentItems, pickedUpItem = [], [], [], [], [], [], [], [], []
key = 0
char = ' '
isLeaving = False

# Inventory
InventorySize, itemSelected, toBePosition, currentPosition = 0, 0, 0, 0
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

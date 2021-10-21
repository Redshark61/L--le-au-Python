
# Map data
coord, data, playerCoord, questToDo, prevPlayerCoord, questDone, createdItems, currentItems, pickedUpItem = [], [], [], [], [], [], [], [], []
key = 0
char = ' '
isLeaving = False
playerName = ''

# Inventory
inventorySize, itemSelected, toBePosition, currentPosition = 0, 0, 0, 0
noDuplicateInventory = []

# Player Stats :
energyMax = 0
foodMax = 0
waterMax = 0
inventoryMax = 0
energyWhileSleeping = 0
looseFoodSleep = 0
looseFoodPerStep = 0
looseWaterPerStep = 0
looseEnergiePerStep = 0
playerMark = ""
skinName = ""

vitalSigns = {
    "energyMax": 0,
    "foodMax": 0,
    "waterMax": 0
}


# Cursors
visibleCursor = '\033[?25h'
hiddenCursor = '\033[?25l'

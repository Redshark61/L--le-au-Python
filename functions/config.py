from functions.checkMod import checkMod

stats = checkMod('playerStats')
# Map data
coord, data, playerCoord, questToDo, prevPlayerCoord, questDone, createdItems, currentItems, pickedUpItem = [], [], [], [], [], [], [], [], []
key = 0
char = ' '
isLeaving = False
playerName = ''

# Inventory
InventorySize, itemSelected, toBePosition, currentPosition = 0, 0, 0, 0
noDuplicateInventory = []
inventoryMax = stats["inventoryMax"]

# Health
vitalSigns = {
    "energyMax": stats["energyMax"],
    "foodMax": stats["foodMax"],
    "waterMax": stats["waterMax"]
}


# Cursors
visibleCursor = '\033[?25h'
hiddenCursor = '\033[?25l'

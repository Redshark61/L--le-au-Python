from functions.Colors import Colors
from functions.Position import position
from functions.emojiDecoder import emojiDecoder


def printMonkeys(color, questToDo, index, quest):
    print(color.setBackground('darkGreen', position((questToDo[index][quest][0])*2-1, (questToDo[index][quest][1])+2, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((questToDo[index][quest][0])*2+3, (questToDo[index][quest][1])+2, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((questToDo[index][quest][0])*2+1, (questToDo[index][quest][1])+1, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((questToDo[index][quest][0])*2+1, (questToDo[index][quest][1]+3), emojiDecoder('f09f90b5'))))

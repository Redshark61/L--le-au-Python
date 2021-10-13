from functions.Position import position
from functions.emojiDecoder import emojiDecoder
import functions.config as config


def printMonkeys(color, index, quest):
    print(color.setBackground('darkGreen', position((config.questToDo[index][quest][0])*2-1, (config.questToDo[index][quest][1])+2, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((config.questToDo[index][quest][0])*2+3, (config.questToDo[index][quest][1])+2, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((config.questToDo[index][quest][0])*2+1, (config.questToDo[index][quest][1])+1, emojiDecoder('f09f90b5'))))
    print(color.setBackground('darkGreen', position((config.questToDo[index][quest][0])*2+1, (config.questToDo[index][quest][1]+3), emojiDecoder('f09f90b5'))))

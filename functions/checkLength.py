#coding: utf-8
from functions.checkMod import checkMod


def checkLength(fileName: str) -> list[str]:
    """
    Using filename, this function return all the dialog and stories stored in the json file at the filename key.

    It's very important that the dialog key and the filename have the same name
    """

    allStoriess = checkMod('stories')
    stories = ''.join(allStoriess[fileName])

    separatedStories = ['']
    maxLength = 45
    splitStories = stories.split(' ')
    i = 0
    for word in splitStories:
        if len(word + separatedStories[i]) >= maxLength:
            separatedStories.append(word + ' ')
            i += 1
        else:
            separatedStories[i] += word+' '
    return separatedStories

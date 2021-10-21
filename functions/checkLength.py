#coding: utf-8
from functions.checkMod import checkMod


def checkLength(fileName: str) -> list[str]:
    """
    Using filename, this function return all the dialog and stories stored in the json file at the filename key.

    !It's very important that the dialog key and the filename have the same name
    """

    # Get all the stories
    allStories = checkMod('stories')
    # Only get the story of the current quest
    stories = ''.join(allStories[fileName])

    # A list wich will store all the line with the correct length
    separatedStories = ['']
    # Length of the line
    maxLength = 45
    splitStories = stories.split(' ')
    i = 0
    for word in splitStories:
        # If the length of the line is longer than the max length add a new element in the list
        if len(word + separatedStories[i]) >= maxLength:
            separatedStories.append(word + ' ')
            i += 1
        # Else add the word to the line
        else:
            separatedStories[i] += word+' '
    return separatedStories

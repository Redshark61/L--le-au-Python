#coding: utf-8
import json


def checkLength(fileName: str) -> list[str]:
    """
    Using filename, this function return all the dialog and stories stored in the json file at the filename key.

    It's very important that the dialog key and the filename have the same name
    """

    with open('data/cinematic.json', encoding='utf-8') as f:
        allCinematics = json.load(f)

    cinematic = ''.join(allCinematics[fileName])

    separatedCinematic = ['']
    maxLength = 45
    splitCinematic = cinematic.split(' ')
    i = 0
    for word in splitCinematic:
        if len(word + separatedCinematic[i]) >= maxLength:
            separatedCinematic.append(word + ' ')
            i += 1
        else:
            separatedCinematic[i] += word+' '
    return separatedCinematic

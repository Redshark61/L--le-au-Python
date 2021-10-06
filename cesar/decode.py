def decode(codedSentence, code, alphabet):

    newSentence = ''
    for i in codedSentence.lower():
        if i not in alphabet:
            newSentence += i
        else:
            for index, letter2 in enumerate(alphabet):
                if i == letter2:
                    place = index - code
                    if place > 26:
                        place -= 26
                    newSentence += alphabet[place]

    return newSentence

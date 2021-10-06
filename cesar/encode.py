def encode(sentence, move, alphabet):
    newSentence = ''
    for i in sentence.lower():
        if i not in alphabet:
            newSentence += i
        else:
            for index, letter2 in enumerate(alphabet):
                if i == letter2:
                    place = index + move
                    if place >= 26:
                        place -= 26
                    newSentence += alphabet[place]

    return newSentence

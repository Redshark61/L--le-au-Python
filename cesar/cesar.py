import string

alphabet = string.ascii_lowercase
alphabet = list(alphabet)


def encode(sentence, move):
    newSentence = ''
    for i in sentence.lower():
        if i not in alphabet:
            newSentence += i
        else:
            for index, letter2 in enumerate(alphabet):
                if i == letter2:
                    place = index + move
                    newSentence += alphabet[place]

    return newSentence


def decode(codedSentence, code):

    newSentence = ''
    for i in codedSentence.lower():
        if i not in alphabet:
            newSentence += i
        else:
            for index, letter2 in enumerate(alphabet):
                if i == letter2:
                    place = index - code
                    newSentence += alphabet[place]

    return newSentence


print(encode('Les mouches volent', 2))
print(decode("ngu oqwejgu xqngpv", 2))

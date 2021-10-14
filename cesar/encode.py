def encode(sentence: str, move: int, alphabet: list[str]) -> str:
    """
    Encode a ceasar code. The sentence is the sentence you want to code, move is the shift, and alphabet, the alphabet.

    Returns the encoded sentence
    """

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

def decode(codedSentence: str, code: int, alphabet: list[str]) -> str:
    """
    Decode a ceasar code. The codedSentence is the sentence coded, code is the shift, and alphabet, the alphabet.

    Returns the decoded sentence
    """

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

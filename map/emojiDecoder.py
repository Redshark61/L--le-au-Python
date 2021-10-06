def emojiDecoder(emoji):
    byteArray = bytearray.fromhex(emoji)
    mark = byteArray.decode()
    return mark

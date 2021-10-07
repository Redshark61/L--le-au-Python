def emojiDecoder(emoji: str) -> str:
    """
    Transform the hex code of an emoji as a string
    """
    byteArray = bytearray.fromhex(emoji)
    mark = byteArray.decode()
    return mark

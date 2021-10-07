import os


class Colors:

    colorsBg = {
        "brightGray": "\033[100m",
        "brightCyan": "\033[106m",
        "darkBlue": "\033[44m",
        "brightYellow": "\033[103m",
        "brightGreen": "\033[102m",
        "darkGreen": "\033[42m",
    }

    colorsFg = {
        "brightGray": "\033[900m",
        "brightCyan": "\033[96m",
        "darkBlue": "\033[34m",
        "brightYellow": "\033[93m",
        "brightGreen": "\033[92m",
        "darkGray": "\033[32m",
        "red": "\033[91m"
    }

    colorBgEnd = "\033[49m"
    colorFgEnd = "\033[39m"

    def init() -> None:
        os.system('')

    def setBackground(color: str, text: str) -> str:
        return Colors.colorsBg[color] + text + Colors.colorBgEnd

    def setForeground(color: str, text: str) -> str:
        return Colors.colorsFg[color] + text + Colors.colorFgEnd

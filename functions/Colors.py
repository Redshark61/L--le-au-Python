import os


class Colors:

    def __init__(self) -> None:
        self.colorsBg = {
            "brightGray": "\033[100m",
            "brightCyan": "\033[106m",
            "darkBlue": "\033[44m",
            "brightYellow": "\033[103m",
            "darkYellow": "\033[43m",
            "brightGreen": "\033[102m",
            "darkGreen": "\033[42m",
            "red": "\033[101m"
        }
        self.colorsFg = {
            "darkYellow": "\033[33m",
            "brightGray": "\033[900m",
            "brightCyan": "\033[96m",
            "darkBlue": "\033[34m",
            "brightYellow": "\033[93m",
            "brightGreen": "\033[92m",
            "darkGray": "\033[32m",
            "red": "\033[91m"
        }
        self.colorBgEnd = "\033[49m"
        self.colorFgEnd = "\033[39m"

    def init(self) -> None:
        """
        Initalize the console to print colors
        """
        os.system('')

    def setBackground(self, color: str, text: str) -> str:
        """
        Set a background for a given string (emoji, char, sentence...)
        """
        return self.colorsBg[color] + text + self.colorBgEnd

    def setForeground(self, color: str, text: str) -> str:
        """
        Set a foreground for a given string (emoji, char, sentence...)
        """
        return self.colorsFg[color] + text + self.colorFgEnd

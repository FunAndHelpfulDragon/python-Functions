from dataclasses import dataclass
from colorama.ansi import AnsiCodes


@dataclass
class FORMAT(AnsiCodes):
    RESET = 0
    BOLD = 1
    DISABLE = 2
    ITALIC = 3
    UNDERLINE = 4
    REVERSE = 7
    INVISIBLE = 8
    STRIKETHROUGH = 9

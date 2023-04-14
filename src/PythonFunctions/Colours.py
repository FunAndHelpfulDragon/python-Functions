from colorama.ansi import AnsiCodes


class AnsiFormat(AnsiCodes):
    RESET               = 0
    BOLD                = 1
    DISABLE             = 2
    ITALIC              = 3
    UNDERLINE           = 4
    REVERSE             = 7
    INVISIBLE           = 8
    STRIKETHROUGH       = 9


Format = AnsiFormat()

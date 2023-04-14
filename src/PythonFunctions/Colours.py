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


def Translate(string: str, Form: AnsiFormat) -> str:
    """Translates a string into the format specified

    Args:
        string (str): The string to translate
        Form (AnsiFormat): The format to use

    Returns:
        str: The result
    """
    return f'{Form}{string}{Format.RESET}'

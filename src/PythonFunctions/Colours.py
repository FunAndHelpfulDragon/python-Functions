from colorama.ansi import AnsiCodes
from colorama import Style


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
        Form (AnsiFormat): The format to use (Does support any kind of colorama input)

    Returns:
        str: The result
    """
    return f'{Form}{string}{Style.RESET_ALL}'


def Revert(string: str) -> str:
    """Get the original string from a coloured version

    Args:
        string (str): The string to translate

    Returns:
        str: The resulant string
    """
    if string.startswith('\x1b'):
        start = string.find('m', 4) + 1
        end = string.find('\x1b', start)

        return string[start:end]

    print("String does not start with '\x1b'")
    return string

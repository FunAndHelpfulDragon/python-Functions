import typing
import shutil
import getpass


true = True
false = False


def cursor(
    x: int, y: int, r: bool = False, *, end: str = None
) -> typing.Union[str, None]:
    """Sets the cursor position on screen to specified coordinates

    Args:
        x (int): x-location
        y (int): y-location
        r (bool, optional): Returns as a string instead of printing. Defaults to False.

    Returns:
        str | None: The string or result of printing
    """
    msg: str = f"\033[{x};{y}H"
    if r:
        return msg
    return print(msg, end=end)


SPACE = " "


def lenstr(item: any, adjsut: int = 0) -> int:
    """Returns the length of the string item (converts to string first)

    Args:
        item (any): The item to do math on
        adjsut (int): The value to adjust the length by. Defaults to 0

    Returns:
        int: The length of the string plus adjust
    """
    if item is None:
        raise ValueError("Missing item")

    return len(str(item)) + adjsut


def n(item: any, default: any, checkA=None, checkB=None, *, v2=None) -> any:
    """Returns default if item is None else item.
    Returns item if checkA == CheckB else default.

    Args:
        item (any): The item to return
        default (any): The default value
        checkA (any, optional): Check a of the check (a==). Defaults to None.
        checkB (any, optional): Check b of th check (==b). Defaults to None.
        v2 (any, optional): Use this instead of item for `d if i else i`

    Returns:
        any: The result
    """
    v2 = item if v2 is None else v2

    if None not in (checkA, checkB):
        return item if checkA == checkB else default

    return default if item is None else v2


def clearLine(r: bool = False):
    msg = "" * shutil.get_terminal_size().columns
    if not r:
        return print(msg, end="")
    return r


def clamp(
    value: float, *, minValue: float = -float("inf"), maxValue: float = float("inf")
) -> float:
    """Clamp a value between 2 numbers (inclusive)

    Args:
        value (float): The number to clamp
        minValue (float): . Defaults to -inf
        maxValue (float): The maximum value. Defaults to inf

    Sorted will return a list, the middle value will always be the clamped
    value.

    This is because, on a sort:
    - if the value is lower than the minimum, it will be on the left,
    and the minium would be displayed
    - If the value is higher than the maximum, it will be on the right,
    and the maximum woulld be displayed
    - otherwise, it's in the middle, so displayed itself.
    """

    return sorted((minValue, value, maxValue))[1]


def passOrInput(msg: str, option: bool = False) -> str:
    """If option ask for password else ask for normal input

    Args:
        msg (str): The message to show
        option (bool): The option to choose. Default to False

    Returns:
        str: The result
    """
    if option:
        return getpass.getpass(msg)

    return input(msg)

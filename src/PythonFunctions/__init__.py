"""PythonFunctions a module for other modules
Run `python -m PythonFunctions --help` for more information
Visit `python-functions.readthedocs.io/` for the documentation
Visit `https://pypi.org/project/PythonFunctions/` for the pypi version
Visit `https://github.com/FunAndHelpfulDragon/python-Functions/` for the source code.
"""
import typing

true = True
false = False


def cursor(x: int, y: int, r: bool = False) -> typing.Union[str, None]:
    """Sets the cursor position on screen to specified coordinates

    Args:
        x (int): x-location
        y (int): y-location
        r (bool, optional): Returns as a string instead of printing. Defaults to False.

    Returns:
        str | None: The string or result of printing
    """
    msg: str = f'\033[{x};{y}H'
    if r:
        return msg
    return print(msg)

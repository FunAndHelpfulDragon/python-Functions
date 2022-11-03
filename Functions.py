## Convert.py
from Program import Convert
class LC(Convert.LocationConvert):
    def __init__(self, value):
        super().__init__(value)

## CleanFolderData.py
from Program import CleanFolderData
class Clean(CleanFolderData.Clean):
    def __init__(self) -> None:
        super().__init__()

## Message.py
from Program import Message

## IsDigit.py
from Program import IsDigit as ID
def IsDigit(var: str):
    """Checks if var is a `real` number

    Args:
        var (str): The string to check

    Raises:
        AttributeError: If recieved None as the input

    Returns:
        bool: Is it a sutiable real number
    """
    return ID.IsDigit(var)

## Check.py
from Program import Check
class check(Check.check):
    def __init__(self) -> None:
        super().__init__()

## board.py
from Program import Board
class board(Board.board):
    def __init__(self) -> None:
        super().__init__()

## PrintTraceback.py
from Program import PrintTraceback as PT
def LogTraceback():
    PT.PrintTraceback()

## watermark.py
from Program import watermark

## Encryption.py
from Program import Encryption
class Encrypt(Encryption.Encryption):
    def __init__(self) -> None:
        super().__init__()

## colours.py
from Program import colours
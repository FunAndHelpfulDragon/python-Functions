from . import Checks as Checks
from .CleanFolderData import Clean as Clean
from .Colours import c as c
from .Message import Message as Message
from _typeshed import Incomplete
from enum import Enum

class ModeEnum(Enum):
    int: str
    yesno: str
    str: str

class Check:
    ModeEnum: Incomplete
    def __init__(self) -> None: ...
    def getInput(self, msg: str, mode: ModeEnum, *, colour: str = ..., **info): ...

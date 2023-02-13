import typing
from .Colours import CONSOLEFORMATS as CONSOLEFORMATS, Fore as Fore, Style as Style
from _typeshed import Incomplete

class search:
    directory: str
    target: Incomplete
    layers: int
    hidden: Incomplete
    searched: Incomplete
    logging: bool
    def __init__(self) -> None: ...
    def Locate(self, target: typing.List[str], *, directory: str = ..., layers: int = ..., hidden: typing.List[str] = ..., logging: bool = ...): ...
    def Clear(self) -> None: ...

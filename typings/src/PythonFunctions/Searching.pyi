import typing
from .Colours import Print as Print
from _typeshed import Incomplete

class search:
    clean: Incomplete
    directory: str
    target: Incomplete
    layers: int
    hidden: Incomplete
    searched: Incomplete
    logging: bool
    def __init__(self) -> None: ...
    def Locate(self, target: typing.List[str], *, directory: str = ..., layers: int = ..., hidden: typing.List[str] = ..., logging: bool = ...): ...
    def Clear(self) -> None: ...

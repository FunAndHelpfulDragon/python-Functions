import typing
from .Colours import Print as Print

class Message:
    @staticmethod
    def clear(message: str = ..., *, timeS: int = ..., colour: typing.List = ..., delete: bool = ...): ...
    @staticmethod
    def warn(message: str = ..., *, timeS: int = ..., colour: typing.List = ...): ...

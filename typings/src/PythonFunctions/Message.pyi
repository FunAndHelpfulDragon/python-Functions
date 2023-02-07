from .Colours import CONSOLECOLOURS as CONSOLECOLOURS, Fore as Fore, Style as Style

class Message:
    @staticmethod
    def clear(message: str = ..., *, timeS: int = ..., delete: bool = ...): ...
    @staticmethod
    def warn(message: str = ..., *, timeS: int = ...): ...

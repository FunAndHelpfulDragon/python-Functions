from . import template as template
from _typeshed import Incomplete

class save(template.SaveTemplate):
    moduleClass: Incomplete
    def __init__(self) -> None: ...
    def getFileSystem(self) -> None: ...
    def WriteData(self, data: any, path: str, Encoding: bool = ...) -> bool: ...
    def ReadData(self, path: str, Encoding: bool = ...) -> any: ...
    def DeleteFile(self, path: str): ...
    def DeleteFolder(self, path: str): ...
    def MakeFolders(self, path: str): ...

def load(): ...

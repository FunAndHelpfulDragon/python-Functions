import typing
from . import SaveModules as SaveModules
from .Check import Check as Check
from .CleanFolderData import Clean as Clean
from .Encryption import Encryption as Encryption
from .Message import Message as Message
from .PrintTraceback import PrintTraceback as PrintTraceback
from _typeshed import Incomplete
from enum import Enum

class Encoding(Enum):
    NONE: int
    JSON: int
    BINARY: int
    CRYPTOGRAPHY: int
    CSV: int

class Storage(Enum):
    NORMAL: int
    FTP: int
    GOOGLE: int
    OTHER: int

class DriveCredentialsMode(Enum):
    ADD: int
    DELETE: int

class save:
    encoding: Incomplete
    storage: Incomplete
    DriveCredentialsEnum: Incomplete
    saveModules: Incomplete
    settings: Incomplete
    enc: Incomplete
    def __init__(self) -> None: ...
    def ChangePasscode(self): ...
    def DriveExists(self) -> bool: ...
    def DriveCredentials(self, path: str, mode: DriveCredentialsMode): ...
    def Save(self, data: any, path: str, encoding: typing.List = ...) -> bool: ...
    def Read(self, path: str, encoding: typing.List = ...) -> any: ...
    def MakeFolders(self, path: str, **data): ...
    def RemoveFile(self, path: str): ...
    def RemoveFolder(self, path: str): ...

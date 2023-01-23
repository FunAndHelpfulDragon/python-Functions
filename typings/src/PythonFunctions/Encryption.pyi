from .Message import Message as Message
from .PrintTraceback import PrintTraceback as PrintTraceback
from _typeshed import Incomplete

disabled: bool

class Encryption:
    fernet: Incomplete
    check: Incomplete
    key: Incomplete
    def __init__(self) -> None: ...
    def GetKey(self) -> bytes: ...
    def EncryptData(self, data, passcode): ...
    def DecryptData(self, data, passcode): ...
    def encrypt(self, data, passcode: bytes, *, fileName: str = ...): ...
    def decrypt(self, passcode: bytes, *, fileName: str = ...): ...

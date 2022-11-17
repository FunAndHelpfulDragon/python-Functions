from . import PrintTraceback
from .Message import Message

disabled = False

try:
    import base64
    import hashlib

    from cryptography import fernet
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    Message.warn(
        "Failed to load encrypting class (Missing imports!)", timeS=2, colour="red"
    )
    PrintTraceback()
    disabled = True


class Encryption:
    """The major class to encrypt and decrypt data securly"""

    def __init__(self) -> None:
        self.fernet = fernet
        self.check: bool = not disabled

    def GetKey(self, passcode: bytes = None) -> bytes:
        """Translates your encrypted (using utf-8) passcode into something more secure

        Args:
            passcode (bytes): Your passcode encrypted with utf-8

        Returns:
            bytes: The result
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        if passcode is None:
            return Fernet.generate_key()

        assert isinstance(passcode, bytes)
        hlib = hashlib.md5()
        hlib.update(passcode)
        Message().warn(
            "WARNING, here is your key please keep this safe.", timeS=2, colour="red"
        )
        return base64.urlsafe_b64encode(hlib.hexdigest().encode("latin-1"))

    def EncryptData(self, data, passcode):
        key = passcode
        if not isinstance(passcode, bytes):
            key = self.GetKey(passcode.encode("utf-8"))

        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        return Fernet(key).encrypt(data)

    def DecryptData(self, data, passcode):
        return Fernet(passcode).decrypt(data)

    def encrypt(self, data, passcode: bytes, *, fileName="encrypted"):
        """Encrypts the data that you want to in a safe file

        Args:
            data (_type_): The data to save
            passcode (bytes): The passcode to encrypt with
            fileName (str, optional): The name of the file. Defaults to "encrypted".
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        # COnvert to bytes
        key = passcode
        if not isinstance(passcode, bytes):
            key = self.GetKey(passcode.encode("utf-8"))

        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        with open(fileName, "wb") as f:
            f.write(self.EncryptData(data, key))
            return "Saved data"

    def decrypt(self, passcode: bytes, *, fileName="encrypted"):
        """Decrypt the data stored in the file

        Args:
            passcode (bytes): Your passcode to decypt with
            fileName (str, optional): The name of the file. Defaults to "encrypted".
            data (any, optional): ONLY REQUIRED IF YOU ALREADY HAVE ENCRYPTED DATA

        Returns:
            _type_: The decrypted data
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        with open(fileName, "rb") as f:
            data = self.DecryptData(f.read(), passcode)
            return data.decode("utf-8")

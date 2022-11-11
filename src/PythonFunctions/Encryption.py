from . import Message
from . import PrintTraceback

disabled = False

try:
    import cryptography.fernet as fernet
    from cryptography.fernet import Fernet
    import base64
    import hashlib
except ModuleNotFoundError:
    Message.Message.warn("Failed to load encrypting class (Missing imports!)", timeS=2, colour="red")
    try:
        PrintTraceback.PrintTraceback()
    except Exception:
        # Just don't print if failed for some reason
        pass
    disabled = True

class Encryption:
    def __init__(self) -> None:
        """The major class to encrypt and decrypt data securly
        """
        self.fernet = fernet
        pass
    
    def GetKey(self, passcode:bytes=None) -> bytes:
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
        Message.Message.warn("WARNING, here is your key please keep this safe.", timeS=2, colour="red")
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
    
    def encrypt(self, data, passcode:bytes, *, fileName="encrypted"):
        """Encrypts the data that you want to in a safe file

        Args:
            data (_type_): The data to save
            passcode (bytes): The passcode to encrypt with
            fileName (str, optional): The name of the file. Defaults to "encrypted".
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"
        
        with open(fileName, "wb") as f:
            f.write(Fernet(passcode).encrypt(data.encode('utf-8')))
    
    def decrypt(self, passcode:bytes, *, fileName="encrypted"):
        """Decrypt the data stored in the file

        Args:
            passcode (bytes): Your passcode to decypt with (Must be same else you get different data)
            fileName (str, optional): The name of the file. Defaults to "encrypted".

        Returns:
            _type_: The decrypted data
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"
        
        with open(fileName, "rb") as f:
            data = Fernet(passcode).decrypt(f.read())
            return data.decode('utf-8')
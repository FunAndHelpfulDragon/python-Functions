import importlib
Encryption = importlib.import_module("PythonFunctions.Encryption", "..")
import os

enc = Encryption.Encryption()
gblKey = None

def test_Key():
    global gblKey
    key = enc.GetKey()
    gblKey = key
    assert type(key) == bytes

def test_Encrypt():
    if gblKey is None:
        test_Key()
    
    data = "Hello"
    enc.encrypt(data, gblKey, fileName="EncryptionTest.byte")
    assert os.path.exists("EncryptionTest.byte")

def test_Decrypt_wrong():
    key = enc.GetKey("encrypt".encode('utf-8'))
    try:
        result = enc.decrypt(key, fileName="EncryptionTest.byte")
    except Encryption.fernet.InvalidToken:
        assert True

def test_Decrypt_Correct():
    global gblKey
    try:
        result = enc.decrypt(gblKey, fileName="EncryptionTest.byte")
        assert result == "Hello"
    except Encryption.fernet.InvalidToken:
        assert False

def test_CleanUp():
    global gblKey
    gblKey = None
    os.remove("EncryptionTest.byte")
    assert True
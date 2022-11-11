from . import PythonFunctions

Encryption = PythonFunctions.Encryption
import os


enc = Encryption()
gblKey = None

# NOTE: IF these tests (test_Key, test_Encrypt, test_Decrypt) fail, it is on purpose as something broke on the server side (not installed modules)


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
    key = enc.GetKey("encrypt".encode("utf-8"))
    try:
        result = enc.decrypt(key, fileName="EncryptionTest.byte")
    except enc.fernet.InvalidToken:
        assert True


def test_Decrypt_Correct():
    global gblKey
    try:
        result = enc.decrypt(gblKey, fileName="EncryptionTest.byte")
        assert result == "Hello"
    except enc.fernet.InvalidToken:
        assert False


def test_finish():
    global gblKey
    gblKey = None
    try:
        os.remove("EncryptionTest.byte")
    except FileNotFoundError:
        pass

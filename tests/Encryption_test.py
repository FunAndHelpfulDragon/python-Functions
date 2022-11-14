"""Tests functions in the Encryption module

NOTE: IF these tests (test_Key, test_Encrypt, test_Decrypt) fail,
it is on purpose as something broke on the server side (not installed modules)
"""

import os

from . import PythonFunctions

Encryption = PythonFunctions.Encryption

enc = Encryption()


def test_Key():
    """Test to see if a random gen key can be generated"""
    key = enc.GetKey()
    assert isinstance(key, bytes)

    with open("Key.keybyte", "wb") as f:
        f.write(key)


def test_Encrypt():
    """Test to see if encryption is good"""
    with open("Key.keybyte", "rb") as f:
        key = f.read()

    data = "Hello"
    enc.encrypt(data, key, fileName="EncryptionTest.byte")
    assert os.path.exists("EncryptionTest.byte")


def test_Decrypt_wrong():
    """Test to see if we get an invalid token with a random key"""
    key = enc.GetKey("encrypt".encode("utf-8"))
    try:
        enc.decrypt(key, fileName="EncryptionTest.byte")
    except enc.fernet.InvalidToken:
        assert True


def test_Decrypt_Correct():
    """Test to see if we get the right data on decrypting the file"""
    try:
        with open("Key.keybyte", "rb") as f:
            key = f.read()

        result = enc.decrypt(key, fileName="EncryptionTest.byte")
        assert result == "Hello"
    except enc.fernet.InvalidToken:
        assert False


def test_finish():
    """Play cleanup"""
    try:
        os.remove("EncryptionTest.byte")
        os.remove("key.keybyte")
    except FileNotFoundError:
        pass

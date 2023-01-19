"""Tests functions in the Clean module
"""

import os

from . import PythonFunctions

Clean = PythonFunctions.CleanFolderData

cln = Clean.Clean()


def test_Clean():
    """Clean the current folder, and make sure that any file ending in .py is not included."""
    with open("tests/Secret", "w", encoding="utf-8") as f:
        f.write("This is a secret file")

    result = cln.clean("tests", ["Secret"])
    assert "__pycache__" not in result
    assert "Secret" not in result

    os.remove("tests/Secret")


def test_Remove():
    """Tests if the clean module can remove the correct data"""
    data = cln.GetData("tests")
    result = cln.RemoveHidden(data)
    for item in result:
        assert not item.startswith(".") and not item.startswith("__")


def test_Reserved():
    """Tests if the clean module can remove hidden / reserved data"""
    data = cln.GetData("tests")
    data = cln.RemoveHidden(data)

    reserved = ["HW", "Password.txt"]
    with open("tests/Password.txt", "w", encoding="utf-8") as f:
        f.write("password")

    result = cln.RemoveReserved(data, reserved)
    for item in reserved:
        assert item not in result

    os.remove("tests/Password.txt")


def test_Wild_Reserved():
    """Tests if the clean module can remove files with * features"""
    data = cln.GetData("tests")
    data = cln.RemoveHidden(data)

    reserved = ["*.txt"]
    for i in range(10):
        with open(f"tests/test{i}.txt", "w", encoding="utf-8") as f:
            f.write("hi")

    result = cln.RemoveReserved(data, reserved)
    for item in result:
        assert not item.endswith(".txt")

    for i in range(10):
        os.remove(f"tests/test{i}.txt")

import os
from . import PythonFunctions
Clean = PythonFunctions.Clean

cln = Clean()

def test_Clean():
    # Clean the current folder, and make sure that any file ending in .py is not included.
    with open("tests/Secret", "w") as f:
        f.write("This is a secret file")
    
    result = cln.clean("tests", ["Secret"])
    assert "__pycache__" not in result
    assert "Secret" not in result
    
    os.remove("tests/Secret")

def test_Get():
    result = cln.GetData("tests")
    assert result == os.listdir("tests")

def test_Remove():
    data = cln.GetData("tests")
    result = cln.RemoveHidden(data)
    for item in result:
        assert not item.startswith(".") and not item.startswith("__")

def test_Reserved():
    data = cln.GetData("tests")
    data = cln.RemoveHidden(data)
    
    reserved = ["HW", "Password.txt"]
    with open("tests/Password.txt", "w") as f:
        f.write("password")
    
    result = cln.RemoveReserved(data, reserved)
    for item in reserved:
        assert item not in result
    
    os.remove("tests/Password.txt")
    
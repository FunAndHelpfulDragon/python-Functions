from . import PythonFunctions
Check = PythonFunctions.check
import sys
from io import StringIO
import random

def int_check(chk: Check):
    ranIn = random.randrange(-10, 10)
    sys.stdin = StringIO(f"{ranIn}")
    result = chk.getInput("Testing (int): ", "int", lower=-10, higher=10)
    return result

def yn_check(chk: Check, vIn: str):
    sys.stdin = StringIO(f"{vIn}")
    return chk.getInput("Testing (yn): ", "yn")

chk = Check()
def test_int():
    rt = int_check(chk)
    if rt == 0:
        assert True
        return
    assert rt

def test_yes():
    assert yn_check(chk, "y") == True

def test_no():
    assert yn_check(chk, "n") == False

def test_error():
    try:
        assert yn_check(chk, "E") == None
    except EOFError:
        # End of file error means that nothing got returned. As so, it breaka
        assert True
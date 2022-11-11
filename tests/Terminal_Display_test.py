from io import StringIO
import sys
from . import PythonFunctions
TD = PythonFunctions.Display
import pytest
import random


dsp = TD()

def callback(value):
    assert value is not None
    return value

def test_set():
    dsp.SetOptions({
        0: (callback, "home"),
        1: (callback, "Test1"),
        2: (callback, "Test2")
    })
    
    assert len(dsp.options) == 3

def test_add():
    dsp.AddOption(-1, (callback, "Test3"))
    dsp.AddOption(-2, (callback, "Test4"))
    
    assert len(dsp.options) == 5

@pytest.mark.repeat(4)
def test_List():
    # Checks to see if they exists, else add them.
    if len(dsp.options) < 5:
        test_set()
        test_add()

    v = random.randrange(-2, 2)
    sys.stdin = StringIO(f"{v}")
    rst = dsp.ShowOptions(list=True)
    assert rst is not None

@pytest.mark.repeat(5)
def test_Remove():
    # Checks to see if removing works
    cLen = len(dsp.options)
    try:
        dsp.RemoveOption(random.randrange(-2, 2))
        assert len(dsp.options) == cLen -1
    except KeyError:
        # If key error, probably issue in random
        pass

# @pytest.mark.repeat(2)
# def test_Grid():
#     moveOptions = ""
#     end = False
#     opt = ["w", "a", "s", "d", "\r"]
#     while not end:
#         item = random.sample(opt, 1)[0]
#         moveOptions += item
#         end = item == "\r"
        
    
#     sys.stdin = StringIO(moveOptions)
#     rst = dsp.ShowOptions()
#     assert rst is not None
"""Tests functions in the Check module
"""

import random
import sys
from io import StringIO

from . import PythonFunctions

Check = PythonFunctions.Check
chk = Check.Check()


def int_check():
    """Checks if a random int is within range

    Returns:
        The result: of the check
    """
    ranIn = random.randrange(-10, 10)
    sys.stdin = StringIO(f"{ranIn}")
    result = chk.getInput(
        "Testing (int): ", chk.ModeEnum.int, lower=-10, higher=10)
    return result


def yn_check(vIn: str):
    """Checks if input is y or n

    Args:
        vIn (str): The input

    Returns:
        The result: of the check
    """
    sys.stdin = StringIO(f"{vIn}")
    return chk.getInput("Testing (yn): ", chk.ModeEnum.yesno)


def yn_check_return(vIn: str):
    """Check if input is y or n and call that function

    Args:
        vIn (str): The input
    """
    sys.stdin = StringIO(f"{vIn}")
    return chk.getInput("Testing (yn): ", chk.ModeEnum.yesno,
                        y=yn_check_y_return, n=yn_check_n_return)


def yn_check_y_return():
    """The yes return function for input check
    """
    return "yes"


def yn_check_n_return():
    """The no return function for input check
    """
    return "no"


def str_check(vIn: str, arr: list):
    """Checks if input is in list

    Args:
        vIn (str): The inputs
        arr (list): The check list

    Returns:
        The result: of the check
    """
    sys.stdin = StringIO(f"{vIn}")
    return chk.getInput("Testing (str): ", chk.ModeEnum.str, info=arr)


def test_int():
    """Result of the int check test"""
    rt = int_check()
    if rt == 0:
        assert True
        return
    assert rt


def test_yes():
    """Result of the yes yn check test"""
    assert yn_check("y") is True


def test_no():
    """Result of the no yn check test"""
    assert yn_check("n") is False


def test_error():
    """Result of the E yn check test"""
    try:
        assert yn_check("E") is None
    except EOFError:
        # End of file error means that nothing got returned. As so, it breaka
        assert True


def test_yes_return():
    assert yn_check_return("y") is "yes"


def test_no_return():
    assert yn_check_return("n") is "no"


def test_str():
    """Test to see if random string in list"""
    strList = ["a", "e", "i", "o", "u"]
    assert str_check("a", strList)
    assert str_check("e", strList)
    assert str_check("i", strList)
    assert str_check("o", strList)
    assert str_check("u", strList)
    assert not str_check("b", strList)
    assert not str_check("c", strList)
    assert not str_check("d", strList)
    assert not str_check("f", strList)
    assert not str_check("g", strList)

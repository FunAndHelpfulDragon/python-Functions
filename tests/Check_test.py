"""Tests functions in the Check module
"""

import random
import string
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


def test_str():
    """Test to see if random string in list
    """
    strList = []
    for _ in range(random.randrange(10)):
        strList.append(random.choice(string.ascii_letters))

    assert str_check(strList[random.randrange(len(strList) - 1)], strList)
    assert not str_check(random.choice(string.digits), strList)

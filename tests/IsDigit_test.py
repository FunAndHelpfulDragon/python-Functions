"""Tests functions in the IsDigit module
"""

import random
import string
import pytest
from . import PythonFunctions
IsDigit = PythonFunctions.IsDigit


@pytest.mark.repeat(10)
def test_isdigit():
    """Random number test (float)"""
    assert IsDigit(random.uniform(-100, 100))


@pytest.mark.repeat(10)
def test_isdigit_str():
    """random str number float test"""
    assert IsDigit(f"{random.uniform(-100, 100)}")


@pytest.mark.repeat(10)
def test_notDigit():
    """random none float test"""
    assert not IsDigit(random.sample(string.ascii_letters, k=random.randrange(1, 5)))

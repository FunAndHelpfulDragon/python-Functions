"""Tests functions in the Convert module
"""

import random
import string

import pytest
from src.PythonFunctions import Convert

letters = string.ascii_uppercase


@pytest.mark.repeat(3)
def test_Convert():
    """Test to convert a random location to a tuple"""
    position = "".join(random.sample(
        string.ascii_uppercase, random.randrange(1, 3)))

    num = random.randrange(100)
    result = Convert.Location(f"{position}{num}")

    x = 0
    for _, i in enumerate(position):
        numo = letters.find(i) + 1
        x *= 26
        x += numo

    assert result[0] == x - 1
    assert result[1] == num - 1

"""Tests functions in the Convert module
"""

import random
import string

import pytest

from . import PythonFunctions

Convert = PythonFunctions.Convert


# BAD WAY BUT FOR TESTING PURPOSE
letters = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


@pytest.mark.repeat(3)
def test_Convert():
    """Test to convert a random location to a tuple"""
    position = "".join(random.sample(
        string.ascii_uppercase, random.randrange(1, 3)))

    num = random.randrange(100)
    result = Convert.Location(f"{position}{num}")

    x = 0
    for _, i in enumerate(position):
        numo = letters.get(i)
        x *= 26
        x += numo

    assert result[0] == x - 1
    assert result[1] == num - 1

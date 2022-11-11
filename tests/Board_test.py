import random

from . import PythonFunctions

Board = PythonFunctions.Board


def rp_test_Size(x: int, y: int):
    """Test that the size input is the correct for size output"""
    brd = Board.CreateBoard(x, y)

    count = 0
    for x in brd:
        for y in x:
            count += 1

    return count


def test_size():
    """Test 10 times, for the correct board size"""
    x = random.randrange(10)
    y = random.randrange(10)
    result = rp_test_Size(x, y)
    print(f"Result: {result}. Input: {x}, {y}")
    assert result == x * y

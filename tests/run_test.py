"""Test to do with run and time"""

import time
import pytest

from . import PythonFunctions

run = PythonFunctions.Run
IsDigit = PythonFunctions.IsDigit.IsDigit


@pytest.mark.repeat(5)
def test_mark():
    """Marking..."""
    index = run.Mark()
    assert index > 0
    assert len(run.markers) == index


def test_get_mark():
    """Reading..."""
    if len(run.markers) == 0:
        run.Mark()

    try:
        run.GetMarkTime(len(run.markers))
    except IndexError:
        assert True

    assert IsDigit(run.GetMarkTime(0))


def test_compare():
    "Comparing..."
    if len(run.markers) == 0:
        run.Mark()
        time.sleep(0.05)
        run.Mark()

    i1 = run.GetMarkTime(0)
    i2 = run.GetMarkTime(1)

    assert i2 - i1 == run.CompareIndex(0, 1)


def test_wrapper():
    @run.Timer
    def delay():
        time.sleep(1)

    @run.Timer
    def delay2(a, b):
        time.sleep(1)
        return a, b

    assert delay() is None
    assert delay2(1, 2) == (1, 2)

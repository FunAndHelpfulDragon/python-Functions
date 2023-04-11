"""Test to do with run and time"""

import time
import pytest

from src.PythonFunctions import Run
from src.PythonFunctions.IsDigit import IsDigit


@pytest.mark.repeat(5)
def test_mark():
    """Marking..."""
    index = Run.Mark()
    assert index > 0
    assert len(Run.markers) == index


def test_get_mark():
    """Reading..."""
    if len(Run.markers) == 0:
        Run.Mark()

    try:
        Run.GetMarkTime(len(Run.markers))
    except IndexError:
        assert True

    assert IsDigit(Run.GetMarkTime(0))


def test_compare():
    "Comparing..."
    if len(Run.markers) == 0:
        Run.Mark()
        time.sleep(0.05)
        Run.Mark()

    i1 = Run.GetMarkTime(0)
    i2 = Run.GetMarkTime(1)

    assert i2 - i1 == Run.CompareMarkers(0, 1)


def test_wrapper():
    @Run.Timer
    def delay():
        time.sleep(1)

    @Run.Timer
    def delay2(a, b):
        time.sleep(1)
        return a, b

    assert delay() is None
    assert delay2(1, 2) == (1, 2)

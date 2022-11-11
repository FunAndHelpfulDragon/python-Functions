from . import PythonFunctions

run = PythonFunctions.run
IsDigit = PythonFunctions.IsDigit
import time

import pytest


@pytest.mark.repeat(5)
def test_mark():
    index = run.Mark()
    assert index > 0
    assert len(run.markers) == index


def test_get_mark():
    if len(run.markers) == 0:
        run.Mark()

    try:
        run.GetMarkTime(len(run.markers))
    except IndexError:
        assert True

    assert IsDigit(run.GetMarkTime(0))


def test_compare():
    if len(run.markers) == 0:
        run.Mark()
        time.sleep(0.05)
        run.Mark()

    i1 = run.GetMarkTime(0)
    i2 = run.GetMarkTime(1)

    assert i2 - i1 == run.CompareIndex(0, 1)

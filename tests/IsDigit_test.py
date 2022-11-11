from . import PythonFunctions
IsDigit = PythonFunctions.IsDigit
import random
import pytest

@pytest.mark.repeat(10)
def test_isdigit():
    assert IsDigit(random.uniform(-100, 100))

@pytest.mark.repeat(10)
def test_isdigit_str():
    assert IsDigit(f"{random.uniform(-100, 100)}")

@pytest.mark.repeat(10)
def test_notDigit():
    assert not IsDigit(random.sample("Hello", k=random.randrange(1, 5)))
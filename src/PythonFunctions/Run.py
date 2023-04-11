"""
Run.py

Mainipulate time, in a module.
Basic functions, but just stored elsewhere
"""

import time

start = time.time()
markers = {}


def Mark(name: str = "") -> int:
    """Add a new marker

    Args:
        name (str): The name to give the marker. Defaults to index position

    Returns:
        int: The marker number
    """
    if name == "":
        name = str(len(markers))
        print(f'Set marker to {name}')
    markers[name] = time.time()
    return len(markers)


def GetMarkTime(name: str) -> float:
    """Get the time at a certain mark. Note: only use pos or name don't use both

    Args:
        pos (int, optional): The index of the mark. Defaults to 0.
        name (str, optional): The name of the mark. Defaults to "".

    Returns:
        float: The mark time.
    """
    return markers.get(str(name))


def CompareMarkers(a: str, b: str, roundValue: int = -1) -> float:
    """Compare the time differences between 2 points

    Args:
        a (str): The first marker
        b (str): The second marker
        roundValue (int, optional): How many to decimal places to round to. 
        Defaults to -1 (No rounding).

    Returns:
        float: The result. (-1.0 if invalid marker)
    """
    a = str(a)
    b = str(b)
    try:
        diff = markers.get(b) - markers.get(a)
        if roundValue == -1:
            return diff

        return round(diff, roundValue)
    except TypeError:
        print(f"Invalid marker passed! a: {a}. b: {b}")
        return -1.0


def End() -> float:
    """Returns the time since the program started

    Returns:
        float: The time difference
    """
    return time.time() - start


def Timer(func):
    """Time how long it takes to run a function
    """
    def wrapper(*args):
        t1 = time.time()
        x = func(*args)
        t2 = time.time()
        print(f'{func.__name__} took {t2-t1} seconds')
        return x
    return wrapper

import time
start = time.time()
markers = []

"""
HOW TO USE:
`import run`

If you want to compare the time difference between 2 functions. Use:
a = run.Mark()
**CODE**
b = run.Mark()
print(run.CompareIndex(a, b))
"""

def Mark() -> int:
    """Add a new marker

    Returns:
        int: The marker number
    """
    markers.append(time.time())
    return len(markers)

def GetMarkTime(i: int) -> float:
    """Return the time at the mark

    Args:
        i (int): The mark index

    Returns:
        float: The time
    """
    return markers[i]

def Compare(a: float, b:float) -> float:
    """Compares a with b

    Args:
        a (float): The first time (start)
        b (float): The second time (end)

    Returns:
        float: The time difference
    """
    return b - a

def CompareIndex(a: int, b:int) -> float:
    """Compare the time differences between 2 points in the marker index

    Args:
        a (int): The first marker index
        b (int): The second marker index

    Returns:
        float: The time difference
    """
    return markers[b] - markers[a]

def End() -> float:
    """Returns the time since the program started

    Returns:
        float: The time difference
    """
    return time.time() - start
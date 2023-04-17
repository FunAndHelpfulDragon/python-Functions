"""Checks if a value is within a certain range
"""
import importlib
IsDigit = importlib.import_module('.IsDigit', 'PythonFunctions')
Message = importlib.import_module('.Message', 'PythonFunctions')
IsDigit = IsDigit.IsDigit


def Clear(msg: str, clear: bool):
    if clear:
        return Message.clear(msg, timeS=1)
    return Message.warn(msg, timeS=1)


def check(value, **info) -> int:
    """Checks if a value is within a certain range

    Args:
        value (_type_): The value to check
        Message (_type_): Message obj
        ID (_type_): IsDigit obj

    Returns:
        _type_: Either the value, or nothing
    """
    higherRange = info.get("higher")
    lowerRange = info.get("lower")
    clear = info.get("clear")

    if value == '':
        return False

    # is digit check
    if IsDigit(value):
        value = float(value)
        if lowerRange is not None:
            if value < lowerRange:
                return Clear(f"Out of range. Too low! (Lowest Value: {lowerRange})", clear)

        if higherRange is not None:
            if value > higherRange:
                return Clear(f"Out of range. Too high! (Highest Value: {higherRange})", clear)
        return int(value)

    return Clear("Invalid input! Not a `real` number", clear)

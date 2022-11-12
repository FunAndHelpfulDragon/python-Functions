"""Checks if a value is within a certain range
"""

def check(value, Message, ID, **info):
    """Checks if a value is within a certain range

    Args:
        value (_type_): The value to check
        Message (_type_): Message obj
        ID (_type_): IsDigit obj

    Returns:
        _type_: Either the value, or nothing
    """
    higherRange = 0
    
    lowerRange = info.get("lower")
    higherRange = info.get("higher")

    if higherRange is None:
        higherRange = lowerRange
        lowerRange = 0

    if ID.IsDigit(value):
        value = float(value)
        if value < lowerRange:
            return Message.clear(
                f"Out of range. Too low! (Lowest Value: {lowerRange})",
                timeS=1,
                colour=["red"],
            )
        if value > higherRange:
            return Message.clear(
                f"Out of range. Too high! (Highest Value: {higherRange})",
                timeS=1,
                colour=["red"],
            )
        return int(value)

    return Message.clear(
        "Invalid input! Not a `real` number", timeS=1, colour="light red"
    )

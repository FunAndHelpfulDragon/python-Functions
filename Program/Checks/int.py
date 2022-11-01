"""
Returns an int value if it's within a range.

Arguments:
---------
lower (int, Optional): lower range of the number. Defaults to 0
higher (int, Optional): higher range of the number. Defaults to 0
"""

def check(value, Message, ID, **info):
    lowerRange = 0
    higherRange = 0
    
    if "lower" in info:
        lowerRange = info["lower"]

    if "higher" in info:
        higherRange = info["higher"]
    
    if higherRange is None:
        higherRange = lowerRange
        lowerRange = 0
    
    if ID.IsDigit(value):
        value = float(value)
        if value < lowerRange:
            return Message.clear(f"Out of range. Too low! (Lowest Value: {lowerRange})", timeS=1, colour=["red"])
        if value > higherRange:
            return Message.clear(f"Out of range. Too high! (Highest Value: {higherRange})", timeS=1, colour=["red"])
        return int(value)
    
    return Message.clear("Invalid input! Not a `real` number", timeS=1, colour="light red")
from PythonFunctions.Convert import Location
from PythonFunctions.Logic import CheckNone
from PythonFunctions.Message import Message


def check(value, **info):
    position = Location(value)
    if CheckNone(*position):
        Message.warn("Invalid location specified", timeS=1)
        return None

    x = info.get('x')
    y = info.get('y')

    if position[0] > x:
        Message.warn('X value is too big!', timeS=1)
        return None

    if position[1] > y:
        Message.warn('Y value is too big!', timeS=1)
        return None

    return position

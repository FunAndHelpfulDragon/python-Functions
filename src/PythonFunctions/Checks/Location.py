from PythonFunctions.Convert import Location
from PythonFunctions.Logic import CheckNone
from PythonFunctions.Message import Message


def check(value, **info):
    position = Location(value)
    if CheckNone(position):
        return None

    x = info.get('x')
    y = info.get('y')

    if position[0] > x:
        Message.clear('X value is too big!', timeS=1)
        return None

    if position[1] > y:
        Message.clear('Y value is too big!', timeS=1)
        return None

    return position

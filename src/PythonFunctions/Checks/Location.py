import importlib

Convert = importlib.import_module('.Convert', 'PythonFunctions')
Logic = importlib.import_module('.Logic', 'PythonFunctions')
Message = importlib.import_module('.Message', 'PythonFunctions')

Location = Convert.Location
CheckNone = Logic.CheckNone


def check(value, **info):
    position = Location(value)
    if CheckNone(*position):
        Message.warn("Invalid location specified", timeS=1)
        return None

    x = info.get('x')
    y = info.get('y')

    if x is not None:
        if position[0] > x:
            Message.warn('X value is too big!', timeS=1)
            return None

    if y is not None:
        if position[1] > y:
            Message.warn('Y value is too big!', timeS=1)
            return None

    return position

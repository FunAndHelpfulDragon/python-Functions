import importlib

Message = importlib.import_module('.Message', 'PythonFunctions')


def check(value, **info):
    value = str(value)
    if len(value) == 0:
        return Message.clear(f"Please enter a value! ({info.get('info')}")
    return value in info.get("info")

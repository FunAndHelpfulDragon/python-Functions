from PythonFunctions.Message import Message


def check(value, **info):
    value = str(value)
    if len(value) == 0:
        return Message.clear(f"Please enter a value! ({info.get('info')}")
    return value in info.get("info")

import importlib

Save = importlib.import_module('.Save', 'PythonFunctions')
save = Save.save


def check(value, **___):
    if value == "":
        return False
    return save().CheckIfExists(value)

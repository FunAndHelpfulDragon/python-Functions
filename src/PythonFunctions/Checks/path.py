from PythonFunctions.Save import save

def check(value, **___):
    if value == "":
        return False
    return save().CheckIfExists(value)

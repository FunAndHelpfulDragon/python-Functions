"""
Returns True ("y") or False ("n")

Arguments:
----------
None
"""


def check(value, Message, ID, **_):
    value = value.strip()

    if len(value) == 0:
        return Message.clear("Invalid input! Nothing there")

    """
    If value[0] == "y", return True
    If value[0] == "n", return False
    If value[0] == ???, return None (Not valid value input)
    """
    return True if value[0] == "y" else False if value[0] == "n" else None

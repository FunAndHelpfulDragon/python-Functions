def checkInstances(instanceType: any, *obj: any) -> bool:
    """Checks if all of object are the of instance type

    Args:
        instanceType (any): The instance type to check against
        *obj (any): The items to check

    Returns:
        bool: Are they all instanceType
    """
    return not any(isinstance(item, instanceType) for item in obj)


def MultiCheck(*obj: any) -> bool:
    # Thanks Chat-GPT3
    """Checks if all of object are the same
    Note: mixing lists and other values won't work

    Args:
        *obj (any): The objects to test

    Returns:
        bool: Are they all the same?
    """
    same = True
    for item in obj:
        unique_values = set(item)
        same = len(unique_values) == 1

    return same


def CheckNone(*obj: any) -> bool:
    """Checks if all of object are None

    Args:
        *obj (any): The objects to test

    Returns:
        bool: Are they all none?
    """
    return any(o is None for o in obj)

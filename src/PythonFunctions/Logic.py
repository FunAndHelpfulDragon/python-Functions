def checkInstances(instanceType: any, *obj: any) -> bool:
    """Checks if all of object are the of instance type

    Args:
        instanceType (any): The instance type to check against
        *obj (any): The items to check

    Returns:
        bool: Are they all instanceType
    """
    for item in obj:
        if not isinstance(item, instanceType):
            return False

    return True


def MultiCheck(*obj: any) -> bool:
    """Checks if all of object are true
    Note: mixing lists and other values won't work

    Args:
        *obj (any): The objects to test

    Returns:
        bool: Are they all true?
    """
    for item in obj:
        if item is False:
            return False

    return True

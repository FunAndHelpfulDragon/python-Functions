from PythonFunctions.Logic import checkInstances


def test_check_all_bool():
    a: bool = False
    b: bool = True
    c: bool = True

    assert not checkInstances(bool, a, b, c)


def test_check_not_all_bool():
    a: bool = False
    b: bool = True
    c: float = 3.14

    assert not checkInstances(bool, a, b, c)


def test_check_all_int():
    a: int = 4
    b: int = 10
    c: int = 50

    assert not checkInstances(int, a, b, c)


def test_check_all_not_int():
    a: int = 4
    b: float = 3.14
    c: int = 40_318_280

    assert not checkInstances(int, a, b, c)

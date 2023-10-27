from src.PythonFunctions.TerminalDisplay import Display

dsp = Display()


def callback(value):
    """The test callback check function"""
    assert value is not None
    return value


def test_set():
    """Test to see if options are set correctly"""
    dsp.SetOptions(
        {0: (callback, "home"), 1: (callback, "Test1"), 2: (callback, "Test2")}
    )

    assert len(dsp.options) == 3


def test_add():
    """Tests to see if adding options works and is still correct"""
    dsp.AddOption(callback, "Test3")
    dsp.AddOption(callback, "Test4")

    assert len(dsp.options) == 5


def test_Remove():
    """Tests to see if removing an option removes an option"""
    # Checks to see if removing works
    cLen = len(dsp.options)
    dsp.RemoveOption(-2)
    assert len(dsp.options) == cLen - 1


def test_RemoveMore():
    cLen = len(dsp.options)
    dsp.RemoveOptions(1, 2)
    assert len(dsp.options) == cLen - 2


def test_RemoveAll():
    dsp.RemoveAllOptions()
    assert len(dsp.options) == 0

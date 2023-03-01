import sys
import os
from . import PythonFunctions, Colours
msg = PythonFunctions.Message.Message


def test_writeSetup():
    try:
        os.mkdir("TestSaveTemp")
    except FileExistsError:
        pass


def test_message():
    with open("TestSaveTemp/Msg.txt", "w", encoding="utf-8") as f:
        sys.stdout = f

        msg.warn("Testing")
        msg.clear("Testing 2")
        print("Test")

    with open("TestSaveTemp/Msg.txt", "r", encoding="utf-8") as f:
        line1 = f.readline().strip('\n')
        assert line1 == f"{Colours.CONSOLECOLOURS.Fore.ORANGE}Testing{Colours.Style.RESET_ALL}"
        line2 = f.readline().strip('\n')
        assert line2 == f"{Colours.CONSOLECOLOURS.Fore.RED}Testing 2{Colours.Style.RESET_ALL}"
        line3 = f.readline().strip('\n')
        assert line3 == "\x1b[2J\x1b[HTest"

    sys.stdout = sys.__stdout__


def test_cleanup():
    os.remove("TestSaveTemp/Msg.txt")
    os.removedirs("TestSaveTemp")

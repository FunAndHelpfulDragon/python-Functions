# Update checker mainly.

"""Init for all the modules
Lets us rename, skip declartion of stuff and more."""

import os


# Credit: Dragmine149
from . import Board, SaveModules, colours, run
from .Check import Check
from .CleanFolderData import Clean
from .Convert import LocationConvert as LocConv
from .Encryption import Encryption
from .IsDigit import IsDigit
from .Message import Message
from .PrintTraceback import PrintTraceback
from .Save import save
from .TerminalDisplay import Display
from .watermark import main as Watermark


canReadGlobal = True
try:
    import requests
except ModuleNotFoundError:
    print("Requests is not installed. Can not check for a new PythonFunction update!")
    canReadGlobal = False


def ReadLocal():
    localVersion = ""
    path = os.path.abspath(os.path.dirname(__file__))
    with open(f"{path}/Version.txt", "r", encoding="utf-8") as f:
        localVersion = f.read()
    return localVersion


def ReadGlobal():
    url = "https://raw.githubusercontent.com/FunAndHelpfulDragon/python-Functions/main/Version.txt"
    r = requests.get(
        url, timeout=60)
    if r != ReadLocal():
        print("Notice: A newer version of PythonFunctions is alvalible.")


if canReadGlobal:
    ReadGlobal()

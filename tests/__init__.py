"""Main folder containg the imports to other locations"""

import os
import sys

sys.path.append(os.getcwd())

# pylint: disable=wrong-import-position
from src import PythonFunctions
from src.PythonFunctions import Board, Colours, Check, Run, SaveModules
from src.PythonFunctions import CleanFolderData
from src.PythonFunctions.Convert import LocationConvert as LocConv
from src.PythonFunctions.Encryption import Encryption
from src.PythonFunctions.IsDigit import IsDigit
from src.PythonFunctions.Message import Message
from src.PythonFunctions.PrintTraceback import PrintTraceback
from src.PythonFunctions.Save import save
from src.PythonFunctions.TerminalDisplay import Display
from src.PythonFunctions.watermark import main as Watermark

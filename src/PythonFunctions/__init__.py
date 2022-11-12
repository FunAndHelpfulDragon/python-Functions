"""Init for all the modules
Lets us rename, skip declartion of stuff and more."""

# Credit: Dragmine149
from . import Board, colours, run
from .Check import Check
from .CleanFolderData import Clean
from .Convert import LocationConvert as LocConv
from .Encryption import Encryption
from .IsDigit import IsDigit
from .Message import Message
from .PrintTraceback import PrintTraceback
from .TerminalDisplay import Display
from .watermark import main as Watermark

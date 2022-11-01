# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# Main file of all code, Gets everything
from colorama.initialise import init, deinit, reinit, colorama_text
from colorama.ansi import Fore, Back, Style, Cursor
from colorama.ansitowin32 import AnsiToWin32

__version__ = '0.4.5-pre'

init()
"""Checks to see if inputted value matches some rules
"""

import importlib
import os
import dataclasses

from . import Checks
from . import IsDigit as ID
from .CleanFolderData import Clean
from .colours import c
from .Message import Message


# Check if the input is a valid input using a whole bunch of data
@dataclasses.dataclass
class Check:
    """Does some checks on the input.

    Please read the docmentation for a list of all the checks
    """

    def __init__(self) -> None:
        pass

    def __translate_Mode(self, data: str, mode: str, **info):
        """Loop through each alvalible check and do stuff

        Args:
            data (str): The data to check
            mode (str): The mode to check against

        Raises:
            NotImplementedError: If that check does not exists

        Returns:
            _type_: Result of the check
        """
        path_Location = os.path.realpath(__file__)
        path_Info = os.path.split(path_Location)
        for external in Clean().clean(f"{path_Info[0]}/Checks"):
            if external[:-3].lower() == mode.lower():
                module = importlib.import_module(f"{Checks.__package__}.{mode}")
                return module.check(data, Message, ID, **info)

        raise NotImplementedError(f"Mode: {mode} not implemented")

    def getInput(self, msg: str, mode: str, *, colour: str = "", **info):
        """Translate the user input, through the check and returns

        Args:
            msg (str): The message to display to the user
            mode (int): The check to run
            colour (str, optional): The text colour of the message. Defaults to "".
            info (Multipile): Other arguments for some checks

        Returns:
            _type_: The result of the check
        """

        # HAHAHA Force them to use colon space
        if msg.endswith(":") and not msg.endswith(" "):
            msg += " "
        elif not msg.endswith(": "):
            msg += ": "

        check = None
        while check is None:
            check = input(f"{c(colour)}{msg}{c()}")

            result = self.__translate_Mode(check, mode, **info)
            if result is None:
                check = None
                continue

            return result

        # If check is none, just send it back i suppose.
        return check

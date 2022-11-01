import importlib
from Program.Message import Message
from Program import IsDigit as ID
from Program.colours import c
from Program.CleanFolderData import Clean

# Check if the input is a valid input using a whole bunch of data
class check:    
    def __init__(self) -> None:
        """Does some checks on the input.
        
        Checks: Please read Documentation/Check.md
        """
        pass

    def __TranslateMode(self, data, mode, **info):
        for external in Clean.clean("Program/Checks"):
            if external[:-3] == str(mode):
                module = importlib.import_module(f"Program.Checks.{mode}")
                return module.check(data, Message, ID, **info)
        
        raise NotImplementedError(f"Mode: {mode} not implemented")
        
    def getInput(self, msg: str, mode:str, *, colour:str="", **info):
        """Translate the user input, through the check and returns

        Args:
            msg (str): The message to display to the user
            mode (int): The check to run
            colour (str, optional): The text colour of the message. Defaults to "".

        Returns:
            _type_: The result of the check
        """
        check = None
        while check is None:
            check = input(f"{c(colour)}{msg}{c()}")
            
            result = self.__TranslateMode(check, mode, **info)
            if result is None:
                check = None
                continue
            
        return check
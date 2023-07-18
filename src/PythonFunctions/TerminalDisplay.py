import inspect
import shutil
import time
import typing

from dataclasses import dataclass
from colorama import Fore, Back
from .Check import Check
from . import Message
from .utils import clamp
from .PrintTraceback import PrintTraceback

canRead = True
try:
    from readchar import key, readkey
except ModuleNotFoundError:
    canRead = False


@dataclass
class Numbers:
    high: int = 2_147_483_648
    low: int = -2_147_483_648


class Display:
    """The main class to give the user an option"""

    def __init__(self) -> None:
        if not canRead:
            print(
                "NOTE: readchar is NOT INSTALLED. This means you can only use list view"
            )

        self.options: typing.Dict = {}  # specific formaat.
        self.__storedText = None
        self.gridData = []
        self.__Number = Numbers()
        self.chk: Check = Check()
        self.cursorPosition = [0, 0]
        self.outMsg = None
        self.quitIsBack: bool = False

    def SetQuitMessage(self, msg: str):
        """Set the message to show on output

        Args:
            msg (str): The message to show
        """
        self.outMsg = msg

    def SetOptions(self, options: typing.Dict):
        """Set the program options

        Args:
            options (typing.Dict): The options to set
        """

        # Validation check
        cleanOptions = {}
        for option in options:
            if isinstance(options.get(option), tuple):
                newOptions = (
                    (options.get(option)[0],)
                    + (options.get(option)[1].replace(" ", "`-_-`"),)
                    + options.get(option)[2:]
                )

                cleanOptions.update({int(option): newOptions})
            else:
                print(
                    f"{option} with data {options.get(option)} has an invalid data"
                    " structure"
                )

        self.options = cleanOptions

    def AddOption(
        self, function, name: str, *, args: typing.Tuple = None, index: int = None
    ):
        """Add another option to the list

        Args:
            function (method): Callback function to call
            args (typing.Tuple): The information about the option to set
            index (int, optional): The index place to place the item
        """
        if index is None:
            index = len(self.options)

        self.options.update(
            {
                index: (
                    function,
                    name.replace(" ", "`-_-`"),
                )
                + (args,)
            }
        )

    def RemoveOption(self, index: int):
        """Remove an option at the selected index

        Args:
            index (int): The index to remove an option
        """
        return self.options.pop(index)

    def RemoveOptions(self, *index: int):
        """Remove all the options with the selected index

        Args:
            *index (int): The indexs to remove

        Returns:
            list: The list of removed options
        """
        removedOptions = []
        for item in index:
            removedOptions.append(self.options.pop(item))
        return removedOptions

    def RemoveAllOptions(self):
        """Remove all of the options in the list"""
        self.options = {}

    def ShowHeader(
        self, *, text: str = "Display.py", typewriter: bool = False, pace: int = 100
    ):
        """Print out a header message

        Args:
            text: (str, option) The text to display. Deafults to "Display.py".
            typewritter: (str, optional): Shows the text letter by letter. Defaults to False.
            pace: (int, optional): Words per second to show using typewritter effect.Defaults to 100
        """
        print(f"{Fore.GREEN}{'-' * shutil.get_terminal_size().columns}{Fore.RESET}")

        if typewriter:
            for i in text:
                print(i, end="", flush=True)
                time.sleep(pace * 0.001)
            print()
        else:
            print(text)

        print(f"{Fore.GREEN}{'-' * shutil.get_terminal_size().columns}{Fore.RESET}")

        self.__storedText = text

    def __GenerateGridData(self, lineLength=-1):
        """Generate the data of the grid. What goes where etc"""
        self.gridData = []
        row = []

        length, consoleLen = 0, shutil.get_terminal_size().columns  # Size limitations
        for index, itemIndex in enumerate(self.options):
            item = self.options.get(itemIndex)[1]

            # Go onto a new row if going to go over the limit
            if (length + 6) // consoleLen >= 1 or (
                lineLength > 0 and index % lineLength == 0 and index > 0
            ):
                row[len(row) - 1] = row[len(row) - 1].replace(" ", "")
                self.gridData.append(row)
                row = []
                length = 0

            row.append(f"{item}   ")
            length += len(item) + 3

        self.gridData.append(row)

    def __ShowGrid(self):
        """Prints out the grid generated in __GenerateGridData"""
        for yIndex, yValue in enumerate(self.gridData):
            for xIndex, xValue in enumerate(yValue):
                # Complicated string, but it calculates the square that should have the `> ` pointer
                v = (
                    f"{Back.BLUE}>{Back.RESET} {xValue}"
                    if self.cursorPosition[0] == xIndex
                    and self.cursorPosition[1] == yIndex
                    else xValue + "  "
                )
                v = v.replace("`-_-`", " ")

                print(v, end="")
            print()
        qm = "Quit" if not self.quitIsBack else "Back"
        print(
            f"""

Controls:
----------------------------------------------------------------------------
W/Up: Up, A/Left: Left, S/Down: Down, D/Right: Right, Q: {qm}, Enter: Select"""
        )

    def __ShowList(self):
        optionList = dict(sorted(self.options.items(), key=lambda ele: ele[0]))

        negList = []
        for opt in optionList:
            if opt <= 0:
                negList.append(opt)
                continue

            print(f"{opt:5}: {optionList.get(opt)[1].replace('`-_-`', ' ')}")
            self.__Number.high = opt

        print()

        if len(negList) > 0:
            self.__Number.low = negList[0]
            negList = reversed(negList)
            for item in negList:
                print(f"{item:5}: {optionList.get(item)[1].replace('`-_-`', ' ')}")

    def __GetListInput(self):
        try:
            v = self.chk.getInput(
                "Please enter the number you want to select: ",
                self.chk.ModeEnum.int,
                lower=self.__Number.low,
                higher=self.__Number.high,
            )
            if len(inspect.signature(self.options.get(v)[0]).parameters) > 0:
                return self.options.get(v)[0](*self.options.get(v)[1:])

            return self.options.get(v)[0]()

        except TypeError as TE:
            Message.clear(f"Invalid input! Reason: {TE}", timeS=2)
            PrintTraceback()
            return None

    def ShowOptions(
        self,
        *,
        useList: bool = False,
        requireResult: bool = True,
        lineLength: int = -1,
        quitIsBack: bool = False,
    ):
        """Returns the item at that index

        Args:
            useList (bool, optional): To show in a list or grid view. Defaults to False.
            requireResult (bool, optional): Require an input to be gathered. Defaults to True.

        Returns:
            _type_: The item returned
        """
        if not useList and canRead:
            self.cursorPosition = [0, 0]
            self.__GenerateGridData(lineLength)
            self.quitIsBack = quitIsBack
            self.__ShowGrid()
            if requireResult:
                return self.__MoveCursor()

        self.__ShowList()
        if requireResult:
            return self.__GetListInput()

        return None

    def __GetItemInfo(self, item: str):
        """Trys to find item in the list.

        Args:
            item (str): The item to find

        Returns:
            Tuple: The information about that item.
        """
        item = item.strip()
        for option in self.options:
            info = self.options.get(option)
            if info[1] == item:
                return info

        return None

    def __MoveCursorInformation(self, keyPress: str):
        if keyPress in ("W", "w", key.UP):
            return (0, -1)
        if keyPress in ("A", "a", key.LEFT):
            return (-1, 0)
        if keyPress in ("S", "s", key.DOWN):
            return (0, 1)
        if keyPress in ("D", "d", key.RIGHT):
            return (1, 0)
        return (0, 0)

    # Modified from chat gpt 3.5 rewrite
    def __MoveCursorIndex(self, cPos: typing.List, keyPress: str):
        # Get movement, if invalid just return 0,0
        moveX, moveY = self.__MoveCursorInformation(keyPress)

        currentX = cPos[0]
        currentY = cPos[1]

        newX = moveX + currentX
        newY = currentY

        rollOver = newX - (len(self.gridData[currentY]) - 1)
        if rollOver > 0 and newY + 1 < len(self.gridData):
            newX = rollOver - 1
            newY += 1

        newY += moveY

        x = clamp(newX, minValue=0, maxValue=len(self.gridData[newY]) - 1)
        y = clamp(newY, minValue=0, maxValue=len(self.gridData))

        return [x, y]

    def __MoveCursor(self):
        """Moves the cursor on the screen"""
        chosen = False
        while not chosen:
            k = readkey()
            if k == key.ENTER:
                chosen = True
                itemInfo = self.__GetItemInfo(
                    self.gridData[self.cursorPosition[1]][self.cursorPosition[0]]
                )

                if len(itemInfo) > 2:
                    return itemInfo[0](itemInfo[1:])

                return itemInfo[0](itemInfo[1])

            if k in ("Q", "q"):
                chosen = True
                return self.outMsg

            self.cursorPosition = self.__MoveCursorIndex(self.cursorPosition, k)

            # moves the cursor, Makes it look clearer
            print("\033[0;0H", end="")
            self.ShowHeader(text=self.__storedText)
            self.__ShowGrid()

        return None

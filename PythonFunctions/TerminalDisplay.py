import os
import typing
from .readchar import readchar
from . import colours
from . import Check
from . import Message

class Display:
    def __init__(self) -> None:
        self.options: typing.Dict = {}  # specific formaat.
        pass

    def SetOptions(self, options: typing.Dict):
        """Set the program options

        Args:
            options (typing.Dict): The options to set
        """
        # Validation check
        cleanOptions = {}
        for option in options:
            if type(options.get(option)) == tuple:
                newOption = options.get(option)[1].replace(" ", "_")
                cleanOptions.update(
                    {int(option): (options.get(option)[0], newOption)})
            else:
                print(
                    f"{option} with data {options.get(option)} has an invalid data structure")

        self.options = cleanOptions

    def AddOption(self, index: int, option: typing.Tuple):
        """Add another option to the list

        Args:
            index (int): The index to add
            option (typing.Tuple): The information about the option to set
        """
        newOption = option[1].replace(" ", "_")
        self.options.update({index: (option[0], newOption)})

    def RemoveOption(self, index: int):
        """Remove an option at the selected index

        Args:
            index (int): The index to remove an option
        """
        return self.options.pop(index)

    def ShowHeader(self, *, text: str = "Display.py"):
        """Print out a header message

        Args:
            text: (str, option) The text to display. Deafults to "Display.py".
        """
        print(f"""{colours.c('g')}{'-' * os.get_terminal_size().columns}{colours.c()}
{text}
{colours.c('g')}{'-' * os.get_terminal_size().columns}{colours.c()}""")

        self.__storedText = text

    def __GenerateGridData(self):
        """Generate the data of the grid. What goes where etc
        """
        self.gridData = []
        row = []

        length, consoleLen = 0, os.get_terminal_size().columns  # Size limitations
        for itemIndex in self.options:
            item = self.options.get(itemIndex)[1]

            # Go onto a new row if going to go over the limit
            if (length + 6) // consoleLen >= 1:
                row[len(row) - 1] = row[len(row) - 1].replace(" ", "")
                self.gridData.append(row)
                row = []
                length = 0

            row.append(f"{item}   ")
            length += len(item) + 3

        self.gridData.append(row)

    def __ShowGrid(self):
        """Prints out the grid generated in __GenerateGridData
        """
        for yIndex in range(len(self.gridData)):
            y = self.gridData[yIndex]
            for xIndex in range(len(y)):
                x = self.gridData[yIndex][xIndex]

                # Complicated string, but it calculates the square that should have the `> ` pointer.
                v = f"{colours.c('bgblue')}>{colours.c()} {x}" if self.cursorPosition[
                    0] == xIndex and self.cursorPosition[1] == yIndex else x

                print(v, end='')
            print()
        print("""

Controls:
---------------------------------------------------------
W: Up, A: Left, S: Down, D: Right, Q: Quit, Enter: Select""")

    def __ShowList(self):
        optionList = {key: val for key, val in sorted(
            self.options.items(), key=lambda ele: ele[0])}

        negList = []
        for opt in optionList:
            if opt < 0:
                negList.append(opt)
                continue

            print(f"{opt:5}:{optionList.get(opt)[1]}")
            self.__highest = opt

        print()

        self.__lowest = negList[0]
        negList = reversed(negList)
        for item in negList:
            print(f"{item:5}:{optionList.get(item)[1]}")

    def __GetListInput(self):
        try:
            v = Check.check().getInput("Please enter the number you want to select: ",
                                    "int", lower=self.__lowest, higher=self.__highest)
            return self.options.get(v)[0](self.options.get(v)[1])
        except TypeError:
            Message.Message().clear("Invalid input!", timeS=2, colour="red")
            return None

    def ShowOptions(self, *, list: bool = False):
        """Returns the item at that index

        Args:
            list (bool, optional): To show in a list or grid view. Defaults to False.

        Returns:
            _type_: The item returned
        """
        if not list:
            self.cursorPosition = [0, 0]
            self.__GenerateGridData()
            self.__ShowGrid()
            return self.__MoveCursor()

        self.__ShowList()
        return self.__GetListInput()

    def __MoveCursor(self):
        """Moves the cursor on the screen
        """
        chosen = False
        while not chosen:
            c = readchar.readchar().lower()
            if c == "w":
                self.cursorPosition[1] -= 1
                # Lock
                if self.cursorPosition[1] < 0:
                    self.cursorPosition[1] = 0

            elif c == "a":
                self.cursorPosition[0] -= 1
                # Lock
                if self.cursorPosition[0] < 0:
                    self.cursorPosition[0] = 0

            elif c == "s":
                self.cursorPosition[1] += 1
                # lock
                if self.cursorPosition[1] > len(self.gridData) - 1:
                    self.cursorPosition[1] = len(self.gridData) - 1

            elif c == "d":
                self.cursorPosition[0] += 1
                # Lock
                if self.cursorPosition[0] > len(self.gridData[self.cursorPosition[1]]) - 1:
                    self.cursorPosition[0] = len(
                        self.gridData[self.cursorPosition[1]]) - 1

            elif c == "\r":
                chosen = True
                return self.options.get(
                    self.gridData[self.cursorPosition[1]][self.cursorPosition[0]])[0](self.options.get(self.gridData[self.cursorPosition[1]][self.cursorPosition[0]])[1])

            elif c == "q":
                chosen = True
                return None

            # move the curspor position instead, as this saves memory and is easier to debug
            print("\033[%d;%dH" % (0, 0), end='')
            self.ShowHeader(text=self.__storedText)
            self.__ShowGrid()

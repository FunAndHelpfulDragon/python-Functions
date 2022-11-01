import typing
from Program.colours import c

# Everything to do with the board. Prints it and creates it.
class board:
    def __init__(self) -> None:
        """Board generation and display
        
        Functions (static):
        - CreateBoard
        - DisplayBoard
        """
    
    @staticmethod
    def CreateBoard(x: int, y: int, *, value: str='-') -> typing.List[typing.List]:
        """Create a 2D array that is like a board

        Args:
            x (int): The width
            y (int): the height
            value (str, optional): What to fill in the board with. Defaults to '-'.

        Returns:
            typing.List[typing.List]: The array result
        """
        board = []
        for _ in range(y):  # Y size (height)
            xLen = []
            for _ in range(x):  # X size (width)
                xLen.append(value)
            board.append(xLen)
        return board

    @staticmethod
    def DisplayBoard(board: typing.List[typing.List], *, colourInfo={}):
        """Displays the inputted board

        Args:
            board (typing.List[typing.List]): The board (2D array) to show
            colourInfo (dict, optional): The list of data that represent the colour of each value on the board. Defaults to {}.
        """
        for y in board:
            for x in y:
                if x in colourInfo:
                    print(f"{c(colourInfo[x])}{x}{c()}", end='')
                else:
                    print(x, end='')
            print()
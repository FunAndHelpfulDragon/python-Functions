# board.md

FILE: [Board.py](../src/PythonFunctions/Board.py)

## Usage

Used to quicky create a 2d array or display that 2d array. Useful for creating boards

```py
from PythonFunctions import board
brd = Board.create_Board(3, 5)
board.DisplayBoard(brd)
```

## Functions and argumnets

### CreateBoard

```py
brd = Board.CreateBoard(X, Y, Info='-')
```

This returns a board of X (required) by Y (required) with all the positions in the board being filled in with Info (optional string).
By default the board looks something like this: `[['-', '-', '-'], ['-', '-', '-']]` but you can change info to be whatever you want.

Required Arguments:

- X: int
- Y: int

Optional: Arguments

- Info

### Displaying a board

```py
Board.DisplayBoard(brd, {
    '-': 'red',
    '+': 'green'
})
```

This prints out the 2D array (board) so it looks like a board not an array. By taking in a required input of the 2d array (brd), and printing it line by line. The json dictionary also passed in is optional, but will change the colour of that symbol on the board. For the above example, anything in the board that is signified as "-" will be printed in the colour `red`.

#### DisplayBoard Args

Required:

- brd: 2d array (the board)

Optional:

- dict (json array)

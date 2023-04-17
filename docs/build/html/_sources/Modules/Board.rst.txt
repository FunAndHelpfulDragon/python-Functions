Board
=====

Last Updated: v1.5

.. code-block:: python

   from PythonFunctions import Board
   brd = Board.CreateBoard(5, 5)
   Board.DisplayBoard(brd)

Used to quickly create or display a 2d array of items.
Useful for creating boards for board games.

CreateBoard
-----------

To create a board, you can use the ``Board.CreateBoard()`` function

.. py:function:: Board.CreateBoard(x, y, *, param='-')
   :noindex:

   Returns a 2D array filled with value

   :param x: The width of the board
   :param y: The height of the board
   :param value: Optional, The default value to set each item. Defaults to '-'
   :type x: int
   :type y: int
   :type value: str
   :return: The 2D array
   :rtype: list[list[str]]

DisplayBoard
------------

Display a 2d array? Use this useful function.

.. py:function:: Board.DisplayBoard(brd, *, colourData, coords=False)
   :noindex:

   Prints out the 2D array in the terrminal

   :param brd: The 2D array
   :param colourData: Optional, The colour to make each item
   :param coords: Show the coordinates of the board on either side
   :type brd: list[list[str]]
   :type colourData: dict
   :type coords: bool

An example of colourData is shown below use Fore from colorama for the colours (or manually do the codes yourself)
Any unassigned values will be shown in the default colour (white)

.. code-block::python

   colourData = {
      "-": colorama.Fore.RED,
      "+": colorama.Fore.BLUE
   }

MultiBoardDisplay
-----------------

(with help from chatGPT)

Display multiple boards side by side in the terminal.

.. py:function:: Board.MultiBoardDisplay(*boards, colourData)
   :noindex:

   Return the message to print multiple boards

   :param boards: The boards to show. Can just be listed as (board, board, board) etc...
   :param colourData: Optional, The colour to make each item
   :type boards: tuple[list[list[str]]] (2D list one after another)
   :type colourData: dict
   :rtype: str
   :return: Message to print multiple boards.
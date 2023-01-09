Board
=====

.. code-block:: python

   from PythonFunctions import Board

Used to quickly create or display a 2d array of items.
Useful for creating boards for board games.

CreateBoard
-----------

To create a board, you can use the ``Board.CreateBoard()`` function

.. py:function:: PythonFunctions.Board.CreateBoard(x, y)

   Returns a 2D array

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

.. py:function:: PythonFunctions.Board.DisplayBoard(brd, colourData)

   Prints out the 2D array in the terrminal

   :param brd: The 2D array
   :type brd: list[list[str]]
   :param colourData: Optional, The colour to make each item
   :type colourData: dict

If you want to use the colourData option, assaign it like this, with the string on the left and the colour info (Read colours) as the colour

.. code-block::python

   colourData = {
      "-": "\033[32m",
      "+": "\033[31m"
   }

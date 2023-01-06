=====
Board
=====

This is one of the sub modules of these module, Which is used to create and display a 2d array.

Example
-------

>>> from Python_Functions import Board
>>> brd = Board.CreateBoard(3, 5)
>>> Board.DisplayBoard(brd)

Functions
=========

The functions, what they do and any errors that could arrise.

CreateBoard
-----------

To create a board of x by y use the ``PythonFunctions.Board.CreateBoard()`` function:
.. authofunction:: PythonFunctions.Board.CreateBoard

DisplayBoard
------------

.. .. code-block:: python
..     Board.DisplayBoard(brd, {
..         "-": "\033[31m"
..     })


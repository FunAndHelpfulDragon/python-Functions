Searching (Verison 2)
=====================

A module used to find a file, or multiple files in 

.. code-block:: python

    from src.PythonFunctions import Searching
    sch = Searching.search()

Locate
------

.. py:function:: Locate(target, *, directory, layers, hidden, logging):
    :noindex:

    Find a file with some paramters to help search for it.

    :param target: File to find.
    :param directory: Directory to search in. Defaults to current run directory (".").
    :param layers: How many layers above the specified directory to go. Defaults to 2.
    :param hidden: Limit the search by not searching these files / folders. Defaults to [].
    :param logging: To output what file in what folder is currently being searched. Defaults to False.
    :type target: List[str]
    :type directory: str
    :type layers: int
    :type hidden: List[str]
    :type logging: bool
    :returns: The location of target
    :rtype: List[str]

.. note::

    The hidden pararmater actually takes data from the clean module!

.. code-block:: python

    result = sch.Locate("Watermark.py", layers=0, hidden=[".venv", "*.pyc", "docs", "dist", "typings"], logging=True)
    print(result)

Clear
-----

.. py:function:: Clear()
    :noindex:

    Reset the class so you can use the same class but get different result.
    Should only be used if it isn't done automatically.
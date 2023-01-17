CleanFolderData (Version 2)
===========================

A module to take a folder, remove some random and unneccessary files, and give you a list / array of the outcome.

.. code-block:: python

    from PythonFunctions.CleanFolderData import Clean
    clean = Clean()

Usage
-----

.. py:function:: clean.clean(path, reserved)
    :noindex:

    The main function, Even can go through here of through one function at a time.
    This function does add some small things compaired to the other functions however.

    :param path: The path of the folder to "clean"
    :type path: str
    :param reserved: Optional, A list of files that are not included
    :type reserved: List[str]
    :return: A list of files that have been "cleaned"
    :rtype: List[str]

.. code-block:: python

    from PythonFunctions.CleanFolderData import Clean
    clean = Clean()
    result = clean.clean(".", ["secret.txt"])
    print(result) # Excepts everything but having hidden files and secret.txt in a list

GetData
-------

.. py:function:: clean.GetData(path)
    :noindex:

    Basically does the same thing as os.listdir(path).
    
    :param path: The path to list the information of
    :type path: str
    :return: A list of files from os.listdir, or path if it is a list
    :rtype: List[str]

.. note::
    If the path could not be found, then an empty list is returned

.. code-block:: python

    from PythonFunctions.CleanFolderData import Clean
    clean = Clean()
    result = clean.GetData(".")
    print(result) # Pretty much prints os.listdir(".")

RemoveHidden
------------

.. py:function:: clean.RemoveHidden(data)
    :noindex:

    Removes all hidden files, those that starts with `.` or `__`

    :param data: The data to remove hidden files from
    :type data: List[str]
    :return: A list of files without hidden files
    :rtype: List[str]

.. code-block:: python

    from PythonFunctions.CleanFolderData import Clean
    clean = Clean()
    result = clean.RemoveHidden(["a", "b", ".hidden", "__pycache", "", "hidden.txt"])
    print(result) # ["a", "b", "hidden.txt"]

RemoveReserved
--------------

.. py:function:: clean.RemoveReserved(data, reserved)
    :noindex:

    Removes all files in reserved from data.
    
    :param data: The data to remove files from
    :type data: List[str]
    :param reserved: The files to remove from data
    :type reserved: List[str]
    :return: A list of files without the files in reserved
    :rtype: List[str]

.. note::
    If a string gets passed instead of a list, then the program will error. I might fix this one day. --Drag

.. code-block:: python

    from PythonFunctions.CleanFolderData import Clean
    clean = Clean()
    result = clean.RemoveReserved(["a", "b", "hidden.txt"], ["hidden.txt"])
    print(result) # ["a", "b"]
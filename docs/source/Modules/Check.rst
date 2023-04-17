Check
=====

Last Updated: v1.5

A module to check the user input against some requirements.

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()


Usage
-----

.. py:function:: check.getInput(input, type, *, callback, rCheck=False, **info)
    :noindex:

    The main function, Basically every check is called through this

    :param input: The stuff to ask the user
    :param type: The check to run
    :param callback: The function to run after the user input. (Must be able to pick up at least 1 argument)
    :param rCheck: Returns the input value as well as check result
    :param info: Other arguments required for the check
    :type input: str
    :type type: check.ModeEnum
    :type callback: function.
    :type rCheck: bool
    :type info: any
    :return: Depends on the check
    :rtype: any

Everything is called and passed though the above function, however for some of the things to work more arguments are required as well.

ModeEnum
--------

This enum is a variable used for declaring the mode that the getInput function should call when it wants the input.
This enum contains all of the possible checks and is required to use.

Int Check
---------

.. py:function:: check.getInput(input, type, *, higher, lower)
    :noindex:

    The main function, but with all the arguments of an int check

    :param input: The stuff to ask the user
    :param type: The check to run.
    :param higher: Optional, The higher range value
    :param lower: Optional, The lower range value
    :type input: str
    :type type: check.ModeEnum.int
    :type higher: int
    :type lower: int
    :return: The result of the check (int = passed, none = failed)
    :rtype: int | None

.. note::
    If higher or lower aren't definied it will just check if it is an int value.
    If one or both are defined, then it will make sure the value is between that range (or smaller / bigger)

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Please enter a number between 1 and 10: ", check.ModeEnum.int, lower=1, higher=10)
    print(result)

Yes No Check
------------

.. py:function:: check.getInput(input, type, *, y, n, yA, nA)
    :noindex:

    The main function, but with arguments for a yes no check

    :param input: The stuff to ask the user
    :param type: The check to run.
    :param y: (Optional) The yes return function
    :param n: (Optional) The no return function
    :param yA: (Optional) Data to pass into the yes function
    :param nA: (Optional) Data to pass into the no function
    :type input: str
    :type type: check.ModeEnum.yesno
    :type y: function
    :type n: function
    :type yA: any
    :type nA: any
    :return: If yes or no got entered
    :rtype: bool

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Do you want to continue [Y/n]: ", check.ModeEnum.yesno)
    print(result)

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()

    def yesFunc(arg):
        print("Hello I win")
        print(arg)
    
    def noFunc(arg):
        print("*Cries* :(")
        print(arg)
    
    result = check.getInput("Win game? [Y/n]: ", check.ModeEnum.yesno, y=yesFunc, n=noFunc, yA='e', nA='*cries*')
    print(result)

.. note::
    If y or n does not exists and that is the function that is meant to be called (e.g. call yesFunc but it doesn't get passed)
    Then the value `True` or `False` will be returned depending on the context and input.
    `yA` and `nA` will be useless without the function `y` or `n`

.. note::
    By default, it will return the result of the function (if it returns), else it will return the result of True



Str Check
---------

.. py:function:: check.getInput(input, type, *, info)
    :noindex:

    The main function but with arguments for a str check

    :param input: The stuff to ask the user
    :param type: The check to run.
    :param info: The list to check the value against
    :type input: str
    :type type: check.ModeEnum.str
    :type info: tuple | list
    :returns: if input is in info
    :rtype: bool

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Vowel: ", check.ModeEnum.str, info=("a", "e", "i", "o", "u"))
    print(result)

Path Check
----------

.. py:function:: check.getInput(input, type)
    :noindex:

    The main function but with arguments for a path check.

    :param input: The stuff to ask the user
    :param type: The check to run.
    :type input: str
    :type type: check.ModeEnum.path
    :returns: if input is in info
    :rtype: bool | string

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Path: ", check.ModeEnum.path)
    print(result)

.. note::
    This uses the Save module and that file system structure, Please refer to that method for path information

Location Check (NEW)
--------------------

.. py:function:: check.getInput(input, type, *, x, y):
    :noindex:

    Converts a message over to a location and checks it.

    :param input: The stuff to ask the user
    :param type: The check to run
    :param X: (Optional), The bigger limit that X can be
    :param y: (Optional), The bigger limit that y can be
    :type input: str
    :type type: check.ModeEnum.Location
    :type x: int
    :type y: y
    :return: If input is in valid range. (Position)
    :rtype: list[int, int]

.. note::
    This uses the Convert.Location module. Please refer to that method for more information
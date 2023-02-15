Check (Version 2)
=================

A module to check the user input against some requirements.

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()


Usage
-----

.. py:function:: check.getInput(input, type, args)
    :noindex:

    The main function, Basically every check is called through this

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run
    :type type: check.ModeEnum
    :param args: Other arguments required for the check
    :type args: any
    :return: Depends on the check
    :rtype: any

Everything is called and passed though the above function, however for some of the things to work more arguments are required as well.

ModeEnum
--------

This enum is a variable used for declaring the mode that the getInput function should call when it wants the input.
This enum contains all of the possible checks and is required to use.

Int Check (Version 3)
---------------------

.. py:function:: check.getInput(input, type, *, higher, lower)
    :noindex:

    The main function, but with all the arguments of an int check

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run.
    :type type: check.ModeEnum.int
    :param higher: Optional, The higher range value
    :type higher: int
    :param lower: Optional, The lower range value
    :type lower: int
    :return: The result of the check (int = passed, none = failed)
    :rtype: int | None

.. note::
    If higher or lower aren't definied it will just check if it is an int value.
    If one or both are defined, then it will make sure the value is between that range (or smaller / bigger)

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Please enter a number between 1 and 10: ", check.ModeEnum.int, 1, 10)
    print(result)

Yes No Check (Version 2)
------------------------

.. py:function:: check.getInput(input, type, *, y, n)
    :noindex:

    The main function, but with arguments for a yes no check

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run.
    :type type: check.ModeEnum.yesno
    :param y: The yes return function
    :type y: function
    :param n: The no return function
    :type n: function
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

    def yesFunc():
        print("Hello I win")
    
    def noFunc():
        print("*Cries* :(")
    
    result = check.getInput("Win game? [Y/n]: ", check.ModeEnum.yesno, y=yesFunc, n=noFunc)
    print(result)

.. note::
    If y or n does not exists and that is the function that is meant to be called (e.g. call yesFunc but it doesn't get passed)
    Then the value `True` or `False` will be returned depending on the context and input.

.. note::
    By default, it will return the result of the function (if it returns), else it will return the result of True



Str Check (Version 1)
---------------------

.. py:function:: check.getInput(input, type, *, info)
    :noindex:

    The main function but with arguments for a str check

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run.
    :type type: check.ModeEnum.str
    :param info: The list to check the value against
    :type info: tuple | list
    :returns: if input is in info
    :rtype: bool

.. code-block:: python

    from PythonFunctions.Check import Check
    check = Check()
    result = check.getInput("Vowel: ", check.ModeEnum.str, info=("a", "e", "i", "o", "u"))
    print(result)
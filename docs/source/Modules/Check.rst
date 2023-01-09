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

Int Check (Version 3)
---------------------

.. py:function:: check.getInput(input, type, higher, lower)
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

Yes No Check (Version 1)
------------------------

.. py:function:: check.getInput(input, type)
    :noindex:

    The main function, but with arguments for a yes no check

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run.
    :type type: checck.ModeEnum.yesno
    :return: If yes or no got entered
    :rtype: bool
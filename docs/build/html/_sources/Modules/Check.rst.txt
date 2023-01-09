Check
=====

A module to check the user input against some requirements.

.. code-block:: python

    from PythonFunctions import Check
    check = Check()


Usage
-----

.. py:function:: check.getInput(input, type, args)

    The main function, Basically every check is called through this

    :param input: The stuff to ask the user
    :type input: str
    :param type: The check to run
    :type type: str
    :param args: Other arguments required for the check
    :type args: any
    :return: Depends on the check
    :rtype: any


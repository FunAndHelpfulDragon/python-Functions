Colours (Version 1)
===================

The terminal can now output text in colour instead of black and white.
Very useful for debugging error messages and making a user interface in the terminal.

.. note::
    This module will not work in an IDE unless it uses an integrated terminal. (It won't break, but won't print what is excepted.)

.. note::
    Windows command prompt users will need the module `Colourama`_ to be able to see the colours.
    If you are not on windows and can't see colours, try also downloading colourama and importing that into your program as well.

.. _Colourama: https://pypi.org/project/colorama/

There are multiple functions and not all in a class, making it easy to use.

.. code-block:: python

    from PythonFunctions import Colours as c

ConsoleFormat (Version 1)
-------------------------

.. py:function:: c.ConsoleFormat
    :noindex:

    :return: A tuple of dictionaries that contain all of the formats for all of the colours in terminal
    :rtype: Tuple[dict]

.. code-block:: python

    from PythonFunctions import Colours as c
    print(c.ConsoleFormat())

Print (Version 1.0.1)
---------------------

The same as the print command although you don't have to format the message with the colour codes beforehand.

.. note::
    You don't get access to all of the print features, and you can't get the actually raw text back.

.. py:function:: c.Print(msg, colour, options)
    :noindex:

    :param msg: The message to print
    :type msg: str
    :param colour: The foreground and background colour, if only one is supplied will be used as foreground. If left as None, default colour will be used.
    :type colour: List[str] | str
    :param options: Different ways to format the message, e.g. Bold Underline. Multiple can be passed in a list. If left as None, default colour will be used.
    :type options: List[str] | str

.. code-block:: python

    from PythonFunctions import Colours as c
    c.Print("Hello World!", ["black", "cyan"]) # Prints hello world but in black text on a cyan background.

Print.GetValue (Version 1)
--------------------------

A public method in the print class. This method returns the value that it last printed.

.. note::
    If you try and print this, you need to reset the colours otherwise everything beyond that point is going to be a different colour.
    Reset the colour py doing `print("\033[0m")` or `print(c.c())`

.. py:function:: c.Print().GetValue()
    :noindex:

    :return: The value last printed by `Print()`
    :rtype: str

.. code-block:: python

    from PythonFunctions import Colurs as c
    printer = c.Print("Hello World!", ["black", "cyan"])
    value = printer.GetValue() # Returns the same as above but without the reset value.

reverse (Version 1)
-------------------

Takes the colour code and outputs if it's a format type or colour type.

.. note::
    This does not return the name of the code but what category...
    Might update this at some point.

.. py:function:: c.reverse(code).reverse()
    :noindex:

    :param code: The code to find the type of
    :type code: str
    :return: The type or if it's not found
    :rtype: str | bool

.. note::
    Even though i put code in the class definition, you still have to use .reverse()

c (Version 1)
-------------

The simplist function

.. py:function:: c.c(name)
    :noindex:

    Returns the code that is found with the name specified.

    :param name: The name to get the code of.
    :type name: str
    :return: Thhe code if found.
    :rtype: str

colourRetrieve (Version 1)
--------------------------

.. note::
    This is not meant to be used as a class, yet its used for the function `c`
    It runs the back end code for `c`. and does pretty much exactully the same thing.

    Please use function `c` instead.
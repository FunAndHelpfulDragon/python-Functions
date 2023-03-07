Terminal Display (Version 2)
============================

A better and easier to use input system for the terminal, supports multiple modes.

.. code-block:: python

    from PythonFunctions.TerminalDisplay import Display
    display = Display()

.. note::
    Module `ReadChar`_ is required to get the interactive mode of the terminal.
    Use `pip install PythonFunctions[terminal] -U` to install readchar

.. _ReadChar: https://pypi.org/project/readchar/

SetOptions
----------

.. py:function:: SetOptions(options)
    :noindex:

    Sets the options for the terminal to display.

    :param options: The options to pass to the UI
    :type options: dict

Options Example
^^^^^^^^^^^^^^^

.. code-block:: python
    
    {
        1: (Callback, "Home"),
        2: (Callback, "Shop"),
        3: (Callback, "Wait"),
    }

Above is an example of how the dictionary should be laid out, index then tuple with a callback function along the value to show.
The number on the left only defines the position and can be negative. (Although they get treeted slightly differently).

.. note::
    You can pass in more than 2 arguments, anything else will be passed to the function that you desire as the callback.
    e.g. passing in `(Callback, "Home", 123)` will send `"Home"` and `123` to the function `Callback` once selected without showing `123` to the user.

AddOption
---------

.. py:function:: AddOption(value, *, index)
    :noindex:

    Add an option to the display. This can also update an existing option

    :param index: (Optional) Position to add it to. Defaults to length of all the options.
    :param value: Value to add the option (Must be like above)
    :type index: int
    :type value: tuple

RemoveOption
------------

.. py:function:: RemoveOption(index)
    :noindex:

    Remove the specified option from the list to display.

    :param index: The position to remove the option from
    :type index: int
    :returns: The value at that position
    :rtype: tuple    

RemoveOptions
-------------

.. py:function:: RemoveOptions(*index)
    :noindex:

    Remove all options specified

    :param index: The index to remove the option from
    :type index: int
    :return: The value at those positions
    :rtype: list

RemoveAllOptions
----------------

.. py:function:: RemoveAllOptions()
    :noindex:

    Clears the list

ShowHeader
----------

.. py:function:: ShowHeader(*, text, typewriter, pace)
    :noindex:

    Shows a header

    :param text: (Optional), Text to display in the header. Defaults to "Display.py"
    :param typewriter: (Optional), To make the text come out in a letter by letter. Defaults to False.
    :param pace: (Optional), speed to make the typewriter work. Defaults to 100.
    :type text: str
    :type typewriter: bool
    :type pace: int

.. note::
    1 second per letter = 1000 pace
    You can work out the rest from that.

ShowOptions
-----------

.. py:function:: ShowOptions(useList)
    :noindex:

    The main function shows all the options that have been specified.

    :param useList: (Optional) To use a list format instead of a interactive movable format
    :type useList: bool 
    :returns: The result of the callback function of the chosen input
    :rtype: any

SetQuitMessage
--------------

.. py:function:: SetQuitMessage(msg)
    :noindex:

    The message to show on quit. (Normaly done by using 'q' in terminal mode)

    :param msg: The message to show
    :type msg: str
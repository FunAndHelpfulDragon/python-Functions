Terminal Display (Version 2)
============================

A better and easier to use input system for the terminal, supports multiple modes.

.. code-block:: python

    from PythonFunctions.TerminalDisplay import Display
    display = Display()

.. note::
    Module `ReadChar`_ is required to get the interactive mode of the terminal.

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

.. code-block:: javascript
    
    {
        1: (Callback, "Home"),
        2: (Callback, "Shop"),
        3: (Callback, "Wait"),
    }

Above is an example of how the dictionary should be laid out, index then tuple with a callback function along the value to show.
The number on the left only defines the position and can be negative. (Although they get treeted slightly differently)

AddOption
---------

.. py:function:: AddOption(index, value)
    :noindex:

    Add an option to the display. This can also update an existing option

    :param index: Position to add it to
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

.. py:function:: ShowHeader(text)
    :noindex:

    Shows a header

    :param text: (Optional), Text to display in the header. Defaults to "Display.py"
    :type text: str

ShowOptions
-----------

.. py:function:: ShowOptions(useList)
    :noindex:

    The main function shows all the options that have been specified.

    :param useList: (Optional) To use a list format instead of a interactive movable format
    :type useList: bool 
    :returns: The result of the callback function of the chosen input
    :rtype: any
Colours
=======

Last Updated: v1.5

The terminal can now output text in colour instead of black and white.
Very useful for debugging error messages and making a user interface in the terminal.


Format
----

.. code-block:: python

    from PythonFunctions.Colours import Format
    from colorama import Style
    print(Format.BOLD + "hi" + Style.RESET_ALL) # Prints "hi" in bold.

Translate
---------

.. py:function:: Colours.Translate(string, Form):
    :noindex:

    Translate a string into a specific format

    :param string: String to Translate
    :param Form: Colour / Format / Style / Whatever to put on the string
    :type string: str
    :type Form: colorama.Form, colorama.Style, Colours.Format
    :rtype: str
    :return: the result

Revert
------

.. py:function:: Colours.Revert(string):
    :noindex:

    Revert a string back into the original form

    :param string: String to revert
    :type string: str
    :return: The result (either original or input)
    :rtype: str
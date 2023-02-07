Colours (Version 1)
===================

The terminal can now output text in colour instead of black and white.
Very useful for debugging error messages and making a user interface in the terminal.

.. note::
    Pretty much, what the point of this file was is now gone, for a good reason. Because i've removed all the functions.
    Whilst working on a different project, i had to make v1.3.1 which changed Colours to work better, As i was working on colours and already had colorama imported i decided to update it.
    The update consisted of removing the useless stuff, which is pretty much everything. Due to the fact that there were better ways to do that.
    I original made this module, over a year ago but now it must rest.

    Reasons for removing:
    - ConsoleFormat: Used dictionaries, now replaced with dataclasses
    - Print: Way less features than normal print, and way over complicated
    - Reverse: Who is giving you a code, and why do you need to find it?
    - c: you could literally put everything in the message field of a normal print object and use that instead. More customasiablity etc.
    - colourRetrieve: Worked when ConsoleFormat was a dictionary, now not as much.

    Colorama is now used for most things, and is installed by default. It can be found `here`_

.. _here: https://pypi.org/project/colorama/


DATA
----

.. note::
    This replaces the old ConsoleFormat function, but in a better way.

Before v1.4, the data about an code was sitting in a dictionary, requiring you to have to shift though the dictionary and get it out, which took time and looked bad.
However, since v1.4 it is all contained inside a class which makes it easier to import and for those using an ide like VSCode, easier to write.
This is like how `colorama`_ does their `Fore`, `Style`, `Back`, `Cursor` datasets

.. code-block:: python

    from PythonFunctions import Colours
    print(Colours.CONSOLEFORMAT.BOLD + "hi" + Colours.Style.RESET_ALL) # Prints "hi" in bold.
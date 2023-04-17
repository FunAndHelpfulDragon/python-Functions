Message
=======

Last Updated: v1.5

A couple of functions to print out a different style of message to the terminal.

clear
-----

.. py:function:: Message.clear(message, *, timeS, delete):
    :noindex:

    Clear the console screen

    :param message: (Optional), Message to show before clear (Message will be shown in red)
    :param timeS: (Optional), time to wait before clear
    :param delete: (Optional), Whever to use os.system('clear') or the fancy skip 100 lines
    :type message: str
    :type timeS: int
    :type delete: bool


wanr
----

.. py:function:: Message.warn(message, *, timeS):
    :noindex:

    Clear the console screen

    :param message: (Optional), Message to show (Message will be shown in orange/yellow)
    :param timeS: (Optional), time to wait before contining
    :type message: str
    :type timeS: int
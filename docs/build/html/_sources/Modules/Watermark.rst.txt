Watermark (Version 2)
=====================

.. code-block:: python

    from PythonFunctions.Watermark import watermark
    Watermark("HI")


watermark
---------

.. note::
    I have also added my information into this function as i made it and wanted credit. 

.. py:function:: watermark(name, twitter, youtube, github, *, colour)
    :noindex:

    :param name: Your name to display
    :param twitter: Link to twitter account
    :param youtube: Link to youtube account
    :param github: Link to github account
    :param colour: (Optional) The colour to make the `-` be.
    :type name: str
    :type twitter: str
    :type youtube: str
    :type github: str
    :type colour: str

LINKCODE
--------

.. py:function:: LINKCODE(link, text)
    :noindex:

    Makes a clickable link in the terminal.

    :param link: The link to redirect to
    :type link: str
    :param text: (Optional) The text to display. Defaults to the link.
    :type text: str
    :return: A message with a clickable link
    :rtype: str


TIME
----

.. py:function:: TIME()
    :noindex:

    Return a time in h,m,s format. Each value being 2 digits.

    :return: The current time of it being ran at.
    :rtype: tuple[str, str, str]

.. code-block:: python

    h, m, s = Watermark.Time()
    print(f"{h}:{m}:{s}") # Example: 14:03:20

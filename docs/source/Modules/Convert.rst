Convert
=======

Last Updated: v1.4.11

Converts cooridnates to the represented position

.. note::
    More things might get added, depends on if i need to conver stuff for ease.

.. code-block:: python
    
    from PythonFunctions.Conver import Location
    print(Location('A3')) # output: (0, 2)


Location
--------

.. py:function:: Location(position)
    :noindex:

    Translates letter to number and make a tuple

    :param position: The position to convert
    :type position: str
    :return: The position but split up and translated
    :rtype: tuple

AudioExtractor
--------------

.. note::
    Module `moviepy` needs to be installed for this to work.
    Install using `pip install PythonFunctions[audio] -U`

.. py:function:: AudioExtractor(path, destination)
    :noindex:

    Extracts a mp3 file from a mp4 file.

    :param path: The path to convert. (If directory, will do all of the directory)
    :type path: str
    :param destination: (Optional), where to place the files. Defaults to "mp3" in the runtime directory.
    :type destination: str
    :return: Message about the progress
    :rtype: str | None
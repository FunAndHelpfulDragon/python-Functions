Convert (Version 1.1)
======================

Converts cooridnates to the represented position

.. note::
    More things might get added, depends on if i need to conver stuff for ease.

.. code-block:: python
    
    from PythonFunctions.Conver import Location
    print(Location('A3')) # output: (0, 2)


Convert
-------

.. py:function:: Location(position)
    :noindex:

    Translates letter to number and make a tuple

    :param position: The position to convert
    :type position: str
    :return: The position but split up and translated
    :rtype: tuple
Convert (Version 1.1)
======================

Converts cooridnates to the represented position

.. note::
    More things might get added, depends on if i need to conver stuff for ease.

.. code-block:: python
    
    from PythonFunctions.Convert import LocationConvert as LC
    print(LC.Convert("A3")) # Output (0, 3)


Convert
-------

.. py:function:: LC.Convert(position)
    :noindex:

    Translates letter to number and make a tuple

    :param position: The position to convert
    :type position: str
    :return: The position but split up and translated
    :rtype: tuple
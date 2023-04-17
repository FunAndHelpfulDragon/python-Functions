PrintTraceback
==============

Last Updated: pre v1

.. code-block:: python

    from PythonFunctions.PrintTraceback import PrintTraceback
    
    try:
        raise ValueError()
    except ValueError:
        PrintTraceback()

This is all, just prints the traceback. Even though it's only 4 lines, (in the actuall source of the module), it can save more lines overtime.
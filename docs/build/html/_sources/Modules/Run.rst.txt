Run
===

Last Updated: v1.5

A module to store information about time, also works out calculations about time.

.. code-block:: python

    from PythonFunctions import Run

Mark
----

.. py:function:: Mark(name)
    :noindex:

    Adds a new marker

    :param name: (Optional) name to give the marker
    :type name: str
    :returns: The marker index
    :rtype: int

.. code-block:: python

    index = Run.Mark()
    print(index)

GetMarkTime
-----------

.. py:function:: GetMarkTime(name)
    :noindex:

    Get the time that mark X has

    :param name: The marker index to get the time of
    :type name: str
    :returns: The time at that point
    :rtype: float

.. code-block:: python

    time = Run.GetMarkTime(index)
    print(time)

CompareMarkers
--------------

.. py:function:: CompareIndex(a, b, roundVale)
    :noindex:

    Compare the marked times between a and b

    :param a: The first marker
    :param b: The second marker
    :param roundValue: (Optional), How many decimal places to round to. Defaults to -1 (none)
    :type a: int
    :type b: int
    :type roundValue: int
    :returns: The time difference
    :rtype: float
    :raise IndexError: One of the provided markers was not in range of all of the markers

.. code-block:: python

    # Get two different times
    a = Run.Mark()
    time.sleep(1)
    b = Run.Mark()

    # Compare
    dif = Run.CompareIndex(a, b)
    print(diff)

End
---

.. py:function:: End()
    :noindex:

    Return the amount of time has passed sinces the file got imported (started)

    :returns: Amount of time passed
    :rtype: float

.. code-block:: python

    print(Run.End())

Timer
-----

.. note::
    This is not used like the other functions.

The purpose of this is to check how long it takes a function to run. To use it follow the code below.

.. code-block:: python

    @Run.Timer
    def test():
        print('a')
        time.sleep(1)
        print('b')

This above code will print off `a` and `b` and the time it took. (`test took X seconds`).
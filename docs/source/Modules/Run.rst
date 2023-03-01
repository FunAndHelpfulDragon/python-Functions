Run (Version 3)
===============

A module to store information about time, also works out calculations about time.

.. code-block:: python

    from PythonFunctions import Run

Mark
----

.. py:function:: Mark()
    :noindex:

    Adds a new marker

    :returns: The marker index
    :rtype: int

.. code-block:: python

    index = Run.Mark()
    print(index)

GetMarkTime
-----------

.. py:function:: GetMarkTime(x)
    :noindex:

    Get the time that mark X has

    :param x: The marker index to get the time of
    :type x: int
    :returns: The time at that point
    :rtype: float
    :raise IndexError: The provided marker was not in range of all of the markers

.. code-block:: python

    time = Run.GetMarkTime(index)
    print(time)

CompareIndex
------------

.. py:function:: CompareIndex(a, b)
    :noindex:

    Compare the marked times between a and b

    :param a: The first marker
    :type a: int
    :param b: The second marker
    :type b: int
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
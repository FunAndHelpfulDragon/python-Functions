Version
=======

Last Updated: v1.5

A module designed to get the version of the package.

.. note::
    I wasn't planning on adding this in at first, but because of how stuff works out here it is.

.. code-block:: python

    from PythonFunctions import Version

CanReadGlobal
-------------

.. py:function:: CanReadGlobal()
    :noindex:

    :returns: If `requests` is installed
    :rtype: bool

ReadLocal
---------

.. py:function:: ReadLocal()
    :noindex:

    Gets the local version

    :returns: The local version
    :rtype: str

ReadGlobal
----------

.. note::
    Module `request`_  is required to run this function.

.. _request: https://pypi.org/project/requests/

.. py:function:: ReadGlobal()
    :noindex:

    Using request, gets the version off the server.
    (Timeouts after 60 seconds)

    :returns: The global (server) version
    :rtype:

.. note::
    Fun Fact! The server is actually just the github repositry.

Compare
-------

.. py:function:: Compare()
    :noindex:

    Using `ReadLocal` and `ReadGlobal` see if there is a new version.
    Prints out information about updating as well.
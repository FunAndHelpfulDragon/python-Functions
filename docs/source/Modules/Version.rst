Version (Version 2)
===================

A module designed to get the version of the package.

.. note::
    I wasn't planning on adding this in at first, but because of how stuff works out here it is.

.. code-block:: python

    from PythonFunctions import Version

LocalSettings
-------------

.. py:function:: LocalSettings():
    :noindex:

    Checks if the :ref: `muted <Mutting>` setting has been activated

    :returns: If `Mute` is true
    :rtype: bool

.. note::
    If `Mute` is true, you can still manually can the function to bypass it.
    Mute just makes sure it doesn't happen automatically

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
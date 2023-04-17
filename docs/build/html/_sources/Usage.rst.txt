Usage
=====

.. _installation:

.. note::
    All of these commands will say about a virtual enviroment, this is up to you.

Installation
------------

To use ``PythonFunctions`` first install it using pip:

(Using testpypi, developement builds)

.. code-block:: console

    (.venv) $ pip install -i https://test.pypi.org/simple/ Python-Functions

(Using pypi, stable build)

.. code-block:: console

    (.venv) $ pip install PythonFunctions

Optional Dependencies
---------------------

There are optional Dependencies which can be installed to improve the usability of the service.

Active (Might be useful for you):
- encryption

- google

- audio

- terminal

- all (Installs all of the above)


Development (Useful for adding new functions)

- tools

To install these, use the following code. Replace `module` with one of the above.

.. code-block:: console

    (.venv) $ pip install PythonFunctions[module]
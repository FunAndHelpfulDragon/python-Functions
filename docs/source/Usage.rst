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

Development (Useful for adding new functions)
- test
- linter

To install these, use the following code. Replace `module` with one of the above.

.. code-block:: console

    (.venv) $ pip install PythonFunctions[module]

.. _Mutting:

Muting the module
-----------------

Lets say, you are using an older version for a specific reason and you don't wont to upgrade yet. Well you can mute the output by making a file
By making the file ``PyFuncSet.json`` and attaching the code below, all update notifications will be muted. If file does not exists, it will not be muted.

.. code-block:: javascript

    {
        "Mute": true
    }


If you don't want to manually make the file, you can run the command below and then edit the file.

.. code-block:: console

    (.venv) $ python -m PythonFunctions -s
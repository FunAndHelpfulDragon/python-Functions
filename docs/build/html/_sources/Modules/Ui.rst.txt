Ui (Version 3)
==============

Some useful commands to make a UI using tkinter


.. code-block:: python
    
    from PythonFunctions.Ui import ui
    tkUi = ui()


FontSettings
------------

.. py:function:: FontSettings(*, font, size)
    :noindex:

    Change the font and size of the ui elements

    :param font: (Optional), The new font to use (Must be installed)
    :param size: (Optional), The new size of the font
    :type font: str
    :type size: int

.. code-block:: python

    tkUi.FontSettings(size=20)

CreateFrame
-----------

.. py:function:: CreateFrame(row, column)
    :noindex:

    Creates a new tk Frame

    :param row: (Optional). The row position. Defaults to 0
    :param column: (Optional). The column position. Defaults to 0
    :type row: int
    :type column: int
    :returns: The frame created
    :rtype: tk.Frame

.. code-block:: python

    frame:tk.Frame = tkUi.CreateFrame()

AddButton
---------

.. py:Function:: AddButton(text, callback, row, column, *, textVar, frame, sticky, callbackArgs, rowspan, columnspan)
    :noindex:

    Create a new tk button to interact with

    :param text: The text to dispaly on the button
    :param callback: The function to call on button click
    :param row: (Optional) The row of the frame to put the button in. Defaults to 0
    :param column: (Optional) The column of the frame to put the button in. Defaults to 0
    :param textVar: (Optional) The text variable to use instead of text. Defaults to None
    :param frame: (Optional) The frame to apply the button to. Defaults to None
    :param sticky: (Optional) The sides to stick to ("north", "east", "south", "west"). Defaults to "nesw"
    :param callbackArgs: (Optional) value to send to the function on callback. Defaults to True    
    :param rowspan: (Optional) How many rows does it take up. Defaults to 1
    :param columnspan: (Optional) How many columns does it take up. Defaults to 1
    :type text: str
    :type callback: function
    :type row: int
    :type column: int
    :type textVar: tk.StringVar
    :type frame: tk.Frame
    :type sticky: str
    :type callbackArgs: any
    :type rowspan: int
    :type columnspan: int
    :returns: The ui button element
    :rtype: tk.Button

.. code-block:: python

    button: tk.Button = tkUi.AddButton("Click me!", mycallback, 1, 1, frame=frame, callbackArgs="yes")

.. note::
    This does not contain all of the tk.Button options, if you want something that isn't here then use the actually tk.Button.
    If you want it added, file a pull request

AddLabel
--------

.. py:Function:: AddLabel(text, row, column, *, textVar, frame, sticky, rowspan, columnspan, image)
    :noindex:

    Creates a new tk Label to interact with.

    :param text: The text to display on the Label
    :param row: (Optional) The row of the frame to put the label in. Defaults to 0
    :param column: (Optional) The column of the frame to put the label in. Defaults to 0
    :param textVar: (Optional) The text variable to use instead of text. Defaults to None
    :param frame: (Optional) The frame to apply the label to. Defaults to None
    :param sticky: (Optional) The sides to stick to ("north", "east", "south", "west")
    :param rowspan: (Optional) How many rows does it take up. Defaults to 1
    :param columnspan: (Optional) How many columns does it take up. Defaults to 1
    :param image: (Optional) The image to display on the label. Defaults to None
    :type text: str
    :type row: int
    :type column: int
    :type textVar: tk.StringVar
    :type frame: tk.Frame:
    :type rowspan: int
    :type columnspan: int
    :tyoe image: tk.PhotoImage
    :returns: The label object
    :rtype: tk.Label

.. code-block:: python

    label: tk.Label = tkUi.AddLabel("", 0, 0, frame=frame)

.. note::
    This does not contain all of the tk.Labal options, if you want something that isn't here then use the actually tk.Button.
    If you want it added, file a pull request

AddTextBox
----------

.. py:function:: AddTextBox(textVar, row, column, *, frame, sticky, rowspan, columnspan, show)
    :noindex:

    Adds a text box to the UI which you can enter stuff into

    :param textVar: The text variable to assign data to.
    :param row: (Optional) The row position of the label. Defaults to 0
    :param column: (Optional) The column position of the label. Defaults to 0
    :param frame: (Optional) The frame to apply the label to. Defaults to None.
    :param sticky: (Optional) The sides to stick to ("north", "east", "south", "west")
    :param rowspan: (Optional) How many rows does it take up. Defaults to 1
    :param columnspan: (Optional) How many columns does it take up. Defaults to 1
    :param show: (Optional) The text to replace the input with. Defaults to ""
    :type textVar: tk.StringVar
    :type row: int
    :type column: int
    :type frame: tk.Frame
    :type sticky: string
    :type rowspan: int
    :type columnspan: int
    :type show: str

.. code-block:: python

    password = tk.StringVar()
    textBox = tkUi.AddTextBox(password, show="*")

.. note::
    show is a useful feature for hidding passwords

ChangeState
-----------

.. py:function:: ChangeState(element, state)
    :noindex:

    Show or hide an element

    :param element: Information about the element
    :param state: (Optional) state to make the element. Defaults to True
    :type element: dict
    :type state: bool

.. code-block:: python

    tkUi.ChangeState({"Element": textBox, "row": 0, "column": 10})

.. note::
    element needs to be a dictionary containing "Element" (if state is false) and "row", "column" (if state is true)

CreateStringVar
---------------

.. py:function:: CreateStringVar(frame, default)
    :noindex:

    Creates a tk.StringVar variable

    :param frame: The frame to attachs to. Defaults to self.canvas
    :param default: The default value to store in the variable
    :type frame: tk.StringVar
    :type default: str
    :returns: The object
    :rtype: tk.StringVar

.. code-block:: python

    pos = tkUi.CreateStringVar()
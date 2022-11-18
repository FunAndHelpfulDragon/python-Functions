# UI.py

[FILE](../src/PythonFunctions/ui.py)

## Usage

A system to easily make ui elements with the tkinter module (Up to a limit)
NOTE: More advanced tkinter features will require manualy modules import instead of using the template.

```py
from src.PythonFunctions.ui import ui

ui("Test").AddLabel("Hello World")
```

### Functions and arguments

#### FontSettings

```py
ui().FontSettings(("verdana", 20))
```

Changes the font settings

Required Arguments:

- Font: tuple (The font and size to change to)

#### CreateFrame

```py
frm = ui().CreateFrame()
```

Create another frame at position X, Y.

Optional Arguments:

- row: int (The row index)
- column: int (The column index)

Returns:

- frame: tk.Frame (The frame object)

#### AddButton

```py
btn = ui().AddButton("Hello", cbk)
```

Add in a clickable button with custom text and callback.

Required Arguments:

- text: str (Text to show on the button)
- callback: function (Callback of the function)

Optional Arguments:

- row: int (Row to place button on)
- column: int (Column to place button on)
- textvar: tk.StringVar (Text variable object)
- frame: tk.Frame (Element to add button to)
- sticky: str (What sides is it sticky to)
- rowspan: int (How many rows to span)
- columnspan: int (How many columns to span)

Returns:

- button: tk.Button (The button object)

#### AddLabel

```py
lbl = ui().AddLabel("Hello world")
```

Add a label to the ui

Required Arguments:

- text: str (The text on the label)

Optional Arguments:

- row: int (The row index position)
- column: int (The column index position)
- textVar: tk.StringVar (Text variable object)
- frame: tk.Frame (Element to add button to)
- sticky: str (What sides is it sticky to)
- rowspan: int (How many rows to cover)
- columnspan: int (How many columns to cover)

Returns:

- label: tk.Label (The label object)

#### AddTextBox

```py
tbx = ui().AddTextBox(tVar)
```

Creates a text box

Required Arguments:

- textVar: tk.StringVar (the text variable to assign data to / from (reading data))

Optional Arguments:

- row: int (Row position of the text box)
- column: int (Column position of the text box)
- text: str (Defult text in the text box)
- frame: tk.Frame (Frame to assign text box to)
- sticky: str (What sides to stick to)
- rowspan: int (How many rows to span)
- columnspan: int (How many columns to span)
- Show: str (The text to replace the input with, for passwords)

Returns:

- textBox: tk.Entry (The textbox)

#### ChangeState

```py
ui().ChangeState({
    "row": 0,
    "column": 0,
    "Element": tbx
})
```

Changes the state of an object, either hiding them or showing them (Default).

Required Arguments:

- Element: dict (Dictionary containg the information.)

- Element Layout: {
    "Element": (Required),
    "row": (Required on show),
    "column": (Required on show)
}

Optional Arguments:

- State: bool (the state of the button, true to show false to hide.)

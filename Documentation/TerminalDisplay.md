# Display.py

FILE: [Display.py](../PythonFunctions/TerminalDisplay.py)
Pass in a list of inputs, and get what the user choice in return.

## Usage

```py
from PythonFunctions import TerminalDisplay
dsp = Display()

def callback(value):
    print(f"{value} called back!")
    return value

dsp.SetOptions({
    1 : "Home",
    2 : "Back",
    -1: "Leave"
})
dsp.ShowHeader(text="Where do you want to go?")
result = dsp.ShowOptions()
```

The above example, does seem complicated at first, spamming over multiple lines. All this above function does is show a grid layout and lets the user chose what they want to select.

## Functions and arguments

### SetOptions

```py
dsp.SetOptions({
    1: (callback, "Home"), 
    2: (callback, "Unknown Shop"),
    3: (callback, "Wait")
})
```

This function sets the options that the user can select from in the class. In grid mode, the index doesn't really matter (except for the ordering) but in list mode it matters more

#### SetOptions Args

Required:

- dict of items (Must have a tuple as the option (might change!))

### AddOption

```py
dsp.AddOption(-2, (callback, "hi"))
```

This function adds an option to the list of already alvalible options. Makes it easy to reuse the class instead of reimporting it and having to make it over again.

#### AddOption Args

Required:

- Index: int (The index to add to)
- Value: tuple (The value to add)

### RemoveOption

```py
dsp.RemoveOption(-2)
```

This function removes an option from the list at the selected index, whilst also returning it for future use.

#### RemoveOption Args

Required:

- Index: int (The index to remove from)

### ShowHeader

```py
dsp.ShowHeader(text="Hello World")
```

This functions shows "Hello World" above the option chooicing area. Instead of it just being against a blank top with nothing to support it.

#### ShowHeader Args

Required: None
Optional:

- text: str (The text to show, Defaults to `Display.py`)

### ShowOptions

```py
rst = dsp.ShowOptions()
```

This is the main function, which actually displays the options that you have specified and lets the user decide what they want to select. After selecting an item, the callback function for that item is called.

#### ShowOptions Args

Required: None
Optional:

- list: bool (To show it in a list form, Defaults to False)

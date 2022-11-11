# Colours.py

FILE: [colours.py](../PythonFunctions/colours.py)

Brighten up your terminal with different colours.

## Usage

Instead of having like 1 class, for it there are multiple functions that do not work together (some do, but not mainly)

PLEASE NOTE: Some systems these may not work, or they may break overtime. (I might make an auto update script at some point for it)

### Functions and argumnets

#### ConsoleFormat

```py
from PythonFunctions import colours
colours.ConsoleFormat()
```

Turns out, colours are just how your format your message. This returns 2 json lists of which when placed before text in a string. Instead of using other complicated functions, this can just be done.

#### Print

```py
colours.Print("Hello World", "green")
```

Specilised print message. An alternative to the normal standard `print`, but with easier colour support.

Required Arguments:

- text: str (the message to print)

Optional Arguments:

- colour: list / string (the colour of the message, if list of len 2, will have one for foreground colour and background colour)
- format: list / string (the format of the message, can do a ton of things)

#### Reverse

```py
colours.reverse('\033[45m')
```

This takes a code and returns the type it is (or false if not found). In the future i plan on it to return more information.

Required Arguments:

- colour: str (The code of the colour to check)

#### c

```py
colours.c('red')
```

Simple function to return the colour of anything that you put into it. And very (i mean this) advanced function. This will work (or at least try) to get the colour from one letter. It doesn't only work on letters, the mod.

Examples:

- if the input was `fgr` it will return the colour code for make the text red.
- if the input was `bgr` it will return the colour code for making the background of the text red
- if the input was `` (nothing) it will return the colour code for reseting the colour back to the normal form.

As mentioned, very advanced function with a lot of usage.

Required Arguments:

- colour + format: str (The colour and format to get the item of. Format before colour)
# Colours.py

FILE: [colours.py](../Program/colours.py)

Brighten up your terminal with different colours.

## Usage

As it's a module with multiple functions, instead of giving one example then explination. You just get all the things instead.

PLEASE NOTE: Some systems these may not work, or they may break overtime. (I might make an auto update script at some point for it)

```py
import Functions
Functions.colours.ConsoleFormat()
```

Turns out, colours are just how your format your message. This returns 2 json lists of which when placed before text in a string. Instead of using other complicated functions, this can just be done.

```py
import Functions
Functions.colours.Print("Hello World", "green")
```

Specilised print message. An alternative to the normal standard `print`. If you only include the first string argument, it will print just normally. However, if you include other arguments it will change the output of the message. The second argumnent is the colour of the message, if this is an array it will change both the foreground and background colour. The third option will change some of the formatting and has up to 7 options.

```py
import Functions
Functions.colours.reverse('\033[45m')
```

This takes a code and returns the type it is (or false if not found). In the future i plan on it to return more information.

```py
import Functions
Functions.colours.c('red')
```

Simple function to return the colour of anything that you put into it. And very (i mean this) advanced function. This will work (or at least try) to get the colour from one letter. It doesn't only work on letters, the mod.

Examples:

- if the input was `fgr` it will return the colour code for make the text red.
- if the input was `bgr` it will return the colour code for making the background of the text red
- if the input was `` (nothing) it will return the colour code for reseting the colour back to the normal form.

As mentioned, very advanced function with a lot of usage.

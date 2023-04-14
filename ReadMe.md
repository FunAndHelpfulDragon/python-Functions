# Functions

This is a gigantic folder, with multiple functions for multiple use cases. The only folder that you will need, is [PythonFunctions](./src/PythonFunctions/).

## Information

Documentation: https://python-functions.readthedocs.io/en/latest/
PyPi: https://pypi.org/project/PythonFunctions/
Latest build (Might be of different version): https://python-functions.readthedocs.io/en/latest/
Contributing: [Contribute](Contribution.md)

## Update Log

### 1.5 (BETA)

NOTE: THIS IS BOUND TO CHANGE. DUE TO MULTIPLE SMALL UPDATES.

#### Added

- [Board.py](src/PythonFunctions/Board.py) `DisplayBoard` `coords` argument to show coordinates on the left and top of the board printout.
- [Board.py](src/PythonFunctions/Board.py) `MultiBoardDisplay` to display multiple boards at once side by side. (Thanks chatGPT)
- [Location](src/PythonFunctions/Checks/Location.py) to [Check.py](src/PythonFunctions/Check.py). Compares string with location
- `rCheck` to [Check.py](src/PythonFunctions/Check.py) to return the value as well as the results. (Defaults to false)
- `Translate` to [Colours.py](src/PythonFunctions/Colours.py) to 'Translates a string into the format specified' (documentation quote)
- [Logic.py](src/PythonFunctions/Logic.py) for random multi logic functions (All of X are Y instance, etc) (Also added test suite)
- [Save.py](src/PythonFunctions/Save.py) `GetModule` function to save a bunch of code in pass-through functions
- [Save.py](src/PythonFunctions/Save.py) `ListFolder` and `CheckIfExists` methods. (Also added to representive systems)
- [TerminalDisplay.py](src/PythonFunctions/TerminalDisplay.py) `requireResult` argument to `ShowOptions` for an input to be required (defualts to true)
- `true` and `false` to module (yep, i did that)

#### Updated

- [Check.py](src/PythonFunctions/Check.py) to not pass in the modules any more (isdigit, etc)
- [Check.INT](src/PythonFunctions/Checks/INT.py) with the ability to 'warn' instead of 'clear'
- [Check.PATH](src/PythonFunctions/Checks/path.py) to use `Save.py` `CheckIfExists` instead of `os`
- [Check.YN](src/PythonFunctions/Checks/yn.py), [Check.STR](src/PythonFunctions/Checks/str.py) to use modules instead of pass in
- Renamed [Colours.py](src/PythonFunctions/Colours.py) `FORMAT` to `Format`
- [Run.py](src/PythonFunctions/Run.py) to use a dictionary instead
- [Run.py](src/PythonFunctions/Run.py) to be able to name markers
- [Run.py](src/PythonFunctions/Run.py) functions according to the new marker system
- [Save.py](src/PythonFunctions/Save.py) with more error logging
- [Save.py](src/PythonFunctions/Save.py) passthough functions to use `GetModule`
- [TerminalDisplay.py](src/PythonFunctions/TerminalDisplay.py) works with temparary space replacement.
- [TerminalDisplay.py](src/PythonFunctions/TerminalDisplay.py) `MoveCursor` function to work with arrow keys, and be smaller and easier to expand. (Thanks chatGPT)

##### Git / Unrelated

- [Tests](./tests/) to use better import system than the previous 
- [.pylintrc](.pylintrc) with more disables. (Read file if you are intrested)

#### Fixed

- Issue where [Colours.py](src/PythonFunctions/Colours.py) was returning a number in Format instead of a ascii code
- Issue where [TerminalDisplay.py](src/PythonFunctions/TerminalDisplay.py) would not show any negative value options in list mode
- Issue where [Watermark.py](src/PythonFunctions/Watermark.py) `LINKCODE` would not display a clickable link if the shell didn't allow it.


#### Removed

- `Colorama` imports from [Colours.py](src/PythonFunctions/Colours.py)
- [Save.py](src/PythonFunctions/Save.py) `__GetFileInformation` due to not being used
- [Save.py](src/PythonFunctions/Save.py) `Save` function (Version 1.5 due removal)
- Some documentation from [Version.py](src/PythonFunctions/Version.py) (function explains itself)
- `Main` from [Watermark.py](src/PythonFunctions/Watermark.py) (Version 1.5 due removal)
- Bunch of imports from [Tests/init.py](tests/__init__.py)

To view all updates, Please view [Updates](Updates/ReadMe.md)

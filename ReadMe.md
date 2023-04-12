# Functions

This is a gigantic folder, with multiple functions for multiple use cases. The only folder that you will need, is [PythonFunctions](./src/PythonFunctions/).

## Information

Documentation: https://python-functions.readthedocs.io/en/latest/
PyPi: https://pypi.org/project/PythonFunctions/
Latest build (Might be of different version): https://python-functions.readthedocs.io/en/latest/
Contributing: [Contribute](Contribution.md)

## Update Log

### 1.5 (BETA)

#### Added

- Added check for file not existing in Save.Read (normal mode). Returns False instead
- Added `Save.ListFolder` to list folders.
- Instance to do multi instance functions
- Traceback to invalid option in list mode of terminal display.
- Added `CheckIfExists` to `Save`
- Added `rCheck` to `Check` to return the check value as well (defaults to false)
- Added `true`, `false` to `__init__.py` 
- Added `requireResult` to `TerminalDisplay.ShowOptions`

#### Updated

- Reworked `Run.py` to use a dictionary instead of an array
- Updated tests to not rely on the `__init__.py` file. (this is going to break something now isn't it?)
- Removed `colorama` from `colours`
- (with help of gpt3.5) reworked `TerminalDisplay.MoveCursor`.

#### Fixed

- Issue in `Checks.INT`
- Tests caused by `Run.py` rework
- issue with `TerminalDisplay.MoveCursor` not taking in arrow keys
- `Checks.INT` not being able to stop on an empty input.

To view all updates, Please view [Updates](Updates/ReadMe.md)

# Functions

This is a gigantic folder, with multiple functions for multiple use cases. The only folder that you will need, is [PythonFunctions](./src/PythonFunctions/).

## Documentation

Every file has it own documentation, which can be found here: [Documentation](https://python-functions.readthedocs.io/en/latest/).

## Expanding

This file is still in development and more is to come! If you want to contribute, follow the same file structure and submit a pull request.
What you see now is not the final version.

## Contributing

Please read [Contributing.md](Contribution.md)

## Update Log

### 1.4.5

#### Changed

- Changed default output message to `None` for those scripts which relayed on it. (instead of empty string)

### 1.4.4

#### Changed

- `Version.py` Compare with new option to mute the hint
- `__main__.py` to print the version instead of run the version compare function.

### 1.4.3

#### Added

- SetQuitMessage in `TerminalDisplay.py`
- `Message_test.py` to test messages (github)

#### Fixed

- An issue in `Message.py` causing `Message` to always be the output no matter the input message.

#### Removed

- `Beautifier.yml` as it required making a new branch to commit the changes (github)

### 1.4.2

#### Changed

- Fixed linter messages that got by the pylint test (Why did it not fail with a score under 10?)
- Updated Save decoder/encoder due to pylint.

### 1.4.1

#### Changed

- Moved update checker out of `__init__.py` to `__main__.py`

### 1.4

#### Added

- Way to view settings in terminal (and default values) (`-s` in `__main__.py`)
- Documentation in `__init__.py`
- Hint in `Version.py`

#### Changed

- `ConsoleFormat` to be a dictionary made up of classes instead
- `Colours` documentation
- Changed `-s` in `__main__.py` to `-gs` and `-s` (2 different functions)
- `Version.py` to work when offline and not crash
- `Version.py` request timeout to 10 seconds (from 60)
- `canReadGlobal` to a `ReadGlobal` and `CanReadGlobal`
- Every file that had a link to old `Colours` functions

#### Removed

- `Deprecated` module due to not working on wsl
- `Colours.Print` due to useless and less features.
- `Colours.reverse` Bit of a waste, and why don't you have to colour name if you are asking for code?
- `Colours.c` Mini function
- `Colours.colourRetrieved` woked when `ConsoleFormat` was a dictionary
- `Credits` as they didn't really do much

To view all updates, Please view [Updates](Updates/ReadMe.md)

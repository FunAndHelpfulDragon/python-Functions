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

### 1.4.10

#### Added

- AudioExtractor in `Convert.py`
- AudioExtractor to `Convert.py` documentation
- New optional dependiences installation options.
- `Watermark.py` `LINKCODE` function. (link + text)
- `Watermark.py` `TIME` function. (Just gets the hour, minute second)
- Relative documentation for `Watermark.py`

#### Updated

- `Save.py` `Read` and `Write` function to use `*` before the encoding argument.
- renamed `Save.py` `Write` function from `Save` to `Write`. (But left `Save` in as a redirect to `Write` until `1.5.0` and gave a warning)
- Updated `Save.py` documentation
- Updated `pyproject.toml` to use move optional dependecies.
- Updated related documentation to include the optional dependience installation instructions.
- Regenerated the whole documentation in `docs/build`
- `Watermark.py` to make it more readable and so more functions can be used elsewhere.
- `Watermark.py` to have a default file name of `__main__`
- Renamed `main` in `Watermark.py` to `watermark`. (Like save, left main as a redirect and gave a warning)
- Updated some backend github code.
- Updated documentation for `tests/`
- Updated some tests (not much though)
- Fixed pylint complaining at a doc by making it disabled in that file. (`docs/source/conf.py`)

#### Fixed

- `Save.py` test with the new `encoding` argument.
- Other random files that got broken with the `Save.py` update.
- Some pylint issues
- Tests that got broken


### 1.4.9

#### Added

- Added notes to `Colours.py` documentation.
- `Check.py`: Added option to check if an input is a valid path on the os.
- `Check.py`: Added a callback function option that gets called after the user enters a result.

#### Changed

- Updated `Check.py`, `Colours.py`, `Convert.py` documentation
- Updated testing for `Check.py`
- Went back to the `Added`, `Changed`, `Removed` format.

#### Fixed

- Fixed issue with `Message.py` not being happy after `Colours.py` update.
- Fixed some tests

#### Removed

- Removed most of the data from `Colours.py` due to being in `Colorama`
- Removed class out of `Convert.py`

### 1.4.8

- Added arrow key support in terminal display.
- Added timer function wrapper to run.py
- Added `includeHidden` to `CleanFolderData.py`
- Updated documentation
- Updated Searching to always search hidden directories by default unless excluded.
- Removed `None` that appears in `search.Locate` with `Logging` enabled

### 1.4.7

- Added `ui.CreateImage`
- Updated `ui.AddButton` to include image option.
- Updated `ui.AddButton` to use a better callback function
- Updated `ui.ChangeState` to not use a dictionary but instead pass in each argument.
- Updated documentation
- Disabled `__main__.py` `GenerateSettings` and `Settings`
- Removed `Version.LocalSettings`
- Removed `Version.Compare` saying to make the "PyFuncSet.json" file

### 1.4.6

- Added return function support to `yes no check`
- Added tests (github)
- Changed yes no check to support capital letters (now makes them lowercase before compare)
- Updated documentation
- Went back to old update log form.
- Fixed documentation warnings

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

### 1.4.0

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

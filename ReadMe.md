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

### 1.2.0

- Bumbed versions
- Added `Version.py` documentation
- Updated `Version.py` to make sure that you are on the newest version using `>`
- Updated `__init__.py` to include the new `Version.py` function
- Fixed issues with pypi and version numbering. (Reason to bumb versions as well)
- Fixed an issue slowly causing `Version.py` to break (was todo with my version updater module.)
- Moved `cryptography` from requirements to optional requirements.

Updates before 1.2.0 are in [Updatelog.md](Updatelog.md)

## Credits

This project uses functions and modules from other people to run. Most of the modules have been auto imported (and kept up to date) but some require you to manually install them (check that module infomation).

### Colourama

[Github](https://github.com/tartley/colorama)
Brings colours to the terminal

### Readchar

[Github](https://github.com/magmax/python-readchar)
Taking an input straight away, instead of getting the user to press enter afterwards

### Cryptography

[Github](https://github.com/pyca/cryptography)
Encrypting and decrypting data. Quick and simple

### Requests

[Github](https://github.com/psf/requests)
Checking if you have the latest version

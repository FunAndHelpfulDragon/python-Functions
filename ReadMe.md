# Functions

This is a gigantic folder, with multiple functions for multiple use cases. The only folder that you will need, is [PythonFunctions](./src/PythonFunctions/).

## Documentation

Every file has it own documentation, which can be found here: [Documentation](https://python-functions.readthedocs.io/en/latest/).
Outdated (ish) but local documents can be found here: [Local documentation](Documentation/ReadMe.md)

## Expanding

This file is still in development and more is to come! If you want to contribute, follow the same file structure and submit a pull request.
What you see now is not the final version.

## Contributing

Please read [Contributing.md](Contribution.md)

## Update Log

Please see [Updatelog.md](Updatelog.md) for updates after the latest update

For versions before `1.1.0` please see the test.pypi directory.

### 1.1.4

- Fixed issue with CleanFolderData.clean() not working due to resvered not being a string

### 1.1.3

- Added `*.txt` (wildcard) support to CleanFolderData.RemoveReserved()
- Added str support to CleanFolderData.RemoveReserved() (You can pass in a string now without it breaking)
- Updated testing to include `*.txt` support

### 1.1.2

- Fixed issue with getting server version.

Updates before 1.1.2 are in [Updatelog.md](Updatelog.md)

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

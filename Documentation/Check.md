# Check.py

FILE: [Check.py](../PythonFunctions/Check.py)

Get a string from the user, and returns the value... After passing through some checks

## Usage

```py
from PythonFunctions import check
chk = check()
result = chk.getInput("Testing (int): ", "int", lower=0, higher=10)
```

Above is one example of what this class can be used for, This returns the user int if it's in range 0 to 10.

## Functions and Arguments

Instead of multiple functions, everything is called via the one function but with different inputs listed below.

```py
check().getInput("Testing (int)", "int", lower=0, higher=10)
```

### Agumnets

Required:

- Msg (str): The message to display to the user
- Mode (str): The check to run

Optional:
These are dependant on what the script wants, please check the documentation for that script (normally found in the file)

## Checks

There are multiple checks, which have their own [folder](../PythonFunctions/Checks/) to contain them all, Mainly because it's easier to add new checks and more.

[Check Documentation](../PythonFunctions/Checks/ReadMe.md)

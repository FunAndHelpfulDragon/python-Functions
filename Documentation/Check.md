# Check.py

FILE: [Check.py](../Program/Check.py)

Get a string from the user, and returns the value... After passing through some checks

## Usage

```py
import Functions
chk = Functions.check()
result = chk.getInput("Testing (int): ", 1, lower=0, higher=10)
```

Above is one example of what this class can be used for, This returns the user int if it's in range 0 to 10.

## Arguments

Instead of multiple functions, everything is called via the one function but with different inputs listed below.

### Required

- Msg (str): The message to display to the user
- Mode (str): The check to run

### Optional

These are dependant on what the script wants, please check the documentation for that script (normally found in the file)

## Checks

There are multiple checks, which have their own [folder](../Program/Checks/) to contain them all, Mainly because it's easier to add new checks and more.

[Check Documentation](../Program/Checks/ReadMe.md)

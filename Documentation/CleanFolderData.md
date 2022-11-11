# CleanFolderData.py

FILE: [CleanFolderData.py](../PythonFunctions/CleanFolderData.py)
Cleans the folder data returned by os.listdir to not include any hidden or reserved files

## Usage

```py
from PythonFunctions import Clean
folder = Clean().clean(".")
```

Above is an example that will remove files starting with `.` or `__` in the folder that the program is run. And returns the list.

## Function and Arguments

### GetData

```py
data = Clean().GetData("PythonFunctions")
```

This returns all the files and folders stored in the path `PythonFunctions` Basically the same as doing `os.listdir("PythonFunctions")`.

Required Arguments:

- path: str (where to list folder and file data)

### RemoveHidden

```py
data = Clean().RemoveHidden(data)
```

This removes all the hidden files that the pervious function returns. The hidden files are files that startswith `.`or `__`.

Requierd Arguments:

- data: list[] (A list of strings)

### RemoveRserved

```py
data = Clean().RemoveReserved(data, reserved=["name.txt", "Reserved.md"])
```

This removes all files in data that are also in the reserved list. Currently does not support file syntax with `*.py` or `b*`

Required Arguments:

- data: list[] (A list of strings)
- reserved: list[] (Another list of strings)

### clean

```py
data = Clean().clean(".", [".secret"])
```

This does the same thing as all 3 above functions do. Just automatic and with some more checks.

Required Arguments:

- path: str (The path to clean)
- reserved: list (A list of strings to remove from the path)

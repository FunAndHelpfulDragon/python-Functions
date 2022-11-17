# Run.py

FILE: [Run.py](../src/PythonFunctions/run.py)

Keep track of how long peices of code are takin to run using this module.

## Usage

On import of the functions module, this module has already logged the time and is ready for action. As there are multiple small use functions, they will be explained one by one.

### Functions and Arguments

#### Mark

```py
from PythonFunctions import run
index = run.Mark()
```

This takes the current time (when it gets runs) and stores it for later use. Basically marking a point in time for retrieval later.

#### GetMarkTime

```py
from PythonFunctions import run
run.GetMarkTime(0)
```

This returns the time stored at that point in the list. The index is returned from `run.Mark()` or you could enteer a random index

Required Arguments:

- index: int (The index to get the time of)

#### CompareIndexx

```py
from PythonFunctions import run
difference = run.CompareIndex(0, 4)
```

This returns the difference between the time at the two indexs stored. This does require some call of mark to be used first before hand though. ALl this does is save some code (and time) as you don't have to read from the list then compare it.

Required Arguments:

- Index0: int (The first position)
- Index1: int (The second position)

#### End

```py
from PythonFunctions import run
difference = run.End()
```

The last function of the set, this function returns the time since the program has been imported.

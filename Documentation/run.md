# Run.py

FILE: [Run.py](../Program/run.py)

Keep track of how long peices of code are takin to run using this module.

## Usage

On import of the functions module, this module has already logged the time and is ready for action. As there are multiple small use functions, they will be explained one by one.

```py
import Function
index = Functions.run.Mark()
```

This takes the current time (when it gets runs) and stores it for later use. Basically marking a point in time for retrieval later.

```py
import Functions
Functions.run.GetMarkTime(0)
```

This returns the time stored at that point in the list. The index is returned from `run.Mark()` or you could enteer a random index

```py
import Functions
difference = Functions.run.Compare(5.34, 3.2)
```

This returns the difference between the two numbers. Basically a simple caculation of `b-a` and which really didn't need to be in here. But is so...

```py
import Functions
difference = Functions.run.CompareIndex(0, 4)
```

This returns the difference between the time at the two indexs stored. This does require some call of mark to be used first before hand though. ALl this does is save some code (and time) as you don't have to read from the list then compare it.

```py
import Functions
difference = Functions.run.End()
```

The last function of the set, this function returns the time since the program has been imported.

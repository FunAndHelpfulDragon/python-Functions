# Convert.py

FILE: [Convert.py](../src/PythonFunctions/Convert.py)

Converts cooridnates to the represented position

## Usage

```py
from PythonFunctions import LocationConvert
position = LocationConvert().Convert("A3")  # returns (0, 3)
```

As there is only one function, not much is going to be explained. This returns the coodinates in a tuple of numbers from letters.

### Function and arguments

```py
position = LocationConvert().Convert("A3")
```

Returns the tuple at position `"A3"` (in python terms, so `(0, 3)`).

Required Arguments:

- Position: str (The position to get the location for)

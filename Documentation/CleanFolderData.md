# Clean Folder Data

FILE: [CleanFolderData.py](../Program/CleanFolderData.py)
Cleans the folder data returned by os.listdir to not include any hidden or reserved files

## Basic Usage

```py
import Functions
clean = Functions.Clean()
data = clean.clean("../Program")
print(data)
```

Above is the bare minimum to get this to work, This takes the folder `../Program` and returns a list without specified rules.
This function does everything that the below functions do in one.

## Functions and more

```py
# Returns the data stored in '../Program'
data = clean.GetData(path="../Program")
```

Here `path` is of type string, and `data` is of type list. The program will allow path to be a list but will just return the list instead of any folers that list might find

```py
# Returns the data without files starting with '.' or __'
data = clean.RemoveHidden(data=["Temp.md", ".Hidden", "__pycache__"])  # Returns ["Temp.md"]
```

Here `data` is of type list, for both in and out. The first data can be renamed if you want, but it's easier and recommended to just use the output as the new data.

```py
# Returns the data without files in the reserved list (if any)
data = clean.RemoveReserved(data=["Temp.md", "name.txt", "Game", "Reserved.md"], reserved=["name.txt", "Reserved.md"])  # returns ["Temp.md", "Game"]
```

Here `data` is of type list, `reserved` is of type list.

```py
# Returns the finished product of all of the above functions.
data = clean.clean(path="../Program", reserved=["Info.md"])
```

Here `data` is of type list, `path` is of type string, `reserved` is of type list. This does the above 3 functions but all in one.
NOTE: `reserved` here is optional and does not have to be included.

# Save.py

FILE: [Save.py](../src/PythonFunctions/Save.py)

## Usage

A system to easly write, read, delete data. with support of multiple file systems and encryption levels

```py
from src.PythonFunctions import save

sv = save() # initilise class
sv.Save("Hello World", "tmp.txt", [sv.encoding.BINARY])
data = sv.Read("tmp.txt", sv.encoding.BINARY)
print(data)
```

### Supporting other file systems

As i plan to add in support for more file systems in the future, you will need to use a different prefix to interact with those apis and file systems.

These prefixes are:

- `nml://` (Normal)
- `gdr://` (Google drive)
- `ftp://` (File transfer protocol)
- `oth://` (Other)

By including one of them at the start, you will use that file system instead of the default file system.

If you want to support a file system / api that i don't support, you will need to use `oth://{system}://` (once i've added in this support). If you want to add in a system by default, then submit a pull request and i'll look into it.

### Functions and arguments

Notes:

- on class initilise, you might get asked for a passcode. This is to enocde your data if the module [Cryptography](https://github.com/pyca/cryptography) is installed.
- If the path does not exists, then the system will make the folders first before doing stuff
- The `encoding` argument in some functions, can be a list or just one value. If it is a list it will encode / decode multiple times before reaching the output. (Following the order in the list).

#### Save

```py
sv = save()
sv.Save("Hello World", "tmp.txt", [sv.encoding.BINARY])
```

Save the specified data to a file using the specified encoding.

Required Arguments:

- data: any (The data you want to save)
- path: str (Where to save the data to)

Optional Arguments:

- encoding: sv.encoding (The type of encoding)

#### Read

```py
sv = save()
data = sv.Read("tmp.txt", sv.encoding.BINARY)
print(data)
```

This decodes the file and prints the output.

Required Arguments:

- path: str (The path to read from)

Optional Arguments:

- encoding: sv.encoding (The type of encoding.)

**Note abount encoding argument**:
If it's a list, it will do the reverse order of the list. This is so you can put in the same list and it will decode without you having to change the list at all.

#### MakeFolders

```py
sv = save()
sv.MakeFolders("Test1")
```

Make a folder (or folders). will use the run path as the default parent.

Required Arguments:

- path: str (Path to create the folder at)

#### RemoveFile

```py
sv = save()
sv.RemoveFile("tmp.txt")
```

Remove the file at path.

Required Arguments:

- path: str (Path to remove the file from)

##### RemoveFolder

```py
sv = save()
sv.RemoveFolder("Test1")
```

Remove the folder and all subdirs of that folder.

Required Arguments:

- path: str (Path to remove the folder from.)

#### ChangePasscode

```py
sv = save()
passcode = sv.ChangePasscode()
```

Change the stored passcode and return it.

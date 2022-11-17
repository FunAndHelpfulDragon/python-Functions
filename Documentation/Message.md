# Message.py

FILE: [Message.py](../src/PythonFunctions/Message.py)

Another way to handle logging stuff in the console

## Usage

```py
from PythonFunctions import Message
Message.warn("Hello World", timeS=2)
Message.clear("Goodbye", timeS=2)
```

Above are some examples of what you can do. There are more things that can also be done and more detail about things.

### Function and arguments

Both functions take the same base arguments, but clear takes more optional arguments.

Optional Argumnets:

- Message: str (Message to print)
- timeS: int (Time to wait before continuing)
- colour: array (Colour of the message, see [colours.md](./colours.md))

Clear Optional Argument ONLY

- Delete: bool (Whever to use the clear command, or just to print a whole bunch of empty lines)

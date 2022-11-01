# Message.py

FILE: [Message.py](../Program/Message.py)

Another way to handle logging stuff in the console

## Usage

```py
import Functions
Functions.Message.warn("Hello World", timeS=2)
Functions.Message.clear("Goodbye", timeS=2)
```

Above are some examples of what you can do. There are more things that can also be done and more detail about things.

```py
Functions.Message.warn()
```

By default, will just print nothing. But will accept arguments to print whatever you need.

### Arguments

Message (message to print): str (Example: `"Hello World"`)

timeS (time to wait before continuing): int (Example: `3`)

colour (colour of the message): [] (Example: `["red", "black"]`)

- Note: you do not need all the colours here, one will do just fine

Using all arguments it looks something like this:

```py
Functions.Message.warn("Hello World", timeS=3, colour=["red", "black"])
```

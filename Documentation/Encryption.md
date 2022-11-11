# Encryption.py

FILE: [Encryption.py](../PythonFunctions/Encryption.py)

Encrypts and decrypts data.

WARNING: You must have the cryptography module installed, if you don't this class won't do anything. Follow instructions down below for more information

## Usage

```py
import Functions
encryptClass = Functions.Encrypt()

# Get the key
key = encryptClass.GetKey("Hello".encode('utf-8'))

# Save data
encryptClass.encrypt("Hello World", key, fileName="Hello")

# read data
encryptClass.decrypt(key, fileNam="Hello")
```

Just three simple functions to encrypt and decrypt your data.

### Function and arguments

#### encrypt

```py
encryptClass.encrypt("Hello World", key, fileName="Hello")
```

This above function just encrypts the data `"Hello World"` (Which can be anything not just string) with the key and saves it under the fileName. You can then read the file all you want, but you won't be able to read the data as it's been ecrypted.

Required Arguments:

- Data: any (The data to encrypt and save)
- Key: bytes (The key to encrypt with)

Optional Arguments:

- fileName: str (The name of the file to save to)

#### decrypt

```py
encryptClass.decrypt(key, fileName="Hello")
```

This above function just decrypts data saved in fileName. If the key is not the same as the original key used to store the data, the data will still be decrypted but not in the correct way, causing errors in the data if you try to use it like you would normally use it.

Required Arguments:

- Key: bytes (The same key to decrypt with)

Optional Arguments:

- fileName: str (The name of the file to decrypt)

#### GetKey

```py
encryptClass.GetKey("Hello".encode('utf-8'))
```

This above function translates an encoded `utf-8` string into a better string for use in a key. This way you can use whatever key you would want to use. If this is left blank, then the program will automatically generate a passcode for you. If you loose this, you might not be able to get your data back.

Optional Arguments:

- key: str (Encoded `utf-8` custom made key)

## Module Requirements

This file is one of the small list of files that require other modules which i didn't make. As so, you will have to manually install them. Most of the time, i would import the package into the project myself, and just use a slightly older version however for encypting data it is easier (and keeps your data safer) if the latest version of the software gets used.

Don't worry though, if you don't have `cryptography` installed, this module won't break the whole program. Instead the class will just not respond to anything that yo send it. This has been done because i wanted to include it without having to force users to install external modules.

### Installation

`pip install cryptography`
This is all, and then just let python do the rest. If you don't want to install this globall make a virtual enviroment with `python -m virtualenv .env` and run command in their instead.

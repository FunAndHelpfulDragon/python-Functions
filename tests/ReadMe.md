# Tests

This folder contains all the automated tests that this program runs.

## Test List

A list of all tests and brief description

### Board_test.py

- test_size (Checks if the 2 input does actually give a good output)

### Check_test.py

- test_int (Checks if random input is valid)
- test_yes (Checks if input returns true)
- test_no (Checks if input returns false)
- test_error (Checks if the input asks again (or errors))

### Clean_test.py

- test_Clean (Checks if everything removes `__pycache__` and `Secret` files)
- test_Get (Checks if the result is equal to os.listdir)
- test_Remove (Checks if it successfully removes hidden files)
- test_Reserved (Checks if it successfully removes reserved files)

### Encryptiontest.py

- test_Key (Makes a key and checks if its a bytes string returned)
- test_Encrypt (Encrypts data and saves, also checks if the path exists)
- test_Decrypt_wrong (Tries to decrypt data with an invalid key)
- test_Decrypt_Correct (Tries to decrypt data with a valid key)
- test_CleanUp (Cleans up everything)

### IsDigit_test.py

all are run 10 times to check that it wasn't a one off error (just in case)

- test_isdigit (Tests if a float, is a digit)
- test_isdigit_str (Tests if a string is a float)
- test_notDigit (Tests if a string is not a float)

### run_test.py

- test_mark (Tests if when mark, will increase the list by one)
- test_get_mark (Tests if a mark out of range, errors and in range returns a float)
- test_compare (Tests if getting them from the list is the same as normally)

### Terminal_Display_test.py (Maybe rewrite)

- test_Set (Checks if the set function adds 3 items to the list)
- test_Add (Checks if the add function adds 2 items to the list)
- test_List (Input a random value and get the result)

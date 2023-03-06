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
- test_yes_return (Checks if the input returns to the yes function on `yes`)
- test_no_return (Checks if the input returns to the no function on `no`)
- test_str (Checks if the string is in a specified list)
- test_path (Checks if the path specified exists)
- test_callback (Checks if the callback function will run on result)

### Clean_test.py

- test_Clean (Checks if everything removes `__pycache__` and `Secret` files)
- test_Get (Checks if the result is equal to os.listdir)
- test_Remove (Checks if it successfully removes hidden files)
- test_Reserved (Checks if it successfully removes reserved files)
- test_Wild_Reserved (Checks if it can remove resered files with things like `*.txt`)

### Convert_test.py

- test_Convert (Repeated 3x) (Checks to see if it can convert a letter to the numbers)

### Encryptiontest.py

- test_Key (Makes a key and checks if its a bytes string returned)
- test_Encrypt (Encrypts data and saves, also checks if the path exists)
- test_Decrypt_wrong (Tries to decrypt data with an invalid key)
- test_Decrypt_Correct (Tries to decrypt data with a valid key)
- test_finish (Cleans up everything)

### IsDigit_test.py

all are run 10 times to check that it wasn't a one off error (just in case)

- test_isdigit (Tests if a float, is a digit)
- test_isdigit_str (Tests if a string is a float)
- test_notDigit (Tests if a string is not a float)

### Message_test.py

- test_writeSetup (Does nothing other than writes a file)
- test_message (Using Message, capture the output write the output and check the output)
- test_cleanup (Cleans up files that don't need to be here)

### run_test.py

- test_mark (Tests if when mark, will increase the list by one)
- test_get_mark (Tests if a mark out of range, errors and in range returns a float)
- test_compare (Tests if getting them from the list is the same as normally)
- test_wrapper (Tests to see if the wrapper functions works. (Not really sure it tests the wrapper function))

### Save_test.py

- test_MakeFolders (Makes folders and checks if they exists)
- test_write_Data_None (Writes data to a file with no encoding)
- test_write_Data_JSON (Writes data to a file with JSON encoding)
- test_write_Data_BINARY (Writes data to a file with BINARY encoding)
- test_write_Data_Crypto (Writes data to a file with Crypto encoding)
- test_write_Data_CSV (Writes data to a file with CSV encoding)
- test_Read_Data_None (Reads data from a file with no encoding)
- test_Read_Data_JSON (Reads data from a file with JSON encoding)
- test_Read_Data_BINARY (Reads data from a file with BINARY encoding)
- test_Read_Data_Crypto (Reads data from a file with Crypto encoding)
- test_Read_Data_CSV (Reads data from a file with CSV encoding)
- test_Remove_File_None (Removes the file with no encoding)
- test_Remove_File_JSON (Removes the file with JSON encoding)
- test_Remove_File_BIANRY (Removes the file with BINARY encoding)
- test_Remove_File_Crypto (Removes the file with Crypto encoding)
- test_Remove_File_CSV (Removes the file with no encoding)
- test_Remove_Folder (Removes the folder)
- test_Finish (Cleans up anything else)

### Searching_test.py

(All of these ignore certain files due to them making it take forever to search)

- test_find_watermark (Tries to find the `watermark.py` file)
- test_find_Multiple (Tries to find multiple files)

### Terminal_Display_test.py (Maybe rewrite)

- test_Set (Checks if the set function adds 3 items to the list)
- test_Add (Checks if the add function adds 2 items to the list)
- test_Remove (Checks to see if removing is possible)
- test_RemoveMore (Remove multiple options at once)
- test_RemoveAll (Remove all of the options)

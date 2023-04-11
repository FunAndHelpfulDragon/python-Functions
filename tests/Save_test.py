import os
import shutil

import pytest

from src.PythonFunctions.Save import save
sv = save()

csvData = {
    "header": ["name", "test"],
    "rows": [
        {"name": "save", "test": "Stuff to do with saving"},
        {"name": "Clean", "test": "Cleaning folders"},
    ],
}


@pytest.fixture(autouse=True)
def test_MakeFolder():
    sv.MakeFolders("TestSaveTemp")
    assert os.path.exists("TestSaveTemp")


def test_MakeFolders():
    sv.MakeFolders("TestSaveTemp/Test1/Test2")
    assert os.path.exists("TestSaveTemp/Test1/Test2")


def test_write_Data_None():
    """Test to write a normal file with no encoding correctly"""
    assert sv.Write("Hello World", "TestSaveTemp/Normal.txt",
                   encoding=sv.encoding.NONE)


def test_write_Data_JSON():
    """Test to write a json file correctly"""
    assert sv.Write(
        {"1": "Hi 2", "2": "Hi 3"}, "TestSaveTemp/JSON.json", encoding=sv.encoding.JSON
    )


def test_write_Data_BINARY():
    """Test to write data as binary using pickle correctly"""
    assert sv.Write("Hello World", "TestSaveTemp/Bin.bin",
                    encoding=sv.encoding.BINARY)


def test_Write_Data_Crypto():
    """Test to write data using cryptography correctly"""
    assert sv.Write("Hello World", "TestSaveTemp/Crypt.bin",
                    encoding=sv.encoding.CRYPTOGRAPHY)


def test_Save_Data_CSV():
    """Test to write csv data from a dictonary"""
    assert sv.Write(csvData, "TestSaveTemp/CSV.csv", encoding=sv.encoding.CSV)


def test_Read_Data_None():
    """Test to read normal file correctly"""
    assert sv.Read("TestSaveTemp/Normal.txt",
                   encoding=sv.encoding.NONE) == "Hello World"


def test_Read_Data_JSON():
    """Test to read json data correctly"""
    assert sv.Read("TestSaveTemp/JSON.json", encoding=sv.encoding.JSON) == {
        "1": "Hi 2",
        "2": "Hi 3",
    }


def test_Read_Data_BINARY():
    """Test to read binary data correctly"""
    assert sv.Read("TestSaveTemp/Bin.bin",
                   encoding=sv.encoding.BINARY) == "Hello World"


def test_Read_Data_Crypto():
    """Test to read data ussing cryptography correctly"""
    assert sv.Read("TestSaveTemp/Crypt.bin",
                   encoding=sv.encoding.CRYPTOGRAPHY) == "Hello World"


def test_Read_Data_CSV():
    assert sv.Read("TestSaveTemp/CSV.csv", encoding=sv.encoding.CSV)


def test_Remove_File_None():
    sv.RemoveFile("TestSaveTemp/Normal.txt")
    assert not os.path.exists("TestSaveTemp/Normal.txt")


def test_Remove_File_JSON():
    sv.RemoveFile("TestSaveTemp/JSON.json")
    assert not os.path.exists("TestSaveTemp/JSON.json")


def test_Remove_File_BINARY():
    sv.RemoveFile("TestSaveTemp/Bin.bin")
    assert not os.path.exists("TestSaveTempBin.bin")


def test_Remove_File_Crypto():
    sv.RemoveFile("TestSaveTemp/Crypt.bin")
    assert not os.path.exists("TestSaveTemp/Crypt.bin")


def test_Remove_File_CSV():
    sv.RemoveFile("TestSaveTemp/CSV.csv")
    assert not os.path.exists("TestSaveTemp/CSV.csv")


def test_Remove_Folder():
    sv.RemoveFolder("TestSaveTemp/Test1")
    assert not os.path.exists("TestSaveTemp/Test1/Test2")


# No automatic testing for FTP as no server to test with


def test_Finish():
    """Clean up after all the tests ends"""
    if os.path.exists("TestSaveTemp"):
        shutil.rmtree("TestSaveTemp")
    assert not os.path.exists("TestSaveTemp")

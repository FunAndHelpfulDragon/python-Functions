import os
import typing

class Clean:
    def __init__(self) -> None:
        """Cleans up the path and removes unnessecary files
        """
        pass

    def GetData(self, path: str) -> typing.List:
        """Returns the files stored in a given path

        Args:
            path (str): The path of files

        Returns:
            typing.List: The list found for that path
        """
        # If list, just use that instead
        if type(path) == typing.List:
            return path
        
        if path is None:
            return []
        
        try:
            return os.listdir(path)        
        except FileNotFoundError:
            return []
    
    def RemoveHidden(self, data: typing.List[str]) -> typing.List[str]:
        """Removes files and folders that start with `.` or `__`

        Args:
            data (typing.List[str]): The original file list

        Returns:
            typing.List[str]: The new list without hidden files
        """
        for folder in data:
            if folder.startswith(".") or folder.startswith("__"):
                data.pop(data.index(folder))
        
        return data
    
    def RemoveReserved(self, data: typing.List[str], reserved: typing.List[str]) -> typing.List[str]:
        """Remove any files that are resereved for other purposes that have not already been accounted for

        Args:
            data (typing.List[str]): The data for that path
            reserved (typing.List[str]): The resereved file list

        Returns:
            typing.List[str]: The new list with the removed files
        """
        for file in data:
            if file in reserved:
                data.pop(data.index(file))
        
        return data

    def clean(self, path:str, reserved: typing.List[str] = []) -> typing.List[str]:
        """Returns the finished product of cleaning up the path

        Args:
            path (str): The path to get the files from
            reserved (typing.List[str], optional): The list of data to not include in the final list. Defaults to [].

        Returns:
            typing.List[str]: The final data list
        """
        # Get data
        data = self.GetData(path)
        # Earily return
        if len(data) == 0:
            return data
        
        # Remove hidden
        data = self.RemoveHidden(data)
        
        if len(data) == 0:
            return data
        
        # Remove reserved files
        reserved.append("Desktop.ini")  # windows non hidden
        reserved.append("$RECYCLE.BIN") # windows non hidden
        
        data = self.RemoveReserved(data, reserved)
        return data

if __name__ == "__main__":
    clean = Clean()
    data = clean.clean(".")
    print(data)
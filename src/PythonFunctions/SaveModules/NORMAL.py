import os
import shutil

from . import template


class Save(template.SaveTemplate):
    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        print(path)
        if Encoding:
            with open(path, "wb") as f:
                return f.write(data) == len(data)

        with open(path, "w+", encoding="utf-8") as f:
            return f.write(data) == len(data)

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        if not os.path.exists(path):
            return False

        if Encoding:
            with open(path, "rb") as f:
                return f.read()

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def MakeFolders(self, path: str):
        if not os.path.exists(path) and path not in ("", None):
            os.makedirs(path)

    def DeleteFile(self, path: str):
        if os.path.exists(path):
            os.remove(path)

    def DeleteFolder(self, path: str):
        if os.path.exists(path):
            shutil.rmtree(path)

    def ListFolder(self, path: str):
        return os.listdir(path)

    def CheckIfExists(self, path: str):
        return os.path.exists(path)


def load():
    return Save()

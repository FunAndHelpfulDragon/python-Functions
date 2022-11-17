import getpass
import importlib
import json
import os
import pickle
import typing
from enum import Enum

from . import Clean, Encryption, Message, PrintTraceback, SaveModules
from .SaveModules import template


class Encoding(Enum):
    # Encoding enum class
    NONE = 1
    JSON = 2
    BINARY = 3
    CRYPTOGRAPHY = 4


class Storage(Enum):
    # Storage enum class
    NORMAL = 1
    FTP = 2
    GOOGLE = 3
    OTHER = 4


class save:
    """Save data, supports multiple systems.

    Supported Systems: [File]
    Planning Support for: [FTP, Google]
    """

    def __init__(self) -> None:
        """Loading the class, storing data such as enum, modules, settings"""
        self.encoding: Encoding = Enum(
            "Encoding", ["NONE", "JSON", "BINARY", "CRYPTOGRAPHY"]
        )
        self.storage: Storage = Enum("Storage", ["NORMAL", "FTP", "GOOGLE", "OTHER"])
        self.saveModules = {}
        self.settings = {
            "FTP": {"Name": "", "Password": ""},
            "SettingsSave": "",
            "Passcode": "",
        }

        self.__LoadModules()
        self.enc = Encryption()
        self.__CheckData()

    def __LoadModules(self):
        """Loading external save modules in."""

        # Loop through the clean list of modules
        # clean -> removes .* and template.py due to reserved
        for module in Clean().clean(
            os.path.dirname(SaveModules.__file__), reserved=["template.py"]
        ):
            module = module[:-3]  # remove .py

            # Attempt to load the module
            try:
                mdl = importlib.import_module(f"{SaveModules.__package__}.{module}")
                self.saveModules[module]: template.SaveTemplate = mdl.load()
            except (AttributeError, ModuleNotFoundError) as e:
                Message.warn(
                    f"Failed to load save module: {SaveModules.__package__}.{module}. Error: {e}",
                    colour=["Red"],
                )
                PrintTraceback()

    def __CheckData(self) -> None:
        """Check if the required data exists"""

        # File checker
        parent = os.path.dirname(__file__)
        if not os.path.exists(f"{parent}/PyFuncSave"):
            os.mkdir(f"{parent}/PyFuncSave")

        # Setting checker
        if not os.path.exists(f"{parent}/PyFuncSave/Settings.secret"):
            self.settings["SettingsSave"] = f"{parent}/PyFuncSave/Settings.secret"

            # Save if not exists
            self.Save(
                self.settings,
                self.settings.get("SettingsSave"),
                [self.encoding.JSON, self.encoding.BINARY],
            )
        else:
            # Load settings otherwise
            self.settings = self.Read(
                f"{parent}/PyFuncSave/Settings.secret",
                [self.encoding.JSON, self.encoding.BINARY],
            )

    def __TranslateStorage(self, path: str):
        """Takes the path and returns the storage type

        Args:
            path (str): The path to save at

        Returns:
            (str, Storage): New path, The storage type
        """
        if path.startswith("ftp://"):
            return path.removeprefix("ftp://"), self.storage.FTP

        if path.startswith("gdr://"):
            return path.removeprefix("gdr://"), self.storage.GOOGLE

        if path.startswith("oth://"):
            return path.removeprefix("oth://"), self.storage.OTHER

        return path, self.storage.NORMAL

    def __CodeData(
        self, data: any, encoding: typing.List[Encoding], *, decode: bool = False
    ):
        """Encode / Decode data

        Args:
            data (any): The data to encode / decode
            encoding (typing.List[Encoding]): The way to do it. (Which order, multi layered)
            decode (bool, optional): TO decode instead of encode. Defaults to False.

        Returns:
            any, bool: The data and whever it has been affected by byte arguments
        """
        result = data
        rBytes = False

        for code in encoding:
            if code.value == 1:
                # DO nothing
                continue

            if code.value == 2:
                # simple json encode
                result = json.dumps(result) if not decode else json.loads(result)
                continue

            if code.value == 3:
                # simple byte encode
                result = pickle.dumps(result) if not decode else pickle.loads(result)
                rBytes = True

            if code.value == 4:
                Passcode = self.settings.get("Passcode")

                # Get passcode if not exists
                if Passcode is None or Passcode == "":
                    Passcode = getpass.getpass(
                        "Please enter a password / passcode to save encrypted data with: "
                    )

                    key = self.enc.GetKey(
                        Passcode.encode("utf-8")
                    )  # get the byte version
                    self.settings["Passcode"] = key.decode(
                        "utf-8"
                    )  # store the byte as string

                    # save the data
                    self.Save(
                        self.settings,
                        self.settings.get("SettingsSave"),
                        [self.encoding.JSON, self.encoding.BINARY],
                    )

                # decrypt / encrypt data
                key = Passcode.encode("utf-8")

                if not decode:
                    result = self.enc.EncryptData(result, key)
                else:
                    result = self.enc.DecryptData(result, key)

                rBytes = True

        return result, rBytes

    def __GetFileInformation(
        self, path: str, encoding: typing.List = None
    ) -> typing.Tuple[str, Storage, typing.List]:
        if encoding is None:
            encoding = [self.encoding.NONE]

        if not isinstance(encoding, typing.List):
            encoding = [encoding]

        path, storage = self.__TranslateStorage(path)

        self.MakeFolders(os.path.dirname(path), storage=storage)

        return path, storage, encoding

    def Save(self, data: any, path: str, encoding: typing.List = None) -> bool:
        """Save data to the designated file system.

        Args:
            data (any): The data to save
            path (str): The path to save to (Read documentation for other systems)
            encoding (typing.List, optional): The encoding to save with. Defaults to None.

        Returns:
            bool: Whever it saves correctly or not
        """
        path, storage, encoding = self.__GetFileInformation(path, encoding)

        data, wByte = self.__CodeData(data, encoding)

        module: template.SaveTemplate = self.saveModules.get(storage.name)
        return module.WriteData(data, path, wByte)

    def Read(self, path: str, encoding: typing.List = None) -> any:
        """Read data from a file

        Args:
            path (str): The path to read from
            encoding (typing.List, optional): The encoding to go under to read it. Defaults to None.

        Returns:
            any: The data in the file
        """
        path, storage, encoding = self.__GetFileInformation(path, encoding)
        module: template.SaveTemplate = self.saveModules.get(storage.name)

        rBytes = False
        for item in encoding:
            if item == self.encoding.BINARY:
                rBytes = True

            if item == self.encoding.CRYPTOGRAPHY:
                rBytes = True

        data = module.ReadData(path, rBytes)
        data, _ = self.__CodeData(data, reversed(encoding), decode=True)

        return data

    def MakeFolders(self, path: str, **data):
        """Make X folders at the path if they do not exist already.
        Automatic if folders do not exist already

        Args:
            path (str): The path to make folders
        """
        storage = data.get("storage")
        if storage is None:
            path, storage = self.__TranslateStorage(path)

        module: template.SaveTemplate = self.saveModules.get(storage.name)
        module.MakeFolders(path)

    def RemoveFile(self, path: str):
        """Remove a file at a path

        Args:
            path (str): The path to remove that file
        """
        path, storage = self.__TranslateStorage(path)
        module: template.SaveTemplate = self.saveModules.get(storage.name)
        module.DeleteFile(path)

    def RemoveFolder(self, path: str):
        """Remove a folder (and all sub stuff)

        Args:
            path (str): The path to remove the folder
        """
        path, storage = self.__TranslateStorage(path)
        module: template.SaveTemplate = self.saveModules.get(storage.name)
        module.DeleteFolder(path)

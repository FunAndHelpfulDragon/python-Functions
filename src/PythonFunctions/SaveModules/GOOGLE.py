import os
import sys
from . import template

disabled = False

try:
    from google.auth.transport.requests import Request
    from google.auth.exceptions import RefreshError
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
except ModuleNotFoundError:
    disabled = True
    # pylint:disable=C0301
    print("NOTE: google drive api is NOT INSTALLED. As so, communicating with google drive api is DISABLED!!")
    # pylint:enable=C0301


class save(template.SaveTemplate):
    def __init__(self) -> None:
        super().__init__()
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.service = None
        self.pageSize = 0

    def credentials(self, data):
        self.pageSize = data.get("gPage")
        super().credentials(data)
        self.service = self.__LoadGoogle()

    def __LoadGoogle(self):
        if disabled:
            return False

        path = self.data.get("SettingsSave")
        path = os.path.dirname(path)
        Tpath = path + "/gToken.json"
        Cpath = path + "/gCred.json"

        if not os.path.exists(Cpath):
            sys.exit(f"Please make sure the file: {Cpath} exists!")

        try:
            creds = None
            if os.path.exists(Tpath):
                creds = Credentials.from_authorized_user_file(
                    Tpath, self.SCOPES)

            # If there are no (valid) credentials available, let the user login
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        Cpath, self.SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save the credentials for the next run
                with open(Tpath, 'w', encoding='utf-8') as token:
                    token.write(creds.to_json())

            print("Drive API loaded!")
            return build('drive', 'v3', credentials=creds)
        except KeyboardInterrupt:
            sys.exit('Bad drive... Please restart the program and try again.')
        except RefreshError:
            if os.path.exists(Tpath):
                os.system(f'rm {Tpath}')

                # Check if files are actually there and not missing due to folder creation.
                if not os.path.exists(Cpath):
                    sys.exit(f'{Cpath} has not been found!')
            return self.__LoadGoogle()

    def __ListDirectory(self, folder='.'):
        """Loop through the path to get all the items

        Args:
            folder (string): The path to check

        Returns:
            List: List of all the items
        """
        if disabled:
            return False

        import ipdb
        ipdb.set_trace()
        query = "trashed = false"

        if folder != "":
            query += f"'{folder}' in parents"

        try:
            files = []
            page_token = None
            while True:
                response = self.service.files().list(q=query,
                                                     spaces='drive',
                                                     fields='nextPageToken, '
                                                     'files(id, name)',
                                                     pageToken=page_token).execute()
                for file in response.get('files', []):
                    # Process change
                    print(F'Found file: {file.get("name")}, {file.get("id")}')
                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break
        except HttpError as error:
            print(F'An error occurred: {error}')
            files = None

        return files

    def __checkIfExists(self, folder, name):
        """Check if an item with a certain name already exists

        Args:
            folder (string): Folder to search through
            name (string): name of the file to search for

        Returns:
            Bool: Does it exists
            item: The id of the item if it exists
        """
        if disabled:
            return False

        print({'folder': folder})
        items = self.__ListDirectory(folder)
        if items is not None:
            for item in items:
                if item['name'] == name:
                    return True, item
        return False, None

    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        if disabled:
            return False

        pathInfo = os.path.split(path)

        if not isinstance(data, bytes):
            data = data.encode('utf-8')

        with open(self.tempFile, "wb") as f:
            f.write(data)

        exists, exId = self.__checkIfExists(pathInfo[0], pathInfo[1])
        if exists:
            self.__DeleteByID(exId)

        metadata = {
            'name': pathInfo[1],
            'mimeType': '*/*',
            'parents': pathInfo[0]
        }

        media = MediaFileUpload(self.tempFile,
                                mimetype='*/*',
                                resumable=True)

        id = self.service.files().create(body=metadata,
                                         media_body=media,
                                         fields='id').execute()

        return id

    def MakeFolders(self, path: str):
        if disabled:
            return False
        return

    def DeleteFile(self, path: str):
        if disabled:
            return False

        return super().DeleteFile(path)

    def __DeleteByID(self, id):
        if disabled:
            return False

        try:
            self.service.files().delete(fileId=id).execute()
            return "Deleted"
        except HttpError:
            return "Not found"


def load():
    return save()

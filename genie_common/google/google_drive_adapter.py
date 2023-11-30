import json
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from genie_common.google.google_consts import SERVICE_ACCOUNT_SECRETS_PATH, GOOGLE_SERVICE_ACCOUNT_CREDENTIALS
from genie_common.models.google import GoogleDriveDownloadMetadata, GoogleDriveUploadMetadata


class GoogleDriveAdapter:
    def __init__(self, drive_service: Resource):
        self._drive_service = drive_service

    @classmethod
    def create(cls) -> "GoogleDriveAdapter":
        drive_service = build(
            serviceName='drive',
            version='v3',
            credentials=cls._build_credentials()
        )
        return cls(drive_service)

    def download(self, *file_metadata: GoogleDriveDownloadMetadata) -> None:
        for file in file_metadata:
            file_content = self._drive_service.files().get_media(fileId=file.file_id).execute()

            with open(file.local_path, 'wb') as f:
                f.write(file_content)

            print(f'Successfully downloaded file to {file.local_path}')

    def upload(self, *file_metadata: GoogleDriveUploadMetadata) -> None:
        for file in file_metadata:
            media = MediaFileUpload(file.local_path, resumable=True)

            try:
                file = self._drive_service.files().create(body=file.metadata, media_body=media, fields='id').execute()
                print(f'File ID: {file.get("id")} uploaded successfully')
            except HttpError as error:
                print(f'An error occurred: {error}')
            finally:
                media.stream().close()

    def clean_folder(self, folder_id: str) -> None:
        query = f"'{folder_id}' in parents and trashed=false"
        results = self._drive_service.files().list(q=query).execute()
        files = results.get('files', [])

        for file in files:
            self._drive_service.files().delete(fileId=file['id']).execute()

        print(f"All folder `{folder_id}` contents deleted successfully!")

    @staticmethod
    def _build_credentials() -> Credentials:
        if os.path.exists(SERVICE_ACCOUNT_SECRETS_PATH):
            return Credentials.from_service_account_file(SERVICE_ACCOUNT_SECRETS_PATH)

        elif GOOGLE_SERVICE_ACCOUNT_CREDENTIALS in os.environ.keys():
            credentials = json.loads(os.environ[GOOGLE_SERVICE_ACCOUNT_CREDENTIALS])
            return Credentials.from_service_account_info(credentials)

        else:
            raise ValueError('Missing Google service account credentials')

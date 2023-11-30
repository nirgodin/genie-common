from dataclasses import dataclass


@dataclass
class GoogleDriveUploadMetadata:
    local_path: str
    drive_folder_id: str
    file_name: str

    def __post_init__(self):
        self.metadata = {
            'name': self.file_name,
            'parents': [self.drive_folder_id]
        }

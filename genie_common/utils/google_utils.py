import json
import os
from typing import Dict, Optional

from genie_common.consts import SERVICE_ACCOUNT_SECRETS_PATH, GOOGLE_SERVICE_ACCOUNT_CREDENTIALS


def load_google_service_account_info() -> Dict[str, str]:
    if os.path.exists(SERVICE_ACCOUNT_SECRETS_PATH):
        with open(SERVICE_ACCOUNT_SECRETS_PATH, "r") as f:
            return json.load(f)

    elif GOOGLE_SERVICE_ACCOUNT_CREDENTIALS in os.environ.keys():
        return json.loads(os.environ[GOOGLE_SERVICE_ACCOUNT_CREDENTIALS])

    else:
        raise ValueError('Missing Google service account credentials')


def get_google_project_id(service_account_info: Optional[Dict[str, str]] = None) -> str:
    info = service_account_info or load_google_service_account_info()
    return info["project_id"]
    # project_name, project_id = project_identifier.split("-")
    #
    # return project_id

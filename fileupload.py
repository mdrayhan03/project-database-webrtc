import os
import mimetypes
import io
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Configuration
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "file.json"  # The local file name
FOLDER_ID = "1nqe5SODYtE74ZleS0wGfgCrs8rD4zuag"  # Optional: leave None to upload to root

# Authenticate using file if exists, else use env variable
creds = None
try:
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        print("Authenticated using local JSON file.")
    else:
        google_creds = os.getenv("GOOGLE_CREDENTIALS")
        if google_creds is None:
            raise Exception("No credentials file or environment variable found.")
        google_creds_json = json.loads(google_creds)
        creds = Credentials.from_service_account_info(google_creds_json, scopes=SCOPES)
        print("Authenticated using environment variable.")
except Exception as e:
    print(f"Error in authentication: {str(e)}")
    raise

# Build Google Drive service
drive_service = build("drive", "v3", credentials=creds)

def upload_to_drive(uploaded_file):
    print(type(uploaded_file))
    # Extract filename and detect MIME type
    file_name = uploaded_file.name
    mime_type = uploaded_file.content_type or mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
    print(file_name, mime_type)

    # File metadata
    file_metadata = {"name": file_name}
    if FOLDER_ID:
        file_metadata["parents"] = [FOLDER_ID]
    print(file_metadata)

    # Media upload
    media = MediaIoBaseUpload(uploaded_file, mimetype=mime_type)
    print("Media: ", media)

    # Upload
    try:
        upload_file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id, name, mimeType"
        ).execute()
        print("Uploaded: ", upload_file)
        download_link = f"https://drive.google.com/uc?id={upload_file['id']}&export=download"
        return download_link
    except Exception as e:
        print("Error uploading file: ", str(e))
        return None
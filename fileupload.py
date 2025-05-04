import os
import mimetypes
import io
import json
import base64
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Configuration
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "file.json"
FOLDER_ID = "1nqe5SODYtE74ZleS0wGfgCrs8rD4zuag"  # Optional: leave None to upload to root

# Authenticate using local file or env
creds = None
try:
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        print("✅ Authenticated using local JSON file.")
    else:
        google_creds_b64 = os.getenv("GOOGLE_CREDENTIALS_B64")
        if not google_creds_b64:
            raise Exception("No credentials file or GOOGLE_CREDENTIALS_B64 environment variable found.")
        # Decode base64 to JSON
        decoded_json = base64.b64decode(google_creds_b64).decode("utf-8")
        google_creds_json = json.loads(decoded_json)
        creds = Credentials.from_service_account_info(google_creds_json, scopes=SCOPES)
        print("✅ Authenticated using base64 credentials from environment.")
except Exception as e:
    print(f"❌ Error in authentication: {str(e)}")
    raise

# Build Drive service
drive_service = build("drive", "v3", credentials=creds)

def upload_to_drive(uploaded_file):
    print(type(uploaded_file))
    file_name = uploaded_file.name
    mime_type = uploaded_file.content_type or mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
    print(file_name, mime_type)

    file_metadata = {"name": file_name}
    if FOLDER_ID:
        file_metadata["parents"] = [FOLDER_ID]
    print(file_metadata)

    media = MediaIoBaseUpload(uploaded_file, mimetype=mime_type)
    print("Media: ", media)

    try:
        upload_file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id, name, mimeType"
        ).execute()
        print("✅ Uploaded: ", upload_file)
        download_link = f"https://drive.google.com/uc?id={upload_file['id']}&export=download"
        return download_link
    except Exception as e:
        print("❌ Error uploading file: ", str(e))
        return None
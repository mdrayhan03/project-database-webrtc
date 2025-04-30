# sl.u.AFuCm9MjagOJqWJ_pno-nUJ52FneP2hKHjkyFrKcfrN-X1AbevEo1BPVFrKV3zbdMlrwScVLcns1v4S7lQjus-9kKHEGFK17_59DCaedHs3bRoGvkmzaPuthllNgVgxwLDKtefXl7wtEmdfJGesJwGHzaJlh5-tpxyVRIwNu8J0mglrXCxGcZ2KLXNopHmytB_3zPXCzFagypmBkDIRDVsTf6wCKDn0dV9r1kHvtn54PCy2rt4Za2uBD5syYmijkvhK7d-QrRmj7IJjSka0E9Vw1MdWYrbdo1Ui46Du5pl2Xo3Y35iRsUyLTSgySohKeOLims01RC1jn6Sz6vklNdYu9VpZF3-x418_-k3ADAheScZTiqeJUKmtHTqzvvKnWGwwGFtEbd14PUbYBPchHRpjdyrXrnhvGuQRN5DqqSQ9tOz2cvvdz99gHHpSk33iLC6a9IHYCSvALjdpLrIQSwDWy_2dGr5J4PF5EMNw74ooJzAU4K0mEW5jg1q89gFeYkWm2GinZsXWLD1DYrGV-2N9NuYDu3AE5z7ZB0f5IDtDbpsZ3Q8VsswpRzb7jOj5Y9JhK1qaSMAva3AigdfjiAP-eS0OSG6qOfM32Zwp1ut9Foml7mt53sWxS12GBm2wVMUpYhaMuiQrt2oxh24uTpzi4mJ_54isT8fwxnANWeNINeZqaP8lOkF5o8rd6puJeKahNrE9-mXmzU9gcjHDvvm_nK5FMraLAhGe9EZVYt1Qqu9m3yRrL5fv40fHm5rN_qLaVEyoFZCNqTnsdxtTB6rNMvL7IjsK5xjju7YNqB1hfxzFmws2UuMw77Z7Lk1OxyFF-WZTkp2ciRjYOQ5rTqQEjTSQe8HCGFUyynHxYutDc2NMrU6kb0IFkOLoPdmvt5nVgua0dksC7pGXMWWWjT-NQT67fmy0A2TuDoXRfhyRh1sbD_EQLcAsxgWqtBiDypbI4T3g2YAGAIhNU8H0uUjdaN2uYP5rJUFyiXwKPm2cPB7Gd_80WymEu2LhjBN3lvLB6QA88_YkIne4sGsYc2zcjIeT5uOu-CfsDxpZXxurwKQmb94R1THGpEUGTHwqlZo-zVTujtUxFbbNtZPlCFxs_qqM5l8aPhPj2t5USf8hdE4pkexG7qczxRw7p9J3ch8B-Odtylo0R-06RRoV7uygcNAU1EfK6dKiCjH8VeNV7W8Niddrj_kNT0fTMdqj2KLSi36pFD7MHjQwrdxZa21rXT33XUael0k5kR9L6Gfv-TsDxo_emHSwz8EYtzBIoAJ31-UKf_ynX62onIddtgR5dNJ5dXo1bog6Hr-YKcDjN9Q8iLfSaoLzYfcgIVs3mD9LUcyBjiMQ7TtemItMbU-yduAj8X961zLyD8uJ9M1Pi3Fe4LYIb59yr3Fx2NO8Bg94RPvB044UWS4Rn-kA0NR7PnlGfrPtQcSm4bTP-XOjPar3N6TFKEtD8Lcnm1RPz8s2vXiod94cDDLSN7WnLLoLjIoGnxYzrHRNBJG62UOpzzA

# import dropbox

# # Your Dropbox access token (get this from the Dropbox App Console)
# ACCESS_TOKEN = 'sl.u.AFuCm9MjagOJqWJ_pno-nUJ52FneP2hKHjkyFrKcfrN-X1AbevEo1BPVFrKV3zbdMlrwScVLcns1v4S7lQjus-9kKHEGFK17_59DCaedHs3bRoGvkmzaPuthllNgVgxwLDKtefXl7wtEmdfJGesJwGHzaJlh5-tpxyVRIwNu8J0mglrXCxGcZ2KLXNopHmytB_3zPXCzFagypmBkDIRDVsTf6wCKDn0dV9r1kHvtn54PCy2rt4Za2uBD5syYmijkvhK7d-QrRmj7IJjSka0E9Vw1MdWYrbdo1Ui46Du5pl2Xo3Y35iRsUyLTSgySohKeOLims01RC1jn6Sz6vklNdYu9VpZF3-x418_-k3ADAheScZTiqeJUKmtHTqzvvKnWGwwGFtEbd14PUbYBPchHRpjdyrXrnhvGuQRN5DqqSQ9tOz2cvvdz99gHHpSk33iLC6a9IHYCSvALjdpLrIQSwDWy_2dGr5J4PF5EMNw74ooJzAU4K0mEW5jg1q89gFeYkWm2GinZsXWLD1DYrGV-2N9NuYDu3AE5z7ZB0f5IDtDbpsZ3Q8VsswpRzb7jOj5Y9JhK1qaSMAva3AigdfjiAP-eS0OSG6qOfM32Zwp1ut9Foml7mt53sWxS12GBm2wVMUpYhaMuiQrt2oxh24uTpzi4mJ_54isT8fwxnANWeNINeZqaP8lOkF5o8rd6puJeKahNrE9-mXmzU9gcjHDvvm_nK5FMraLAhGe9EZVYt1Qqu9m3yRrL5fv40fHm5rN_qLaVEyoFZCNqTnsdxtTB6rNMvL7IjsK5xjju7YNqB1hfxzFmws2UuMw77Z7Lk1OxyFF-WZTkp2ciRjYOQ5rTqQEjTSQe8HCGFUyynHxYutDc2NMrU6kb0IFkOLoPdmvt5nVgua0dksC7pGXMWWWjT-NQT67fmy0A2TuDoXRfhyRh1sbD_EQLcAsxgWqtBiDypbI4T3g2YAGAIhNU8H0uUjdaN2uYP5rJUFyiXwKPm2cPB7Gd_80WymEu2LhjBN3lvLB6QA88_YkIne4sGsYc2zcjIeT5uOu-CfsDxpZXxurwKQmb94R1THGpEUGTHwqlZo-zVTujtUxFbbNtZPlCFxs_qqM5l8aPhPj2t5USf8hdE4pkexG7qczxRw7p9J3ch8B-Odtylo0R-06RRoV7uygcNAU1EfK6dKiCjH8VeNV7W8Niddrj_kNT0fTMdqj2KLSi36pFD7MHjQwrdxZa21rXT33XUael0k5kR9L6Gfv-TsDxo_emHSwz8EYtzBIoAJ31-UKf_ynX62onIddtgR5dNJ5dXo1bog6Hr-YKcDjN9Q8iLfSaoLzYfcgIVs3mD9LUcyBjiMQ7TtemItMbU-yduAj8X961zLyD8uJ9M1Pi3Fe4LYIb59yr3Fx2NO8Bg94RPvB044UWS4Rn-kA0NR7PnlGfrPtQcSm4bTP-XOjPar3N6TFKEtD8Lcnm1RPz8s2vXiod94cDDLSN7WnLLoLjIoGnxYzrHRNBJG62UOpzzA'

# def upload_file_to_dropbox(uploaded_file):
#     print("Step 2")
#     # Connect to Dropbox
#     dbx = dropbox.Dropbox(ACCESS_TOKEN)
    
#     if uploaded_file :
#         print("Step 3")
#         file_data = uploaded_file.read()
#         file_name = uploaded_file.filename

#         dropbox_path = f"/{file_name}"

#         # Upload to Dropbox
#         dbx.files_upload(file_data, dropbox_path, mode=dropbox.files.WriteMode.overwrite)
#         print("Successfull")
#     else :
#         print("Unsuccessful")

# def get_dropbox_download_link(uploaded_file):
#     dbx = dropbox.Dropbox(ACCESS_TOKEN)
#     print("Step 4")
#     file_path = f"/{uploaded_file.filename}"

#     # Create a shared link (or reuse existing one)
#     try:
#         print("Step 5")
#         link_metadata = dbx.sharing_create_shared_link_with_settings(file_path)
#     except dropbox.exceptions.ApiError as e:
#         # If link already exists, fetch it
#         if e.error.is_shared_link_already_exists():
#             link_metadata = dbx.sharing_list_shared_links(path=file_path).links[0]
#         else:
#             raise

#     # Force direct download
#     download_url = link_metadata.url.replace('?dl=0', '?dl=1')
#     print("Step 6: " , download_url)
#     return download_url


import mimetypes
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Configuration
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "file.json"
FOLDER_ID = "1nqe5SODYtE74ZleS0wGfgCrs8rD4zuag"  # Optional: leave None to upload to root

# Authenticate
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build("drive", "v3", credentials=creds)

def upload_to_drive(uploaded_file):
    # Extract filename and detect MIME type    
    file_name = uploaded_file.name
    mime_type = uploaded_file.content_type or mimetypes.guess_type(file_name)[0] or 'application/octet-stream'

    # File metadata
    file_metadata = {"name": file_name}
    file_metadata["parents"] = [FOLDER_ID]

    # Media upload
    media = MediaIoBaseUpload(uploaded_file, mimetype=mime_type)

    # Upload
    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, name, mimeType"
    ).execute()

    download_link = f"https://drive.google.com/uc?id={uploaded_file['id']}&export=download"
    return download_link

from pymongo import MongoClient
from pymongo.errors import *
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime

class Database:
    def __init__(self):
        client = MongoClient("mongodb+srv://mdrayhan03:mongodbrayhan03@practice.j8okl.mongodb.net/?retryWrites=true&w=majority&appName=Practice")  # Replace with your MongoDB URI if needed
        db = client["Video_Chat_DB"]
        self.user_col = db["User_Col"]
        self.meeting_col = db["Meeting_Col"]
        self.history_col = db["History_Col"]
        self.upload_col = db["Upload_Col"]

    def insert_new_user(self, name, email, password) :
        data = {
            "name" : name,
            "email" : email,
            "password" : password,
            "photo" : "None",
            "type" : 3, # type 1 == superadmin 2 == admin 3 == user
            "status" : 2,   # status 1 == active 2 == inactive 0 == deleted
        }
        try:
            response = self.user_col.insert_one(data)
            if response.inserted_id:
                print(f"Document inserted successfully with ID: {response.inserted_id}")
            else:
                print("Insertion failed: No inserted ID returned.")
        except PyMongoError as e:
            print(f"An error occurred: {e}")

    def insert_new_meeting(self, adminID, maxTime, maxMember) :
        data = {
            "adminID" : adminID ,
            "startTime" : datetime.now().strftime("%H:%M:%S") ,
            "maxTime" : maxTime ,
            "maxMember" : maxMember ,
            "currentMember" : 0, 
            "status" : 1 # status 1 == running 0 == end
        }

        try:
            response = self.meeting_col.insert_one(data)
            if response.inserted_id:
                print(f"Document inserted successfully with ID: {response.inserted_id}")
                return response.inserted_id
            else:
                print("Insertion failed: No inserted ID returned.")
        except PyMongoError as e:
            print(f"An error occurred: {e}")
    
    # def update_meeting_member(self, meetingID) :
    #     try :
    #         response = self.history_col.find_one({"_id" : ObjectId})
    #         if response.inserted_id:
    #             print(f"Document inserted successfully with ID: {response.inserted_id}")
    #         else:
    #             print("Insertion failed: No inserted ID returned.")
    #     except PyMongoError as e:
    #         print(f"An error occurred: {e}")

    def insert_new_history(self, meetingID, userID, type) :
        data = {
            "meetingID" : meetingID ,
            "userID" : userID ,
            "startTime" : datetime.now().strftime("%H:%M:%S") ,
            "type" : type # type 1 == meeting creator 2 == member
        }

        try:
            response = self.history_col.insert_one(data)
            if response.inserted_id:
                print(f"Document inserted successfully with ID: {response.inserted_id}")
            else:
                print("Insertion failed: No inserted ID returned.")
        except PyMongoError as e:
            print(f"An error occurred: {e}")

    def find_login_user(self, email, password) :
        condition = {
            "email" : email,
            "password" : password
        }
        try:
            response = self.user_col.find_one_and_update(condition, {"$set" : {"status" : 1}}, return_document=True)
            response["_id"] = str(response["_id"])
            if response is None:
                print("No user found")
                return None
            else:       
                response["_id"] = str(response["_id"])         
                return response
        except PyMongoError as e:
            print(f"An error occurred: {e}")

    def find_logout_user(self, id) :
        condition = {
            "_id" : ObjectId(id)
        }
        try:
            response = self.user_col.find_one_and_update(condition, {"$set" : {"status" : 2}}, return_document=True)
            response["_id"] = str(response["_id"])
            if response is None:
                print("No user found")
                return None
            else:       
                response["_id"] = str(response["_id"])         
                return response
        except PyMongoError as e:
            print(f"An error occurred: {e}")
    
    def update_user_info(self, id, name, email):
        try:
            condition = {"_id": ObjectId(id)}
            update = {"$set": {"name": name, "email": email}}

            updated_user = self.user_col.find_one_and_update(
                condition, 
                update, 
                return_document=True
            )

            if updated_user is None:
                print("No user found")
                return None

            updated_user["_id"] = str(updated_user["_id"])
            print("User updated successfully:", updated_user)
            
            return updated_user
        
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return None
    
    def find_existing_meeting(self, id) :
        try:
            id = ObjectId(id)
        except InvalidId:
            return None
        
        try:
            response = self.meeting_col.find_one({"_id" : ObjectId(id)})            
            if response is None:
                print("No meeting found")
                return None
            else:       
                if response["status"] == 1 :
                    return response
                else :
                    print("None")
                    return None
        except PyMongoError as e:
            print(f"An error occurred: {e}")

    def get_created_meetings(self, user_id):
        meetings = self.meeting_col.find({"adminID": str(user_id)})
        created = []
        for m in meetings:
            created.append({
                "meeting_id": str(m["_id"]),
                "start_time": m.get("startTime", "N/A"),
                "status": "Running" if m.get("status") == 1 else "Ended",
            })
        return created

    # Get joined meetings by the logged-in user
    def get_joined_meetings(self, user_id):
        joined_histories = self.history_col.find({"userID": str(user_id)})
        joined = []
        for h in joined_histories:
            meeting = self.meeting_col.find_one({"_id": h["meetingID"]})
            if meeting:
                joined.append({
                    "meeting_id": h["meetingID"],
                    "creator_id": meeting.get("adminID", "N/A"),
                    "start_time": meeting.get("startTime", "N/A"),
                    "join_time": h.get("startTime", "N/A"),
                })
        return joined
    
    def insert_new_upload(self, meeting_id, sender_id, file_name, file_type, file_url):
        upload_data = {
            "meetingID": str(meeting_id),
            "senderID": str(sender_id),
            "fileName" : file_name,
            "fileType": file_type,
            "fileURL": file_url,
            "sendTime": datetime.now().strftime("%H:%M:%S")
        }
        try:
            response = self.upload_col.insert_one(upload_data)
            if response.inserted_id:
                print(f"Upload inserted successfully with ID: {response.inserted_id}")
                return response.inserted_id
            else:
                print("Upload insertion failed: No inserted ID returned.")
        except PyMongoError as e:
            print(f"An error occurred during upload insertion: {e}")
    
    def get_uploads_by_meeting(self, meeting_id):
        try:
            uploads = list(self.upload_col.find({"meetingID": str(meeting_id)}))
            for upload in uploads:
                upload["_id"] = str(upload["_id"])  # Optional: convert ObjectID to string
            return uploads
        except PyMongoError as e:
            print(f"An error occurred while fetching uploads: {e}")
            return []
    
    def get_uploads_by_sender(self, sender_id):
        try:
            uploads = list(self.upload_col.find({"senderID": str(sender_id)}))
            for upload in uploads:
                upload["_id"] = str(upload["_id"])  # Optional: convert ObjectID to string
            return uploads
        except PyMongoError as e:
            print(f"An error occurred while fetching uploads by sender: {e}")
            return []



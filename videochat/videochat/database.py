from django.db import connection

def create_user_tb() :
    with connection.cursor() as cursor :
        cursor.execute("""
            CREATE TABLE user_tb(
                username VARCHAR(50) PRIMARY KEY UNIQUE,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                email VARCHAR(100) UNIQUE,
                phoneno VARCHAR(20),
                dob DATE,
                password VARCHAR(50),
                status INT,
            )
        """)
    
def create_room_tb() :
    with connection.cursor() as cursor :
        cursor.execute("""
            CREATE TABLE room_tb(
                roomid INT PRIMARY KEY,
                meeting_time INT,
                max_participant INT,
                current_participant INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                admin_user_name VARCHAR(50),
                FOREIGN KEY(admin_user_name) REFERENCES user_tb(username)
            )
        """)
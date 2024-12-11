# user dao
# db 관련

from app.mongodb.mongodb import client #mongodb cilent 연결


db = client["database"] # database 선택 
collection = db["user"] # collection 선택

def user_entity(user) -> dict:
    return{
        "id": str(user["_id"]),
        "name": str(user["name"]),
        "email": str(user["email"]),
        "password": str(user["password"]),   
    }

def user_list(users) -> list:
    return [user_entity(user) for user in users]
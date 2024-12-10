# user dao
# db 관련

from app.mongodb.mongodb import client #mongodb cilent 연결
from app.model.user import User
db = client["database"] #database 선택 
db["user"] #collection 선택
# router

def user_entity(db) -> dict:
    return{
        "_id":str(db['_id'].value()),
        "name": db['name'],
        "email": db['email'],
        "password": db['password']    
    }
    
def user_list(db) -> list:
    user_list = []
    for User in db: 
        user_list.append(user_entity(User))
    return user_list
    
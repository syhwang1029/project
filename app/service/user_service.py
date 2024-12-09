from bson import ObjectId
from fastapi import FastAPI
from app.mongodb.mongodb import MongoClient
from model.user import User
app = FastAPI() 

# Mongodb 클라이언트 생성
cilent = MongoClient.create_mongo_client()
db = MongoClient.get_database(cilent, "database")
collection = db['user']

## user ##
@app.post("/user/insert")
async def insert_db(user: User):
    user_dict = user.dice()
    MongoClient.insert_user(collection, user_dict)
    return {"user":"ok!"}

# 참고
# https://hanseungwan24.tistory.com/entry/Fast-API-%EA%B5%AC%EC%B6%952

# 생성
# @app.post("/user/")
# async def create_user(name: str, email: str, password: str):
#     user = await get_collection.insert_One({"name":get_collection[name], "email":get_collection[email],"password":get_collection[password]})
#     return user
    
# # 조회
# @app.get("/user/{user_id}")
# def get_user(user_id: str):
#     user = get_collection.find_one({"_id":ObjectId(user_id)})
#     return user

# user dao
# db 관련 저장 

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 

from bson import ObjectId
from app.mongodb.mongodb import client #mongodb cilent 연결

# mongndb 정보들 선택
db = client["database"] # user database 선택 
collection = db["user"] # user collection 선택

# 유저 정보
# user repository 
class UserRepository: 
# 1. 생성 (create)   
    def create_repository(self, user: dict) -> dict: # user 생성
                # dict = {key:value} => json 객체
        users = collection.insert_one(user) 
                        # db create 명령어 
        return str(users.inserted_id) # ObjectId
    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
    
# # 2. 조회 (read)
#     def read_repository(self): # user 조회
#         response = collection.find()
#                     # db read 명령어
#         data = [] # List 초기화
#         for user in response:
#             user["_id"] = str(user["_id"]) # "_id"(ObjectId)로 user 검색 
#             data.append(user) # append : 데이터 추가
#         return data 

# 3. 수정 (update)
    def update_repository(self, user_id: str, user: dict): # user 수정
        users = collection.update_one({"id": ObjectId(user_id)},# ObjectId 지정 
                                        {"$set": user})
                                # db update 명령어
        return users 
# 4. 삭제 (dlelte)
#     def delete_repository(self, email): # user 삭제
#         response = collection.delete_one({"email":email})
#                                             #email로 User 삭제
#         # db delete 명령어
#         return response.deleted_count


# user dao
# db 관련 조건 . 및저장 

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 

from bson import ObjectId
from app.mongodb.mongodb import client # mongodb cilent 연결
# model 사용 x

# mongndb 정보들 선택
db = client["database"] # user database 선택 
collection = db["user"] # user collection 선택

# 유저 정보
# user repository 
class UserRepository: 
# 1. 생성 (create)   
    # 비동기
    async def create_repository(self, user: dict)->dict: # user 생성
        # collection에서만 dict 상속 가능함
        users = collection.insert_one(user) 
                        # db create 명령어 
        return str(users.inserted_id) # ObjectId 
        # object에서는 await 사용 불가능힘
        
    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
    
# 5. 일부 조회 (read)
    async def read_repository_userid(self, user_id: str):
        users = collection.find_one({"_id":ObjectId(user_id)})
        return users
    
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
    async def update_repository(self, user_id: str, user: dict): # user 수정
        users = collection.update_one({"_id": ObjectId(user_id)},# ObjectId 지정 
                                        {"$set": user})
                                # db update 명령어
        return users
# 4. 삭제 (dlelte)
#     def delete_repository(self, email): # user 삭제
#         response = collection.delete_one({"email":email})
#                                             #email로 User 삭제
#         # db delete 명령어
#         return response.deleted_count


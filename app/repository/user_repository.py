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
 
 # 5. 일부 조회 (read)
    async def read_repository_userid(self, user_id: str):
        users = collection.find_one({"_id":ObjectId(user_id)}) # objectId = user_id 지정
        users["_id"] = str(users["_id"]) # str으로 수정
        # ObjectID 참고 
        # https://github.com/accubits/FastAPI-MongoDB
        return users
 
 # 4. 전체 조회 (read)
    async def read_repository(self): # user 조회
        # 비동기
        return collection.find()
    
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
    
# 2. 수정 (update)
    async def update_repository(self, user_id: str, user: dict): # user 수정
        users = collection.update_one({"_id": ObjectId(user_id)}, # objectId로 수정 
                                        {"$set": user})
                            # db update 명령어                  
        return users.modified_count # query 실행 후, doc 값이 변하면 modified_count = 1
    # MongoDB 명령어 참고
    # https://velog.io/@hosunghan0821/DBs-MongoDB-%EA%B8%B0%EB%B3%B8%EC%BF%BC%EB%A6%AC
    
# 3. 삭제 (dlelte)
    async def delete_repository(self, user_id: str): # user 삭제
        users = collection.delete_one({"_id": ObjectId(user_id)}) # objectId로 삭제
                         # db delete 명령어
        return users.deleted_count
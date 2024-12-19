# user dao
# db 관련 조건문(mongodb 명령어) 및 data 저장 

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 

from bson.objectid import ObjectId # mongodb objectId
from app.database.database.user_collection import db, collection # mongodb 
from app.token.utillity import Token # jwt utillity
# model 사용 x


# 유저 정보
# user repository 
class UserRepository:   
    def __init__(self): #mongodb 정보
        self.db =  db #user database
        self.collection = collection # user colletcion
        
        self.token = Token() # jwt

      
 # 5. 전체 조회 (read)
    async def read_repository(self): # user 조회
        # 비동기
        users = collection.find() # db find 명령어
        userlist = [] # user list 초기화
        for user in users: #user 객체에 db find 명령어 대입 
            user["_id"] = str(user["_id"]) # user 객체에 ObjectId 대입
            userlist.append(user) # userlist에 데이터 추가
        return userlist
        # 조회 참고
        # https://github.com/accubits/FastAPI-MongoDB
 
 # 4. 일부 조회 (read)
    async def read_repository_userid(self, user_id: str):
        users = collection.find_one({"_id":ObjectId(user_id)}) # objectId = user_id 지정
        users["_id"] = str(users["_id"]) # str으로 수정
        # ObjectID 참고 
        # https://github.com/accubits/FastAPI-MongoDB
        return users
    
# 1. 생성 (create)   
    # 비동기
    async def create_repository(self, user: dict): # user 생성
        # collection에서만 dict 상속 가능함
        users = collection.insert_one(user) 
                        # db create 명령어 
        return str(users.inserted_id) # ObjectId 
        # object에서는 await 사용 불가능힘
        
    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
    
# 2. 수정 (update) 
    async def update_repository(self, user_id: str, user: dict) -> dict: # user 수정
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
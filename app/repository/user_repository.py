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
        
        self.jwt = Token() # jwt
      
 # 5. 전체 조회 (read)
    async def read_repository(self): # user 조회
        # 비동기
        users = collection.find() # db find 명령어
        userlist = [] # user list 초기화
        for user in users: #user 객체에 db find 명령어 대입 
            user["_id"] = str(user["_id"]) # user 객체에 ObjectId를 문자열로 반환
            userlist.append(user) # userlist에 데이터 추가
        return userlist
        # 조회 참고
        # https://github.com/accubits/FastAPI-MongoDB
 
 # 4. 일부 조회 (read)
    async def read_repository_username(self, username: str): # username으로 특정 user 조회 
        user = collection.find_one({"username": username}) # None 
        if user: # objectId = user_id 지정
            user["_id"] = str(user["_id"]) # str으로 수정
        return user 
        # ObjectID 참고 
        # https://github.com/accubits/FastAPI-MongoDB
    
         # 해당 user(대상)가 아닌 경우, 무효(None) 처리함
                # return None 설명 참고
                # https://velog.io/@munang/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4
    
# 1. 생성 (create)   
    # 비동기
    async def create_repository(self, user: dict): # user 생성
        # collection에서만 dict 상속 가능함
        users = collection.insert_one(user) 
                        # db create 명령어 
        return str(users.inserted_id) # ObjectId = _id 필드 생성
        # object에서는 await 사용 불가능함   
    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
    
# 2. 수정 (update) 
    async def update_repository(self, user_id: str, user: dict): # user_id로 user 수정
        users = collection.update_one({"_id": ObjectId(user_id)}, # objectId = user_id
                                        {"$set": user}) # user 전체 정보
                            # db update 명령어                
        return users.modified_count # query문(collection.update_one) 실행 후 document 값이 변경되면,
                                    # 성공 modified_count = 1 
                                    # / 실패  modified_count = 0
    # MongoDB 명령어 참고
    # https://velog.io/@hosunghan0821/DBs-MongoDB-%EA%B8%B0%EB%B3%B8%EC%BF%BC%EB%A6%AC
    
# 3. 삭제 (dlelte)
    async def delete_repository(self, user_id: str): # user_id로 특정 user 삭제
        users = collection.delete_one({"_id": ObjectId(user_id)}) # objectId = user_id
                         # db delete 명령어
        return users.deleted_count # 성공 deleted_count = 1 
                                   # 실패 deleted_count = 0
    
    
            
# user dao
# db 관련 조건문(mongodb 명령어) 및 data 저장 

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 

from bson.objectid import ObjectId
from app.database.database.user_collection import db, collection # mongodb 

from app.token.utillity import Token # jwt utillity
# model 사용 x


# 유저 정보
# user repository 
class UserRepository:   
    def __init__(self): #mongodb 정보
        self.db = db # user database
        self.collection = collection # user colletcion
        
        self.jwt = Token() # jwt
      
 # 5. 전체 조회 (read)
    async def read_repository(self): # user 전체 조회
        # 비동기 
        users = collection.find() # db find 명령어
        userlist = [] # user list 초기화
        # objectid = list 형태의 array를 받음
        for user in users: # for in 반복문 : 
                            # user collection에서 조회한 user data을 user 객체로 확인
                            # for in 반복문 참고
                            # https://wikidocs.net/16045
            user["_id"] = str(user["_id"]) # json type으로 변경 
                                           # json 형태인 objectid = string으로 변경 작업 필요
                                           # "_id"의 key => str 으로 변경 ==> json 형태
                                           # 요약 : objectid을 str으로 변경하여 json 형태로 사용함
                                           # pymongo objectid 참고 
                                           # https://blog.voidmainvoid.net/334
            userlist.append(user) # userlit 객체 list에 원소 (data) 추가
        return userlist # userlist로 user 조회
        # 조회 참고
        # https://github.com/accubits/FastAPI-MongoDB

  # 4. 일부 조회 (read) - token
    async def read_repository_username(self, username: str): # username으로 특정 user 조회 
        user = collection.find_one({"username": username}) 
        if user: # objectId = user_id 지정
            user["_id"] = str(user["_id"]) # str으로 수정
            return user 
        # ObjectID 참고 
        # https://github.com/accubits/FastAPI-MongoDB
        return None
         # 해당 user(대상)가 아닌 경우, 무효(None) 처리함
                # return None 설명 참고
                # https://velog.io/@munang/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4
 

# 6. 일부 조회 (read) - userid
    async def read_repository_userid(self, user_id: str): # userid로 user 조회
        # 비동기 
        users = collection.find_one({"_id":ObjectId(user_id)}) # db raed 명령어
        # 1. pymongo를 통해 collection에서 find한 objectid는 유효한 json 타입이 아님
                            # userid로 user 조회(조건)
        users["_id"] = str(users["_id"]) # user 조회
        # 2. 그리하여 string으로 변환하여 json 형태로 결과값을 받음.
        return users # user 조회 결과 반환
 
# 7. 일부 조회 (read) - email
    async def read_repository_email(self, email: str): # email로 user 조회
        # 비동기
        users = collection.find_one({"email":email}) # db read 명령어 
                        # email로 조회 (조건)
        users["_id"] = str(users["_id"]) # string으로 반환하여 json 사용
        return users  # users로 결과 반환
    
# 1. 생성 (create)   
    # 비동기
    async def create_repository(self, user: dict): # user 생성
        # collection에서만 dict 상속 가능함
        user_idct = dict(user) # 1. user = user.dict()
        # user_idct 선언 이유 : 쿼리 매개변수 user와 따로 구분 -> server에 넘길 때만 사용
        # repository에서만 사용함
        users = collection.insert_one(user_idct) # db create 명령어 
        # 2. collection.insert_one(user)
        user_idct["_id"] = str(users.inserted_id) # insertde_id : objectid (고유 키) 자동 생성 
        # 3. objectid를 string으로 결과값 받기 => json 형태로 변환 
        return user_idct # ObjectId = "_id" 
        # objectid 에서는 await 사용 불가능함   
        # 4. user 생성 반환
        
        
    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
    
    # crud 참고
    # https://apidog.com/kr/blog/fastapi-and-mongodb-2/
    
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
    
    
            
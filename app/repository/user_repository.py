# user dao
# db 관련

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 

from app.mongodb.mongodb import client #mongodb cilent 연결

# mongndb 정보들 선택
db = client["database"] # user database 선택 
collection = db["user"] # user collection 선택

# user repository 
class UserRepository: 
# 1. 생성 (create)   
    def create_repository(self, data): # user 생성
        # data 객체에 user 정보 저장
        data = dict(data) # dict = {key:value} => json 객체
        response = collection.insert_one(data) # response(응답) 
                        # db create 명령어 
        return str(response.inserted_id) #response : 등록 id
                # id 지정

    # Mongodb 명령어 참고 
    # https://kimdoky.github.io/python/2018/12/03/python-nosql/
# 2. 조회 (read)
    def read_repository(self): # user 조회
        response = collection.find()
                    # db read 명령어
        data = [] # List 초기화
        for user in response:
            user["id"] = str(user["id"]) # "_id"(ObjectId)로 user 검색 
            data.append(user) # append : 데이터 추가
        return data 
# 3. 수정 (update)
    def update_repository(self, data): # user 수정
        # data["_id"] = ObjectId(data["_id"])
        response = collection.update_one({"id": data["id"]},
                                        {"$set": data})
                                #email로 User 변경
                                # db update 명령어
        return response.modified_count # 수정된 문저 수 포함 => user 수정후 db에 저장
# 4. 삭제 (dlelte)
    def delete_repository(self, email): # user 삭제
        response = collection.delete_one({"email":email})
                                            #email로 User 삭제
        # db delete 명령어
        return response.deleted_count


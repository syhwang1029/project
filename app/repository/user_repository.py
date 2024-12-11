# user dao
# db 관련

# crud 참고
# https://github.com/accubits/FastAPI-MongoDB 


from app.mongodb.mongodb import client #mongodb cilent 연결

# DB 설정
db = client["database"] # user database 선택 
collection = db["user"] # user collection 선택

# user repository 
class UserRepository: 
    def __init__(self, create_user, read_user, update_user, delete_user): # user crud
        self.create_user = create_user # 생성
        self.read_user = read_user # 조회
        self.update_user = update_user # 수정
        self.delete_user = delete_user # 삭제   
# 1. 생성 (create)   
    def create_user(data): # user 생성
        data = dict(data) # dict = {key:value}
        response = collection.insert_one(data) # response(응답) 
                        # db create 명령어 
        return str(response.inserted_id) #response : 등록 id
# 2. 조회 (read)
    def read_user(): # user 조회
        response = collection.find()
                    # db read 명령어
        data = [] # List 초기화
        for user in response:
            user["_id"] = str(user["_id"]) # "_id"(ObjectId)로 user 검색 
            data.append(user) # append : 데이터 추가
            return data
# 3. 수정 (update)
    def update_user(data): # user 수정
        data = dict(data)
        response = collection.update_one({"_id": data["id"]},
                                        {"$set": data})
                                # db update 명령어
        return response.modified_count
# 4. 삭제 (dlelte)
    def delete_user(id): # user 삭제
        response = collection.delete_one({"_id":id})
        # db delete 명령어
        return response.deleted_count
    






# def user_entity(user) -> dict:
#     return{
#         "id": str(user["_id"]),
#         "name": user["name"],
#         "email": user["email"],
#         "password": user["password"] 
#     }




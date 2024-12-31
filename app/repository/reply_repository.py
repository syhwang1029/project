from bson import ObjectId # objectid = replyid
from app.database.database.reply_collection import db, collection # reply mongodb

# reply repository
class ReplyRepository:
    def __init__(self): # mongodb
        self.db = db # reply database 
        self.collection = collection # reply collection 

    # 1. 생성 (create) 
    async def creat_repository(self, reply): # reply 생성
        replys = collection.insert_one(reply) # mongodb 명령어로 단일 문서인 reply의 data 생성 
           # mongodb 명령어에서는 await 사용 불가능함 
           # => repository 대신에 service에서 await을 사용함
        return self.read_repository_replyid(replys.inserted_id) # reply 문서 삽입되면서 objectid 자동생성
                    # replyid로 일부 문서 조회하는 함수(read_repository_replyid)로 반환
 
    # 5. 일부 조회 (read) - replyid
    async def read_repository_replyid(self, reply_id: ObjectId): # Objectid = replyid로 지정
        reply = collection.find_one({"_id":reply_id}) # objectid로 일부 reply의 data 조회
        if reply: 
            reply["_id"] = str(reply["_id"]) # pydantic에서 받아온 mongodb의 명령어는 유효한 json 객체 타입이 아님
                                            # 그리하여 str으로 형변환 후 유효한 json 유형으로 변환하여 reply의 data를 반환함 
            del reply["_id"] # 조회한 relpyid의 data가 없는 경우: objectid 삭제 (무효화)
        return reply # 조회한 reply의 data를 반환함
        
    # 4. 전체 조회 (read)
    async def read_repository(self) -> list: # reply 전체 조회
        replylist = [] # reply list 초기화
        replys = collection.find({}) # mongodb 명령어로 reply의 data 전체 조회
        for reply in replys: # replyid로 reply의 data 조회
            reply["id"] = str(reply["_id"]) # 유효한 json 형태로 reply의 data를 받기 위한 str 형변환
            del reply["_id"] # 조회한 replyid가 없는 경우 : objectid 삭제
            replylist.append(reply) # 조회한 reply의 data를 list에 추가 
        return replylist # 조회한 reply의 data를 list 형태로 반환함
    # list 형태로 전체 reply 조회
    
    
    # 2. 수정 (update)
    async def update_repository(self, reply_id: ObjectId, reply): 
        collection.update_one({"_id": reply_id}, # objectid = reply id
                               {"$set": reply}) # 수정할 reply의 data 지정
        return self.read_repository_replyid(reply_id) 
            # replyid로 일부 문서 조회하는 함수(read_repository_replyid)로 반환
    
    # 3. 삭제 (delete)
    async def delete_repository(self, reply_id: ObjectId) -> bool: # objectid로 지정 후 reply 삭제
        reply_delete = collection.delete_one({"_id":reply_id}) # Objectid = reply id
        return reply_delete.deleted_count > 0 # bool 타입으로 반환하여, 
                                             # 결과 값이 1인 경우 ture, 0인 경우 false
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
        reply = collection.find_one({"_id" : reply_id}) # objectid로 일부 reply의 data 조회
        if reply: 
            reply["_id"] = str(reply["_id"]) # pydantic에서 받아온 mongodb의 명령어는 유효한 json 객체 타입이 아님
                                            # 그리하여 str으로 형변환 후 유효한 json 유형으로 변환하여 reply의 data를 반환함 
            del reply["_id"] # 조회한 relpyid의 data가 없는 경우: objectid 삭제 (무효화)
        return reply # 조회한 reply의 data를 반환함
        
    # 4. 전체 조회 (read)
    
    
    # 2. 수정 (update)
    # 3. 삭제 (delete)

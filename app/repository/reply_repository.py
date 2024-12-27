from bson import ObjectId
from app.database.database.reply_collection import db, collection # reply collection

# reply repository
class ReplyRepository:
    def __init__(self):
        self.db = db # reply database 
        self.collection = collection # reply collection 

    # 1. 생성 (create)
    async def creat_repository(self, reply):
        replys = collection.insert_one(reply) # 단일 문서 삽입 
        return await self.read_repository(replys.inserted_id)
    # 2. 수정 (update)
    # 3. 삭제 (delete)
    # 4. 조회 (read)
    async def read_repository(self, reply_id: ObjectId):
        reply = await collection.find_one({"_id" : reply_id})
        if reply:
            reply["_id"] = str(reply["_id"])
            del reply["_id"]
        return reply
        
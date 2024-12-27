from bson import ObjectId # comment id
from app.database.database.comment_collection import db, collection # comment collection

# crud 참고 
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j


# comment repository
class CommentRepositoty:
    def __init__(self):
        self.db = db # comment database
        self.collection = collection # comment collection 
    
# 1. 생성 (create)
    async def create_repository(self, comment): # 새로운 comment 생성 
        comments = collection.insert_one(comment) # comment 등록
        return await self.read_repository(str(comments.inserted_id)) # objectid 자동 생성

# 5. 일부 조회 (read) - commentid
    async def read_repository_commentid(self, comment_id: ObjectId): # 전체 comment 조회
            comment = collection.find_one({"_id":comment_id}) # commentid = ObjectId
            if comment: # comment collenction에서 data 조회
                comment["_id"] = str(comment["_id"]) # objectid str 변환
                                                     # 이유 : pymongo로 불러온 mongodb 명령어는 
                                                     # 유효한 json 타입이 아님 
                                                     # str 형변환 후 json 형태로 불러옴
                del comment["_id"] # data가 없는 경우 objectid 삭제
                return comment # 결과값 반환

# 4. 전체 조회 (raed) 
    async def read_repository(self) -> list: # list로 comment 결과값 반환
        commentlist = [] # comment의 data를 담을 list 초기화                          
        comments = collection.find() # comment collection에서 data 전체 조회
        for comment in comments: 
            comment["id"] = str(comment["_id"]) # objectid str 변환 
            del comment["_id"] # data가 없는 경우 objectid 삭제
            commentlist.append(comment) # 조회한 data를 list에 추가
        return commentlist # comment 결과값 반환
            
# 2. 수정 (update)
    async def update_repositoty(self, comment_id: ObjectId, comment): # comment id로 수정할 comment 지정
        collection.update_one({"_id":ObjectId(comment_id)},
                                         {"$set": comment}) # comment 수정
        return await self.read_repository(comment_id) # 수정 data 반환

# 3. 삭제 (delete)
    async def delete_repository(self, comment_id: ObjectId): # comment id로 comment 삭제
        comments = collection.delete_one({"_id":comment_id}) # comment 삭제
        return comments.deleted_count > 0 # deleted_count = 1 : 성공
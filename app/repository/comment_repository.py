from bson import ObjectId # comment id
from app.database.database.comment_collection import collection # comment collection

# crud 참고 
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j


# comment repository
class CommentRepositoty:
    def __init__(self):
        self.collection = collection # board collection 
    
# 1. 생성 (create)
    async def create_repository(self, comment: str):
        comments = collection.insert_one(comment)
        return self.read_repository(comments.inserted_id) # 등록한 댓글 조회
        
# 2. 수정 (update)
    async def update_repositoty(self, comment_id: str, comment):
        comments = collection.update_one({"_id":ObjectId(comment_id)},
                                         {"$set": comment})
        return self.read_repository(comments.modified_count)
# 3. 삭제 (delete)
    async def delete_repository(self, comment_id: str):
        comments = collection.delete_one({"_id":ObjectId(comment_id)})
        return comments.deleted_count > 0 # deleted_count = 1 : 성공

# 4. 조회 (read)
    async def read_repository(self): 
            commentlist = [] # list 초기화
            comments = collection.find() # comment collection 전체 조회
            for comment in comments: # comment 조회
                comment["_id"] = str(comment["_id"]) # objectid str 변환
                commentlist.append(comment) # list에 comment 추가 
            return commentlist # comment 결과 반환

# 5. 일부 조회 (read) - commentid
    async def read_repository_commentid(self, comment_id: str): # objectid
        comments = collection.find_one({"_id":ObjectId(comment_id)}) # comment id로 comment 조회
        comments["_id"] = str(comments) # comment id str 변환
        return comments # comment 결과 반환
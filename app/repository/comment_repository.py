from bson import ObjectId # comment id
from app.database.database.comment_collection import collection # comment collection

# crud 참고 
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j


# comment repository
class CommentRepositoty:
    def __init__(self):
        self.collection = collection # board collection 
    
# 1. 생성 (create)
    async def create_repository(self, comment: str): # 새로운 comment 생성 
        comments = collection.insert_one(comment) # comment 등록
        return self.read_repository(comments.inserted_id) # objectid 자동 생성
        
# 2. 수정 (update)
    async def update_repositoty(self, comment_id: str, comment): # comment id로 수정할 comment 지정
        comments = collection.update_one({"_id":ObjectId(comment_id)},
                                         {"$set": comment}) # comment 수정
        return self.read_repository(comments.modified_count) # modified_count = 1 : 성공 / = 0 : 실패

# 3. 삭제 (delete)
    async def delete_repository(self, comment_id: str): # comment id로 comment 삭제
        comments = collection.delete_one({"_id":ObjectId(comment_id)}) # comment 삭제
        return comments.deleted_count > 0 # deleted_count = 1 : 성공

# 4. 조회 (read)
    async def read_repository(self): # 전체 comment 조회
            commentlist = [] # comment의 data를 담을 list 초기화
            comments = collection.find() # 전체 comment collection 조회
            for comment in comments: # comment 조회
                comment["_id"] = str(comment["_id"]) # objectid str 변환
                                                     # 이유 : pymongo로 불러온 mongodb 명령어는 
                                                     # 유효한 json 타입이 아님 
                                                     # str 형변환 후 json 형태로 불러옴 
                commentlist.append(comment) # list에 comment의 data 추가 
            return commentlist # 추가된 commentlist로 comment 결과 반환

# 5. 일부 조회 (read) - commentid
    async def read_repository_commentid(self, comment_id: str):  # objectid = comment_id                              
        comments = collection.find_one({"_id":ObjectId(comment_id)}) # comment id로 comment 조회
        comments["_id"] = str(comments) # comment id str 변환
        return comments # comment 결과 반환
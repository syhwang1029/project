from bson import ObjectId # objectid = comment id
from app.database.database.comment_collection import db, collection # comment mongodb
# crud 참고 
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j


# 댓글 (comment)
# comment repository
class CommentRepositoty:
    def __init__(self): # comment mongodb
        self.db = db # comment database
        self.collection = collection # comment collection 
    
# 1. 생성 (create) 
    async def create_repository(self, comment): # 새로운 comment 생성 
        comments = collection.insert_one(comment) # mongodb 명령어로 새로운 comment의 data 등록
                    # 단일 문서로 comment 생성 
        return self.read_repository_commentid(comments.inserted_id) # objectid 자동 생성 
                            # objectid로 조회하는 함수(read_repository_commentid)로 반환

# 5. 일부 조회 (read) - comment id
    async def read_repository_commentid(self, comment_id: ObjectId): # comment id로 일부 comment의 data 조회
            comment = collection.find_one({"_id":comment_id}) # mongodb 명령어로 ObjectId로 지정한 comment id로 comment 조회 
            if comment:     
                comment["_id"] = str(comment["_id"]) # objectid : str 변환
                                                     # 이유 : pymongo로 불러온 mongodb 명령어는 유효한 json 타입이 아님 
                                                     # str 형변환 후 json 형태로 comment의 data를 불러옴
                del comment["_id"] # data인 경우 : objectid 삭제
            return comment # comment의 결과값 반환

# 4. 전체 조회 (raed) 
    async def read_repository(self) -> list: # list로 comment 결과값 반환
        commentlist = [] # comment의 data를 담을 list 초기화                          
        comments = collection.find({}) # mongodb명령어로 comment의 data 전체 조회
        for comment in comments: 
            comment["id"] = str(comment["_id"]) # objectid : str 변환 
            del comment["_id"] # data가 없는 경우 : objectid 삭제
            commentlist.append(comment) # 조회한 comment의 data를 list에 추가
        return commentlist # comment의 결과값 반환

            
# 2. 수정 (update)
    async def update_repositoty(self, comment_id: ObjectId, comment): # comment id로 수정할 comment 지정
        collection.update_one({"_id":comment_id}, 
                              {"$set": comment}) # comment의 data 수정
        return self.read_repository_commentid(comment_id) # 수정한 comment의 data 반환

# 3. 삭제 (delete)
    async def delete_repository(self, comment_id: ObjectId) -> bool: # comment id로 comment 삭제 
        comments = collection.delete_one({"_id":comment_id}) # comment 삭제
        return comments.deleted_count > 0 # deleted_count = 1 : 성공 # bool로 반환
from ctypes import Array
from bson.objectid  import ObjectId
from app.database.database.board_collection import db, collection # mongodb
from app.repository.comment_repository import CommentRepositoty # comment repository

# crud 참고 1
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j

# crud 참고 2
# https://jay-ji.tistory.com/86


# 게시판
# board repository
class BoardRepository: 
        def __init__(self): # mongodb
            self.db = db # board database
            self.collection = db # board colletcion
            
            # comment
            self.com = CommentRepositoty() # comment repository
            self.com_col = self.com.collection # comment collection 
    
    # 5. 전체 조회 (read)
        async def read_repository(self) -> list:
        # 비동기
            boards = collection.find() # mongodb find 명령어
            boardlist = [] #board list 초기화
            for board in boards: #board라는 objectId로 board 컬렉션 데이터 조회 
                board["_id"] = str(board["_id"]) # objectId로 조회 
                boardlist.append(board) # board 컬렉션에 있는 데이터 조회
            return boardlist 
        
    # 4. 일부 조회 (read) #ObjectId(board id)로 조회
        async def read_repository_boardid(self, board_id: str): # ObjectId
            # 비동기 
            boards = collection.find_one({"_id": ObjectId(board_id)})  
            boards["_id"] = str(boards["_id"]) # objectId로 board id 지정
            return boards          
          
    # 1. 생성 (create) # 단일 문서 삽입
        async def create_repository(self, board: dict): # dict = {key, value}  
        # 비동기                              
            boards = collection.insert_one(board)
                     # monnodb data insert 명령어
            return str(boards.inserted_id) # ObjectId 자동 생성 
                            # boardid <= update, delete 때 특정조건으로 사용 
        # insert_id 설명 
        # https://kimdoky.github.io/python/2018/12/03/python-nosql/
        
        # ObjectId = RDB Primary key 개념
        # https://stackoverflow.com/questions/8783753/how-to-get-the-object-id-in-pymongo-after-an-insert
        # https://www.inflearn.com/community/questions/697448/inserted-id-%EB%A1%9C-db%EC%97%90-%EA%B0%92%EC%9D%B4-insert%EB%90%98%EC%97%88%EB%8A%94%EC%A7%80-%ED%99%95%EC%9D%B8-%EA%B0%80%EB%8A%A5%ED%95%9C%EB%8D%B0-update%EC%8B%9C%EC%97%90%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%99%95%EC%9D%B8-%EA%B0%80%EB%8A%A5%ED%95%A0%EA%B9%8C%EC%9A%94?srsltid=AfmBOorNfR3e0nGBoB5C0R-9TxHsIY301YjS5OdgNWewX3i5Ie988C-9
        
    # 2. 수정 (update)
        async def update_repository(self, board_id: str, board: dict): #data는 mongodb 저장 => dict, id는 str => ObjectId
        # 비동기

        # objectId 설정
        # https://damansa1.tistory.com/58
            boards = collection.update_one({"_id": ObjectId(board_id)},  # {field($set):vlaue}
                                        {"$set": board}) 
                                                # monodb update 명령어 
                                                # 특정 조건(board id) 하나로 수정
        # $set 설명
        # https://www.mongodb.com/ko-kr/docs/v5.0/reference/operator/update/set/
            return boards.modified_count # query 실행 후, doc 값 변경 후 modified_count = 1 
                    # mongodb 기본 쿼리 참고
                    # https://velog.io/@hosunghan0821/DB-MongoDB-%EA%B8%B0%EB%B3%B8%EC%BF%BC%EB%A6%AC
    
    # 3. 삭제 (delete)
    # crud 참고 3 (delete)
    # https://coding-shop.tistory.com/383
        async def delete_repository(self, board_id: str):
            # 비동기
            boards = collection.delete_one({"_id": ObjectId(board_id)})
                    # mongodb delete 명령어
                    # 하나만 삭제
            return boards.deleted_count 
    
    # 6. 게시판 생성 (crate), 게시판에 comment 추가 (update)
        async def create_repository_from_comment(self, board_id: str, comment: dict) -> bool:
            comment_data = self.com_col.insert_one(comment) # comment collection에 data 생성
            comment_id = str(comment_data.inserted_id) # comment 생성되면서 objectid 자동 생성
            comment_id = collection.update_one(                
                    {"_id": ObjectId(board_id)}, # boardid로 comment 추가할 board 지정
                    {"$push": {"comment":str(ObjectId(comment_id))}} # 생성한 comment 필드를 "$push" 연산자로 board에 추가 
            )
            return comment_id.modified_count > 0 # 추가 성공 = 1, 추가 실패 = 0)

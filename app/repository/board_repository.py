from bson import ObjectId
from app.mongodb.mongodb import client #mongodb cilent 연결
from app.model.board import Board # board model
# crud 참고 1
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j

# crud 참고 2
# https://jay-ji.tistory.com/86

# board mongodb
db = client["database"] # board database 선택 
collection = db["board"] # board collection 선택

        
# 게시판
# board repository
class BoardRepository:   
    # 1. 생성 (create) # 단일 문서 삽입
    def create_repository(self, board: dict): # dict = {key, value}                                
            boards = collection.insert_one(board)
                     # monnodb data insert 명령어
            return str(boards.inserted_id) # ObjectId <= update, delete때 사용  
    
        # insert_id 설명 
        # ObjectId = RDB Primary key 개념
        # https://stackoverflow.com/questions/8783753/how-to-get-the-object-id-in-pymongo-after-an-insert
        # https://www.inflearn.com/community/questions/697448/inserted-id-%EB%A1%9C-db%EC%97%90-%EA%B0%92%EC%9D%B4-insert%EB%90%98%EC%97%88%EB%8A%94%EC%A7%80-%ED%99%95%EC%9D%B8-%EA%B0%80%EB%8A%A5%ED%95%9C%EB%8D%B0-update%EC%8B%9C%EC%97%90%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%99%95%EC%9D%B8-%EA%B0%80%EB%8A%A5%ED%95%A0%EA%B9%8C%EC%9A%94?srsltid=AfmBOorNfR3e0nGBoB5C0R-9TxHsIY301YjS5OdgNWewX3i5Ie988C-9
        
    # 2. 수정 (update)
    def update_repository(self, board_id:str, board: dict): #data는 mongodb 저장 => dict, id는 str => ObjectId
        boards = collection.update_one({"_id":board_id},  # {filed($set):vlaue}
                                         {"$set": board}) # filed 값 지정
        # $set 설명
        # https://www.mongodb.com/ko-kr/docs/v5.0/reference/operator/update/set/
        return boards 
    
    
    # 3. 삭제 (delete)
    # crud 참고 3 (delete)
    # https://coding-shop.tistory.com/383
    def delete_repository(self, board_id:str):
        boards = collection.delete_one({"_id":board_id})
        return boards
    
        # 5. 전체 조회 (read)
    def read_repository_board(self):
        return collection.find()
        
    # 4. 조회 (read) #ObjectId로 조회
    def read_repository(self, board_id: str): # ObjectId
        board_id = collection.find_one({"_id": ObjectId(board_id)})  
        return board_id      

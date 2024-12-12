from app.mongodb.mongodb import client #mongodb cilent 연결
# https://www.tutorialspoint.com/fastapi/fastapi_using_mongodb.htm
from app.model.board import Board

# mongndb 정보들 선택
db = client["database"] # board database 선택 
collection = db["board"] # board collection 선택


# schema 참고글
# https://www.makeuseof.com/rest-api-fastapi-mongodb/
def board_schema(board) -> dict: # board schema
        return{
            "id": str(board["_id"]),
            "title": board["title"],
            "author": board["author"]
            }
        
def boards_schema(boards) -> list:
        return [boards_schema(board) for board in boards]

# board repository
class BoardRepository:        
    #1. 생성 (create)
    def create_repository(self, board: Board):
        _id = collection.insert_one(dict(board))
        board = boards_schema(collection.find({"_id":_id.inserted_id}))
        return {"board":board}
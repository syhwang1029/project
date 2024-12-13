# board service 
from app.repository.board_repository import BoardRepository # board repository
from app.model.board import Board # board model

# 게시판
# board repository 
class BoardService(): 
    def __init__(self): # board repository 인스턴스
        self.repository = BoardRepository() 
        
    # 1. 생성 (create) 
    def create_service(self, board: Board): # create
        board = dict(board) # data : dict 
        return self.repository.create_repository(board)

    # 2. 수정 (update)
    def update_service(self, board_id: str, board: Board): # update
        board = dict(board) # data : dict 
        return self.repository.update_repository(board_id, board)
    
    # 3. 삭제 (delete)
    async def delete_service(self, board_id: str):#board id로 delete
        return self.repository.update_repository(board_id)
    
    # 5.전체 조회 (read) 
    def read_service_board(self):
        return self.repository.read_repository_board()
    
    # 4. 조회 (read) 
    def read_service(self, board_id: str): #ObjectId
        return self.repository.read_repository(board_id)
        
    
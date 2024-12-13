# board service 
from app.repository.board_repository import BoardRepository # board repository
from app.model.board import Board # board model

# 게시판
# board repository 
class BoardService(): 
    def __init__(self): # board repository 인스턴스
        self.repository = BoardRepository() 
    
    # 1. 생성 (create)
    async def create_service(self, board: str): # create
        return self.repository.create_repository(board)
        
    
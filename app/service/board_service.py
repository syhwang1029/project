# board service 
from app.repository.board_repository import BoardRepository

class BoardService(): 
    def __init__(self): #board repository 인스턴스
        self.repository = BoardRepository()
    
    def create_service(self, board): # create
        return self.repository.create_repository(board)
        
    
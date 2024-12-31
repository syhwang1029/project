# board service 
from app.repository.board_repository import BoardRepository # board repository
from app.model.board import Board, UpBoard # board model
from app.model.comment import Comment # comment model

# 게시판
# board repository 
class BoardService: 
    def __init__(self): # board repository 인스턴스
        self.repository = BoardRepository() 
    
    # 5. 전체 조회 (read) 
    async def read_service(self):
        # 비동기 
        return await self.repository.read_repository()
                # 의존성 주입
    
    # 4. 일부 조회 (read) #boardid
    async def read_service_boardid(self, board_id: str): #ObjectId
        # 비동기 
        return await self.repository.read_repository_boardid(board_id)
            # 의존성 주입
        
        
    # 1. 생성 (create) 
    async def create_service(self, board: Board): # create 
        # 비동기
        board = dict(board) # data : dict 
        return await self.repository.create_repository(board)
            # 의존성 주입

    # 2. 수정 (update)
    async def update_service(self, board_id: str, board: UpBoard): # update model 추가
    # 비동기 
        board = dict(board) # board : dict 
        return await self.repository.update_repository(board_id, board)
        # 의존성 주입
    
    # 3. 삭제 (delete)
    async def delete_service(self, board_id: str):#board id로 delete
    # 비동기
        return await self.repository.delete_repository(board_id) #호출 메소드명 확인
            # 의존성 주입
    
    
    # 6. 댓글 추가 (crate)
    async def create_service_from_comment(self, board_id: str, comment: Comment):
        # board id를 입력하여 추가할 comment collection 지정,
        # Comment model로 생성한 comment를 collection에 저장
        comment = dict(comment) # comment.dict()
        return await self.repository.create_repository_from_comment(board_id, comment)  
# board router (crud)

from fastapi import APIRouter # router

from app.service.board_service import BoardService # board service
from app.model.board import Board # board model 


router = APIRouter( # router = FastAPI()
    prefix="/boards",  # board routing 
    tags=["Board"]
)

service = BoardService() # board service 객체

# 게시판 (board)
# 5. 전체 조회 (read)
@router.get("/board/") # 전체
def reat_boards():
    return service.read_service_board()

# 4. 일부 조회 (read) #ObjectId
@router.get("/board/{board_id}")#ObjectId
def reat_board(board_id: str):
    return service.read_service(board_id)


# 1. 생성 (create)
@router.post("/board/") 
async def create_board(board: Board):
    # 비동기 
    return await service.create_service(board)


# 2. 수정 (update)
@router.put("/board/{board_id}")
def update_board(board_id: str, board: Board):
    return service.update_service(board_id, board)

# 3. 삭제 (deletw)
@router.delete("/board/{board_id}")
def delete_board(board_id: str): #board id(ObjectId)로 삭제
    return service.delete_service(board_id)


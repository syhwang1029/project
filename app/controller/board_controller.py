# board router (crud)

from fastapi import APIRouter # router

from app.service.board_service import BoardService # board service
from app.model.board import Board, UpBoard # board model 


router = APIRouter( # router = FastAPI()
    prefix="/boards",  # board routing 
    tags=["Board"] #태그 추가
)

service = BoardService() # board service 객체

# 게시판 (board)
# 5. 전체 조회 (read)
@router.get("/board/") # 전체
async def reat_board():
    # 비동기
    return await service.read_service()
        # 의존성 주입

# 4. 일부 조회 (read) #ObjectId
@router.get("/board/{board_id}") # ObjectId
async def reat_board_boardid(board_id: str):
    # 비동기 
    return await service.read_service_boardid(board_id)
        # 의존성 주입


# 1. 생성 (create)
@router.post("/board/") 
async def create_board(board: Board):
    # 비동기 
    return await service.create_service(board)


# 2. 수정 (update)
@router.put("/board/{board_id}")
async def update_board(board_id: str, board: UpBoard): #update model 추가
    # 비동기
    return await service.update_service(board_id, board)
        # 의존성 주입

# 3. 삭제 (deletw)
@router.delete("/board/{board_id}")
async def delete_board(board_id: str): #board id(ObjectId)로 삭제
    # 비동기
    return await service.delete_service(board_id)
        # 의존성 주입


# board router (crud)

from fastapi import APIRouter # router

from app.service.board_service import BoardService # board service
from app.model.board import Board # board model 


router = APIRouter( # router = FastAPI()
    prefix="/boards"  # board routing 
)

service = BoardService() # board service 객체

# 게시판
# 1. 생성 (create)
@router.post("/board") 
async def create_board(board: Board):
    return service.create_service(board)

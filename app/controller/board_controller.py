# board router


from fastapi import APIRouter

from app.service.board_service import BoardService
from app.model.board import Board
router = APIRouter( # board routing
    prefix="/boards"
)

service = BoardService

# 1. create 
@router.post("/board")
async def create_board(board: Board):
    return service.create_service(board)

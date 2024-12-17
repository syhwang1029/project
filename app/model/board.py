from typing import Optional # 선택 메소드
from pydantic import BaseModel, EmailStr

# 게시판
# Board 데이터 모델 정의
class Board(BaseModel):
    title: str # 게시판 제목
    content: str # 게시판 내용
    board_author: EmailStr # 게시판 작성자 => 이메일로 아이디 지정
# 댓글, 대댓글 author 구분  
# "board" 추가 => board_author

# 게시판, 댓글, 대댓글 => 서로 다른 user 

# update 
class UpBoard(BaseModel):
    title: Optional[str] = None # 선택
    content: Optional[str] = None # 선택
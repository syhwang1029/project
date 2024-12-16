from pydantic import BaseModel

# 게시판
# Board 데이터 모델 정의
class Board(BaseModel):
    title: str # 게시판 제목
    content: str # 게시판 내용
    board_author: str # 게시판 작성자 
# 댓글, 대댓글 author 구분  
# "board" 추가 => board_author

# 게시판, 댓글, 대댓글 => 서로 다른 user 
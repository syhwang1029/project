from pydantic import BaseModel

# Board 데이터 모델 정의
class Board(BaseModel):
    title: str # 게시판 제목
    content: str # 게시판 내용
    board_author: str # 게시판 작성자 
# 댓글, 대댓글 author과 구분하기 위하여 앞에 "board"를 추가함 => board_author
# 서로 다른 user 
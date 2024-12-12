from pydantic import BaseModel
# Board 데이터 모델 정의
class Board(BaseModel):
    title: str # 게시판 제목
    content: str # 게시판 내용
    author: str # 게시판 작성자
from typing import List, Optional
from pydantic import BaseModel, EmailStr

# 댓글 (comment) 모델 데이터 정의
class Comment(BaseModel):
    comment: str # 댓글 내용
    comment_author: EmailStr # 댓글 작성자
    reply : Optional[List[str]] =  [] # 대댓글 list 
    
# 댓글 수정   
class CommentUpdate(BaseModel):
    comment: Optional[str] = None # 선택값
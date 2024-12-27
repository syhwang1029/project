from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

from app.model.reply import Reply # 대댓글

# 댓글 
class Comment(BaseModel):
    comment: str # 댓글 내용
    comment_author: EmailStr # 댓글 작성자
    reply : Union[List[Reply], None] = None # 대댓글
 
# 댓글 수정   
class CommentUpdate(BaseModel):
    comment: Optional[str] = None 
    comment_author: EmailStr # 댓글 작성자

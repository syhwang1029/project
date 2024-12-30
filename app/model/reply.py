from typing import Optional
from pydantic import BaseModel, EmailStr

# 대댓글 (reply) 모델 데이트 정의
class Reply(BaseModel):
    reply: str # 대댓글 내용
    reply_author: EmailStr # 대댓글 작성자 
    
# 대댓글 수정
class ReplyUpdate(BaseModel):
    reply: Optional[str] = None # 선택값 
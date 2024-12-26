from pydantic import BaseModel, EmailStr

# 대댓글
class Reply(BaseModel):
    reply: str # 대댓글 내용
    reply_author: EmailStr # 대댓글 작성자 
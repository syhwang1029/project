# jwt schema
from pydantic import BaseModel

# token 모델 데이터 정의
class Token(BaseModel):
    access_token: str # secret key
    token_type: str # payload
    
class TokenData(BaseModel):
    username: str | None = None
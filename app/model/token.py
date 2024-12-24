# jwt schema
from typing import Optional
from pydantic import BaseModel

# token 모델 데이터 정의
class Tokens(BaseModel): 
    access_token: str # secret key
    token_type: str # payload
    
# token data
class TokenData(BaseModel):
    username: Optional[str] = None # 선택적
    # username
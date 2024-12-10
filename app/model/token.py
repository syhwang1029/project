# jwt schema
from pydantic import BaseModel

class Token(BaseModel): # jwt 데이터 모델 정의
    access_token: str 
    token_type: str
    name: str
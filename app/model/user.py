from pydantic import BaseModel # BaseModel: 데이터 모델 정의
# None : 기본, 선택적 type 설정
from bson import objectid

class User(BaseModel): #user 데이터 모델 정의
    _id: objectid
    uname: str 
    email: str 
    password: str 
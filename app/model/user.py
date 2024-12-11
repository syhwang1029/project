# user schema
from bson import ObjectId
from pydantic import BaseModel, Field # Database 모델의 정의
# 타입 검증, 오류 관리
# https://mobicon.tistory.com/627

# bson -> json 인코딩 역할 

class User(BaseModel): # user 데이터 모델 정의
    name: str 
    email: str
    password: str
    
class CreateUser(User): # 생성
    name : str
    email: str 
    password: str 

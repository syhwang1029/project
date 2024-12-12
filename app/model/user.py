# user schema
from bson.objectid import ObjectId
from pydantic import BaseModel, Field # Database 모델의 정의

# 타입 검증, 오류 관리
# https://mobicon.tistory.com/627

# bson -> json 인코딩 역할 
# user 데이터 모델 정의
class User(BaseModel): # 조회, 생성
    name: str 
    email: str
    password: str
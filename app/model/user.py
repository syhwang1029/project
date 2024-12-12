# user schema

from pydantic import BaseModel, Field # Database 모델의 정의

# 타입 검증, 오류 관리
# https://mobicon.tistory.com/627

# bson -> json 인코딩 역할 
# user 데이터 모델 정의

# ObjectId 참고
# https://www.mongodb.com/community/forums/t/why-do-we-need-alias-id-in-pydantic-model-of-fastapi/170728

# User 모델 정의 
class User(BaseModel): # 조회, 생성
    id: str #=  Field(default_factory=id, alias="_id") #ObjectId
        # model name, db key
    name: str # 이름
    email: str # 이메일
    password: str # 비밀번호
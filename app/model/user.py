# user schema

from pydantic import BaseModel # Database 모델의 정의

# 타입 검증, 오류 관리
# https://mobicon.tistory.com/627

# bson -> json 인코딩 역할 
# user 데이터 모델 정의

# ObjectId 참고
# https://www.mongodb.com/community/forums/t/why-do-we-need-alias-id-in-pydantic-model-of-fastapi/170728

# User 모델 데이터 정의 
class User(BaseModel): # 조회, 생성
    username: str # 이름 #token 구분
    email: str # 이메일

# 입력 UserIn 
class UserIn(User): # 리캡 : User 클래스 상속받음 
    password: str # 비밀번호 포함 
    # 그외 그대로 사용

# 출력 UserOut 
class UserOut(User):
     pass # 비밀번호 미포함
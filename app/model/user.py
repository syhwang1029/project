# user schema

from typing import Optional # 선택적
from pydantic import BaseModel, EmailStr # Database 모델의 정의

# 타입 검증, 오류 관리
# https://mobicon.tistory.com/627

# bson -> json 인코딩 역할 
# user 데이터 모델 정의


# User 모델 데이터 정의 
class User(BaseModel): # 조회, 생성
    username: str  # 이름 #token 구분
    email: EmailStr # 이메일
                    #user@example.com
    # EmailStr 다운로드 
    # pip install 'pydantic[email]'
    # https://docs.pydantic.dev/latest/install/
   
# model 리캡 참고
# https://fastapi.tiangolo.com/ko/tutorial/extra-models/#reduce-duplication
# 입력 UserIn 
class UserIn(User):
     password: str # 비밀번호 포함 
     
# 출력 UserOut 
class UserOut(User): # 리캡 : User 클래스 상속받음 
     pass # 비밀번호 미포함
 
# Updata
class UpUser(BaseModel): 
     username: str | None = None # 선택값 = Optional = 기본값 = None 
     email: EmailStr | None = None
     password: str | None = None
# model Nono 참고 - Python 3.10 
# https://fastapi.tiangolo.com/ko/tutorial/body-multiple-params/#path-query     
     

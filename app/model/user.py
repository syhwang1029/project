# user schema

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
    password: str # 비밀번호 포함 
    
# model 리캡 참고
# https://fastapi.tiangolo.com/ko/tutorial/extra-models/#reduce-duplication
# 입력 UserIn 
class UserIn(BaseModel): # 리캡 : User 클래스 상속받음
    username: str = None # 이름 #token 구분
    email: EmailStr = None   # 이메일
    password: str = None # 비밀번호 포함 
    # 그외 그대로 사용

# 출력 UserOut 
class UserOut(User):
     pass # 비밀번호 미포함

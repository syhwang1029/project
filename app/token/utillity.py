# jwt 참고
# https://essenceofinvesting.tistory.com/114

from passlib.context import CryptContext # 비밀번호 해싱 (passlib) + 알고리즘 (bcrypt) 포함

# JWT = json web tokens
class Token:
# passlib context
# db 저장 전에 비밀번호 해싱

# password 해싱 유틸리티
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                            # 알고리즘 : bcrypt 


# JWT (json web token) 토큰 생성을 위한 설정 
# => Payload
SECRET_KEY = "3e43d54f6479cb9dd441c33538e3f10180f5aa891de8b52d6248bfc0926bdbfa" # 비밀 키
ALGORITHM = "HS256" # 암호화 해시 알고리즘 
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 만료시간 = 30분
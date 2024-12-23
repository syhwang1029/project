# jwt 참고
# https://essenceofinvesting.tistory.com/114

from passlib.context import CryptContext # 비밀번호 해싱 (passlib) + 알고리즘 (bcrypt) 포함

# JWT = json web tokens
class Token:
# passlib context
# db 저장 전에 비밀번호 해싱

# 패스워드 해싱 유틸리티
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                            # 알고리즘 : bcrypt 


# jwt(json web token) 생성 => Payload
SECRET_KEY = "46e183100685ba84b28891a51d305d17105a7f073026b8afd9fb57ac5cb5b00c" # 비밀 키
ALGORITHM = "HS256" # 암호화 해시 알고리즘 
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 만료시간 = 30분
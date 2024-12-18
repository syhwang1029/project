from passlib.context import CryptContext # 비밀번호 해싱 + 알고리즘 포함

import os # 운영체제와 상호작용
from datetime import datetime, timedelta #시간과 날짜
from typing import Union, Any 
# union[A,B] -> 두가지 이상의 타입 : 합집합 ㄴ
# any : 하나라도 True이면 True 반환, 모두 False이면 False 반환

from jose import jwt # jwt 토큰 
# jose : 웹 어플리케이션 보안 점검
# token : 클라이언트에서 인증 정보 보관 방법

# passlib context
# 암호 해싱을 위한 구성 컨텍스트
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                            # 알고리즘 : bcrypt

# jwt 생성 
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 액세스 만료 시간
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 새로고침 만료 시간
ALGORITHM = "HS256" # 알고리즘

# 비밀 유지
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY'] # jwt 비밀 키
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY'] # 새로고침 jwt 비밀 키

# 유저 토큰
# token repository
class TokenRepository:
# 일반 비밀번호 -> 데이터베이스에 안전하게 저장할 수 있는 해시 반환                            
    async def get_hashed_password(password: str) -> str:
        return password_context.hash(password)

    # 일반 비밀번호와 해시 비밀번호 일치 여부 확인
    async def verify_password(password: str, hashed_pass: str)-> bool:  # True / False
        return password_context.verify(password, hashed_pass)
                        # verify 함수로 비밀번호 일치 여부 확인 
                        # password = hashed_pass ? 
                        
    # 비밀유지 설정
    # 새로고침 토큰 만료시간이 액세스 토큰 만료시간보다 길음
    async def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
            
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
        return encoded_jwt
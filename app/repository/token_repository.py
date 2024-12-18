# jwt 참고
# https://essenceofinvesting.tistory.com/114

from passlib.context import CryptContext # 비밀번호 해싱 + 알고리즘 포함
import os # 운영체제와 상호작용
from datetime import datetime, timedelta # 시간과 날짜
from typing import Union, Any 
# union[A,B] -> 두가지 이상의 타입 : 합집합 
# any : 하나라도 True이면 True 반환, 모두 False이면 False 반환

from jose import jwt # jwt 토큰 
# jose : 웹 어플리케이션 보안 점검
# token : 클라이언트가 직접 자신에 해당하는 정보를 저장하는 방식 (보관)
# JWT = Header + Payload + Signature (Base64)



# jwt(json web token) 생성 => Payload
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 액세스 만료시간
                                # 30 minute
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 새로고침 만료시간
                                    # 7day
ALGORITHM = "HS256" # 암호화 해시 알고리즘 => header
# 쿠키x -> 보안적인 문제 대비 예방

# secret key
# os : 환경 변수
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY'] # jwt 임의의 비밀 키
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY'] # 새로고침 jwt 비밀 키
# os.environ : 파이썬 코드에 접근하여 환경변수 이름과 값 딕셔너리 형태로 저장 
# 딕셔너리 형태 = {"환경변수 이름":"값"}

# passlib context
# 암호 해싱을 위한 구성 컨텍스트
# db 저장 전에 비밀번호 해싱
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                            # 알고리즘 : bcrypt
                            
                            
# token repository
class TokenRepository:
# 일반 비밀번호 -> 해시로 반환 -> db에 안전하게 저장                            
    async def get_hashed_password(password: str) -> str:
                                                # return 값 = str
        return password_context.hash(password)
                                # hash : 임의의 길이의 데이터(key)를 고정된 길이의 데이터(hash value)로 매핑(=hashing)

    # 일반 비밀번호와 해시 비밀번호 일치 여부 확인
    async def verify_password(password: str, hashed_pass: str) -> bool: 
                                                            # return 값 = bool (True / False)
        return password_context.verify(password, hashed_pass)
                        # verify 함수로 비밀번호 일치 여부 확인 
                        # password = hashed_pass => bool로 return
                        
    # 비밀유지 설정
    # 새로고침 토큰 만료시간이 액세스 토큰 만료시간보다 길음
    async def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
                                   # str or any type
                                                                # int = 알수없음(None)
        if expires_delta is not None: # Ture
                        # is not None : is 연산자 호출
                            # => is 연산자 : 좌/우 값이 같은 Object(객체) 인지 확인 
                        # None : 초기화되지 않는 변수
                        # expires_delta 객체와 None 동일한지 여부 확인
                        
            expires_delta = datetime.utcnow() + expires_delta 
                            # datetime.utcnow : 날짜와 시간 -> int
        else: # False
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
                                                    # timedelta : 두 날짜의 차이 계산
                                                    # 새로고침 만료시간
                                                    
        to_encode = {"exp": expires_delta, "sub": str(subject)}
                        # 만료 기간 
        # 해싱된 값 인코딩                 
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
                                            # 새로고침 비밀 키, 알고리즘
                    # jwt 인코드
        
        return encoded_jwt # str으로 return
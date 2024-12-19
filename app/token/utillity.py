# jwt 참고
# https://essenceofinvesting.tistory.com/114

from passlib.context import CryptContext # 비밀번호 해싱 + 알고리즘 포함

from datetime import datetime, timedelta, timezone # 시간과 날짜

from jose import jwt # jwt 토큰 
# jose : 웹 어플리케이션 보안 점검
# token : 클라이언트가 직접 자신에 해당하는 정보를 저장하는 방식 (보관)
# JWT = Header + Payload + Signature (Base64)

# passlib context
# 암호 해싱을 위한 구성 컨텍스트
# db 저장 전에 비밀번호 해싱
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                            # 알고리즘 : bcrypt


# jwt(json web token) 생성 => Payload
SECRET_KEY = "46e183100685ba84b28891a51d305d17105a7f073026b8afd9fb57ac5cb5b00c" # jwt 임의의 비밀 키
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 액세스 만료시간 = 30분
ALGORITHM = "HS256" # 암호화 해시 알고리즘 => header
# 쿠키x -> 보안적인 문제 대비 예방 
                           
# jwt - token
class Token: 
# 일반 비밀번호 -> 해시로 반환 -> db에 안전하게 저장                            
    async def get_hashed_password(password: str) -> str:
                                                # return 값 = str
        return password_context.hash(password)
                                # hash : 임의의 길이의 데이터(key)를 고정된 길이의 데이터(hash value)로 매핑(=hashing)

    # 일반 비밀번호와 해시 비밀번호 일치 여부 확인 (검증)
    async def verify_password(password: str, hashed_pass: str) -> bool: 
                                                            # return 값 = bool (True / False)
        return password_context.verify(password, hashed_pass)
                        # verify 함수로 비밀번호 일치 여부 확인 
                        # password = hashed_pass => bool로 return
                        
    # 비밀유지 설정 -> 만료 시간
    async def create_refresh_token(data: dict, expires_delta: timedelta | None = None) -> str:  
                                                        # 시간차이 계산
        # 만료 시간
        to_encode = data.copy() # data 복사
        
        if expires_delta: # True인 경우
            # 만료 시간 데이터
            expire = datetime.now(timezone.utc) + expires_delta
                        # 날짜와 시간
                        
        else: # False인 경우
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
                    # 날짜와 시간
                    
            to_encode.update({"exp": expire}) # 만료 시간 측정
            
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
                                # 만료 시간, 비밀 키, 알고리즘
        return encoded_jwt # 측정 시간에 따른 비밀키 완료
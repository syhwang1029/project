# fake db    
from app.model.user import UserInDB # userdb medel
from app.token.utillity import Token # token
from app.token.utillity import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM 
from datetime import datetime, timedelta, timezone # 시간과 날짜
from jose import jwt # jwt 
from app.model.user import UserInDB # jwt 토큰 
# jose : 웹 어플리케이션 보안 점검
# token : 클라이언트가 직접 자신에 해당하는 정보를 저장하는 방식 (보관)
# JWT = Header + Payload + Signature (Base64)

# token repository
class TokenRepository:
    def __init__(self):
         self.jwt = Token() # token
         
# password
    # 일반 비밀번호와 해시 비밀번호 일치 여부 확인 (검증)
    def verify_password(self, plain_password, hashed_passworod):
                                                            # return 값 = bool (True / False)
        return self.jwt.pwd_context.verify(self, plain_password, hashed_passworod)
                        # verify 함수로 비밀번호 일치 여부 확인 
                        # password = hashed_pass => bool로 return
    
                        
    # 일반 비밀번호 -> 해싱 -> 해싱 비밀번호 db에 안전하게 저장                            
    def hashed_password(self, password):
                                                # return 값 = str
        return self.jwt.pwd_context.hash(self, password)
                        # hash : 임의의 길이의 데이터(key)를 고정된 길이의 데이터(hash value)로 매핑(=hashing)

    # user 정보
    def get_user(self, db, username: str): 
            if username in db: 
                user_dict = db[username]
            return UserInDB(**user_dict)
    
    # 사용자 인증
    def authenticate_user(self, fake_db, username: str, password: str):
            user = self.get_user(fake_db, username)
            if not user:
                return False
            if not self.verify_password(password, user.hashed_password):
                return False
            return user                 
    # JWT 설명 참고
    # https://velog.io/@taegong_s/%EC%8B%AD%EC%9E%90%EB%A7%90%ED%92%80%EC%9D%B4-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EA%B3%BC-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-JWT%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
    
# token
    # 토큰 생성
    # 비밀유지 설정 -> 만료 시간
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):  
                                            # 암호화 데이터, JWT 만료 시간
        # 만료 시간
        to_encode = data.copy() # data 복사
        
        if expires_delta: # True인 경우
            # 만료 시간 데이터
            expire = datetime.now(timezone.utc) + expires_delta
                        # 날짜와 시간
                        
        else: # False인 경우
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
                    # 날짜와 시간
                    
            to_encode.update({"exp": expire}) # 만료 시간 업데이트 (측정) 
            # 토큰에 만료 시간 포함
            
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
                                # 만료 시간, 비밀 키, 알고리즘
        return encoded_jwt # 비밀키 생성 완료
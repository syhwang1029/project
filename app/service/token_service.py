from datetime import datetime, timedelta, timezone
import jwt # jwt import
from app.repository.user_repository import UserRepository # user  repository
from app.token.utillity import Token, SECRET_KEY, ALGORITHM 

# jwt 참고1
# https://databoom.tistory.com/entry/FastAPI-JWT-%EA%B8%B0%EB%B0%98-%EC%9D%B8%EC%A6%9D-6
# jwt 참고2
# https://wikidocs.net/176934

 


# token service
class TokenService:
    def __init__(self):
        self.jwt = Token() # token
        self.repository = UserRepository() # user repository
# password
    # 일반 텍스트 비밀번호 해싱 
    # 동기 : 데이터의 요청과 결과가 한자리에서 동시에 일어나는 것                 
    def hashed_password(self, password: str) -> str:
                                                # return 값 = str
        return self.jwt.pwd_context.hash(password)
                        # hash : 임의의 길이의 데이터(key)를 고정된 길이의 데이터(hash value)로 매핑(=hashing)
    
    # 비밀번호 검증
    # user가 입력한 일반 텍스트 비밀번호와 
    # database에 저장된 해싱 비밀번호 검증은 
    # 데이터 요청과 동시에 일어나야 함 -> 동기적 처리
    def verify_password(self, plain_password: str, hashed_passworod: str) -> bool: 
                                                    # return 값 = bool (True / False)
                        # plain password : 일반 텍스트 비밀번호
                        # hashed password : 해싱 비밀번호 (암호화)
                                                            
        return self.jwt.pwd_context.verify(plain_password, hashed_passworod)
                        # verify 함수로 비밀번호 일치 여부 확인 
                        # password = hashed_pass => bool로 return  
    # JWT 설명 참고
    # https://velog.io/@taegong_s/%EC%8B%AD%EC%9E%90%EB%A7%90%ED%92%80%EC%9D%B4-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EA%B3%BC-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-JWT%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
    
 
# JWT 토큰 생성 함수
    # 만료 시간
    def create_access_token(self, user_data: dict, expires_delta: timedelta | None = None):  
                                    # data : 딕셔너리의 형태로 유저 정보 포함
                                    # expires_delta : jwt 만료시간
        # 유저정보 encode 
        # encoding : 사용자가 입력한 값을 컴퓨터 언어(code)로 변환시키는 것
        to_encode = user_data.copy() # 유저 정보 data 객체 담은 후 복사 
        
         # 토큰 만료시간
        if expires_delta: # True인 경우
            # 만료시간 데이터
            expire = datetime.now(timezone.utc) + expires_delta
                    # daetime: 날짜와 시간 조작
                    # now : 시간대 표기
                    # utc : 영국 + timezone = 영국의 현재 시간과 오늘의 날짜
                        
        else: # False인 경우
            expire = datetime.now(timezone.utc) + timedelta(minutes=15) # 기본 시간 15분
                    # 오늘의 날짜 + 15분 
                    # utcnow 더이상 사용하지 않기 때문에 now로 대체함
                                    
        to_encode.update({"exp": expire}) # 만료시간 측정 
            # 생성할 토큰에 만료시간 포함
            
        # JWT 토큰 encoding 
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
                                # encoding할 jwt의 data = 만료시간, 비밀키, 알고리즘
        return encoded_jwt # JWT 토큰 생성 완료
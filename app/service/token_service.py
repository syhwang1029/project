from datetime import datetime, timedelta, timezone
from typing import Annotated # 토큰 만료시간
from fastapi import Depends, HTTPException # 의존성 주입, 예외 처리
from fastapi.security import OAuth2PasswordBearer # 로그인시 토큰을 받기 위한 경로
from jwt.exceptions import InvalidTokenError
import jwt # jwt import
from app.model.token import TokenData # token data model
from app.repository.user_repository import UserRepository # user  repository
from app.token.utillity import Token, SECRET_KEY, ALGORITHM  # jwt 발급을 위한 설정
from fastapi import status


# jwt 참고1
# https://databoom.tistory.com/entry/FastAPI-JWT-%EA%B8%B0%EB%B0%98-%EC%9D%B8%EC%A6%9D-6
# jwt 참고2
# https://wikidocs.net/176934


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 
# 로그인시 token을 받기 위한 경로("/token") 정의


# token service
class TokenService:
    def __init__(self):
        self.jwt = Token() # token
        self.repository = UserRepository() # user repository
        self.oauth2_scheme = oauth2_scheme # token url

# password
    # 일반 텍스트 비밀번호 해싱                    
    async def hashed_password(self, password: str) -> str:
                                                # return 값 = str
        return self.jwt.pwd_context.hash(password)
                        # hash : 임의의 길이의 데이터(key)를 고정된 길이의 데이터(hash value)로 매핑(=hashing)
    
    # 비밀번호 검증
    async def verify_password(self, plain_password: str, hashed_passworod: str) -> bool: 
                                                    # return 값 = bool (True / False)
                        # plain password : 일반 텍스트 비밀번호
                        # hashed password : 해싱 비밀번호 (암호화)
                                                            
        return await self.jwt.pwd_context.verify(plain_password, hashed_passworod)
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
 
                 
# FastAPI에서 JWT 토큰 생성
    # 현재 user 정보 가져오기
    # 로그인 후 권한 인증
    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]): 
                            # Depends : token에 oauth2 의존성 주입
        # token 디코딩, 검증한 현재 user 반환
        
        # 예외 처리 
        credentials_exception = HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, # 예외 처리 시 반환할 상태 코드 
                # 401 에러 : 해당 리소스 접근 자격 증명이 없는 경우
                # from fastapi import status
                # status 참고
                # https://zambbon.tistory.com/entry/FastAPI-Custom-HTTPException-for-Auth-50
            detail="토큰 자격 증명을 검증할 수 없습니다.", # cilent에게 전달할 오류 메세지
            headers={"WWW-Authenticate": "Bearer"},  # header를 요구하는 응답을 위한 선택적 인수
            # bearer 값을 포함하는 header
            # bearer token 인증 : bearer 토큰이라는 보안 토큰을 사용해 인증하는 방식
        )
        
        try: # token 생성
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
             # payload : 값이 지정된 딕셔너리로, decode 할 대상 (업데이트)
             # token, 비밀 키, 알고리즘
            username: str = payload.get("sub") # payload : 딕셔너리 형태
            # sub : subject = 키값 => username 

            # jwt 용어 참고
            # https://velog.io/@maintain0404/JWT%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
            
            if username is None:   # is None : object (username) 그 자체를 받아, False 처리함
                raise credentials_exception # raise + 예외처리 이름 (credentials_exception) 
                                                # : 고의적으로 에러를 발생시킴, 
                                                # 뒤에 예외 처리한 401 에러가 나타남
            token_data = TokenData(username=username) # token data = database에 token 저장  
            
        except InvalidTokenError: # jwt 토큰에서 발생한 에러
            raise credentials_exception # 에러 내용 (401 에러)
        
        # username
        user = await self.repository.read_repository_username(username=token_data.username) # data 저장
        
        if user is None: # user 자체를 받아 False 처리함
            raise credentials_exception # 예외 처리
        
        return user # JWT 권한 인증 내용 = user로 반환
#user router
    
# from fastapi.responses import JSONResponse 
# JSONResponse : 
# response(응답)를 커스터마이징(고객의 요구에 따른 대응)하여 전달하고 싶을때, 메세지로 전달
# JSONResponse 설명
# https://velog.io/@rosewwross/Django-JsonResponse

# bson(mongodb) -> json(fast api) 형태로 변형
# json_util 설명
# https://basketdeveloper.tistory.com/entry/Pythonbson%EC%9D%84-json%EC%9C%BC%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EB%B0%A9%EB%B2%95

# bson과 json의 차이점
# https://velog.io/@chayezo/MongoDB-JSON-vs.-BSON

from datetime import timedelta 
from typing import Annotated # 토큰 만료시간
from fastapi import APIRouter, Depends, HTTPException # 의존성 주입, 예외 처리
from fastapi.security import  OAuth2PasswordRequestForm
from app.service.token_service import TokenService # token service
from app.token.utillity import ACCESS_TOKEN_EXPIRE_MINUTES, Token # jwt utillity =>  jwt 발급을 위한 설정
# from fastapi.responses import JSONResponse # router 
# 라우터 참고
# https://wikidocs.net/176226
# from app.repository.user_repository import collection #mongodb client 정보

from app.service.user_service import UserService # user service
from app.model.user import UpUser, UserIn # user model
from app.model.token import Tokens # token model
from fastapi import status


router = APIRouter( #router란 객체는 app = FastAPI와 동일한 효과 (routing)
    prefix="/users", # 경로
    tags=["User"] 
)

service = UserService() # user service 
token_service = TokenService() # token service

# token
jwt = Token() # Json Web Token



## user ##
# 5. 전체 조회 (read)
# @rouetr.get = @app.get 
@router.get("/user/") # get : 조회
            # database 조회로, 필터링이 필요하지 않기에 response_model=UserIn 추가 x
            # 응답 모델 (response model) 참고
            # https://fastapi.tiangolo.com/ko/tutorial/response-model/#response_model_include-response_model_exclude
async def read_user():
    # 비동기 
    return await service.read_service() 
            # 의존성 주입
            
# 6. 일부 조회 (read) - userid
@router.get("/user/{user_id}") # userid = Objectid
async def read_user_userid(user_id: str): # userid로 user 조회
    return await service.read_service_userid(user_id)

# 7. 일부 조회 (read) - email
@router.get("/user/{user_id}/{email}") 
    # 경로 매개변수 순서에 맞게 userid/email로 설정 작업
async def read_user_email(email:str): # email로 user 조회
    return await service.read_service_email(email) 

         
# 회원가입 (JWT 토큰 생성)
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 
# 1. 생성 (create)
# @router.post = @app.post
@router.post("/token/", response_model=UserIn) # post : 생성
  # path parameter (경로 파라미터)
  # token 발급
async def create_user(user: UserIn): # 입력 model UserIn
    # 비동기 
        # query parameter 
    return await service.create_service(user)
        # 의존성 주입

## token ##
# 로그인 (JWT 토큰 인증)
@router.post("/login/", response_model=Tokens) # response_mode : 응답 처리 model
                            # model : Tokens 
                            # 유틸리티 class명이 Token이여서, model명을 Tokens로 변경함
async def login_for_access_token( # 로그인 및 JWT 토큰 인증
            form_data: Annotated[OAuth2PasswordRequestForm, Depends()]): 
                                        # OAuth2PasswordRequestForm : username과 password 값을 얻기 위한 form
    user = await service.read_service_username(form_data.username) # username : user 조회 
    
    # 비밀번호 검증 -> 동기로 처리
    if not user or not token_service.verify_password(form_data.password, user["password"]): 
                                                        # 입력 받은 텍스트 비밀번호와 db에  저장된 비밀번호 일치 유무 검증
                                                    # verify_password 메소드 return값인 pwd_context.verify로 검증 시도함
                                                   
        # raise : 의도적인 에러 발생 
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, # 400 에러 : 잘못된 요청
                                                      # 제공된 입력에 오류가 있거나 관련이 없는 입력인 경우
            # from fastapi import status
            detail="username 또는 password가 올바르지 않습니다.", 
                # client에게 보낼 오류 메세지
            headers={"WWW-Authenticate": "Bearer"}, 
                    # WWW-Authenticate : 인증 정보인 Authenticate 헤더
        )
       
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
                                        # 토큰 만료시간 (30분) 
    # 토큰 생성                                   
    access_token = token_service.create_access_token(
                                        # access token : 
                                        # to_encode: 만료시간, SECRET_KEY: 비밀키, ALGORITHM: 알고리즘    
                user_data={"sub": user["username"]}, # 토큰의 주체 : sub = username 
                expires_delta=access_token_expires # expires_delta : 토큰 만료시간
                )
    
    return {"access_token": access_token, "token_type": "bearer"}
            # 액세스 토큰 : secret key , 토큰 타입 (payload) : bearer
            # bearer 보안 토큰 : jwt 토큰 포함 
    # token router 참고
    # https://databoom.tistory.com/entry/FastAPI-JWT-%EA%B8%B0%EB%B0%98-%EC%9D%B8%EC%A6%9D-6

# 2. 수정 (update)
# @router.put = @app.put //전체 수정
# @routre.patch = @app.patch //일부 수정
@router.put("/user/{user_id}") 
async def update_user(user_id: str, user: UpUser): # 선택값 설정, 기본값 = None
    # 비동기                    
    return await service.update_service(user_id, user)
        # 의존성 주입
# Optional 참고       
# https://zambbon.tistory.com/entry/FastAPI-Query-Parameters-08

# 3. 삭제 (delete)
# @router.delete = @app.delete 
@router.delete("/user/{user_id}") # delete : 삭제
async def delete_user(user_id: str):
    return await service.delete_service(user_id)
    
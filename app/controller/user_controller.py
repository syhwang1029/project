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
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.service.token_service import TokenService
from app.token.utillity import ACCESS_TOKEN_EXPIRE_MINUTES, Token # jwt utillity
# from fastapi.responses import JSONResponse # router 
# 라우터 참고
# https://wikidocs.net/176226
# from app.repository.user_repository import collection #mongodb client 정보

from app.service.user_service import UserService # user service
from app.model.user import UpUser, User, UserIn # user model
from app.model.token import Tokens # token model
from fastapi import status


router = APIRouter( #router란 객체는 app = FastAPI와 동일한 효과 (routing)
    prefix="/users", # 경로
    tags=["User"] 
)

service = UserService() # user service 
token_service = TokenService() # token service
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

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

# 1. 생성 (create)
# @router.post = @app.post
@router.post("/user/", response_model=UserIn) # post : 생성
  # path parameter (경로 파라미터)
async def create_user(user: UserIn): # 입력 model UserIn
    # 비동기 
        # query parameter 
    return await service.create_service(user)
        # 의존성 주입

## token ##
# 로그인 및 토큰 발급 
@router.post("/token/", response_model=Tokens) # response_mode : 응답 처리 model
async def login_for_access_token(
            form_data: Annotated[OAuth2PasswordRequestForm, Depends()]): 
                                        # OAuth2PasswordRequestForm : username과 password 값을 얻기 위한 form
    user = await service.read_service_username(form_data.username, form_data.password) # username : user 조회 
    
    if not user or not await token_service.verify_password(form_data.password, user["passworod"]): 
                                                        # 입력 받은 텍스트 비밀번호와 db에 저장된 비밀번호 일치 유무 검증
                                                    # verify_password 메소드 return값인 pwd_context.verify로 검증 시도함
                                                   
        # raise : 의도적인 에러 발생 
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, # 401 에러 : 해당 user를 찾지 못하거나 비밀번호가 일치하지 않은 경우 
            # from fastapi import status
            detail="username 또는 password가 일치하지 않거나, 해당 user가 존재하지 않습니다.", 
                # client에게 보낼 오류 메세지
            headers={"WWW-Authenticate": "Bearer"}, 
                    # WWW-Authenticate : 인증 정보인 Authenticate 헤더
        )
       
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
                                        # 토큰 만료시간 (30분) 
    # 토큰 생성                                   
    access_token = token_service.create_access_token(
                                       
                user_data={"sub": user["username"]}, # 토큰의 주체 : sub = usernames
                expires_delta=access_token_expires # 토큰 만료시간
                )
    
    return {"access_token": access_token, "token_type": "bearer"}
            # 액세스 토큰, 토큰 타입 : bearer
            # bearer 보안 토큰 : jwt 토큰 포함 
    # token router 참고
    # https://databoom.tistory.com/entry/FastAPI-JWT-%EA%B8%B0%EB%B0%98-%EC%9D%B8%EC%A6%9D-6

# 2. 수정 (update)
# @router.put = @app.put //전체 수정
# @routre.patch = @app.patch //일부 수정
@router.put("/user/{user_id}", response_model=UpUser) 
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


# 이전 참고글
# https://hanseungwan24.tistory.com/entry/Fast-API-%EA%B5%AC%EC%B6%952
    
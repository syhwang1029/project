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

from typing import Optional
from fastapi import APIRouter

# from fastapi.responses import JSONResponse # router 
# 라우터 참고
# https://wikidocs.net/176226
# from app.repository.user_repository import collection #mongodb client 정보

from app.service.user_service import UserService # user service
from app.model.user import UpUser, UserIn, UserOut # user model



router = APIRouter( #router란 객체는 app = FastAPI와 동일한 효과 (routing)
    prefix="/users", # 경로
    tags=["User"]
)

service = UserService() # user service 객체


## user ##
# 5. 전체 조회 (read)
# @rouetr.get = @app.get 
@router.get("/user/") # get : 조회
                    # 태그로 제목 표시
async def read_user():
    # 비동기 
    return await service.read_service()
            # 의존성 주입

# 4. 일부 조회 (read)
@router.get("/user/{user_id}")
async def reat_user_userid(user_id: str):
    # 비동기
    return await service.read_service_userid(user_id)
            # 의존성 주입


# 1. 생성 (create)
# @router.post = @app.post
@router.post("/user/") # post : 생성
  # path parameter (경로 파라미터)
async def create_user(user: UserIn): # 입력 model UserIn
    # 비동기 
        #query parameter 
    return await service.create_service(user)
        # 의존성 주입

# 2. 수정 (update)
# @router.put = @app.put //전체 
# @routre.patch = @app.patch //일부
@router.put("/user/{user_id}") # patch : 일부 수정
async def update_user(user_id: str, user: Optional[UpUser] = None): # 선택값 설정, 기본값 = None
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
    
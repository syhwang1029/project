#user router
    
# from fastapi.responses import JSONResponse 
# JSONResponse : 
# response(응답)를 커스터마이징(고객의 요구에 따른 대응)하여 전달하고 싶을때, 메세지로 전달
# JSONResponse 설명
# https://velog.io/@rosewwross/Django-JsonResponse

from bson import json_util
# bson(mongodb) -> json(fast api) 형태로 변형
# json_util 설명
# https://basketdeveloper.tistory.com/entry/Pythonbson%EC%9D%84-json%EC%9C%BC%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EB%B0%A9%EB%B2%95

# bson과 json의 차이점
# https://velog.io/@chayezo/MongoDB-JSON-vs.-BSON

from fastapi import APIRouter # router 
# 라우터 참고
# https://wikidocs.net/176226
# from app.repository.user_repository import collection #mongodb client 정보
from app.service.user_service import UserService

router = APIRouter( #router란 객체는 app = FastAPI와 동일한 효과 (routing)
    prefix="/users"
)
service = UserService

## user ##
#1. 조회 (read)
# @rouetr.get = @app.get 
@router.get("/user/") # get : 조회
async def read_user():
    return service.read_user()

#2. 생성 (create)
# @router.post = @app.post
@router.post("/user/") # post : 생성
async def create_user(): #dict(딕셔너리) 자료형 => {key:value} 
    return service.create_user()

#3. 수정 (update)
# @router.put = @app.put    
@router.put("/user/{user_id}") # put : 수정
async def update_user(): 
    return service.update_user()

# 4. 삭제 (delete)
# @router.delete = @app.delete 
@router.delete("/user/{user_id}") # delete : 삭제
async def delete_user(user_id : str):
    return service.delete_user()



# 이전 참고글
# https://hanseungwan24.tistory.com/entry/Fast-API-%EA%B5%AC%EC%B6%952
    
# 전체 흐름 : main -> controller(router) -> service -> model -> repository(dao) -> database
from fastapi import FastAPI  #FastAPI 서버 #의존성 주입
import uvicorn #main 함수로 uvicorn 자동 실행 
from app.service import user_service #user 라우팅
                    # import는 디렉토리명으로 해야함


app = FastAPI() #app 인스턴스에 FastAPI 서버 할당


# ### route (end point) ###
# # (특정) HTTP protocol : post(생성)/get(읽기)/put(수정)/delet(삭제)
# # --> 경로와 통신

# # 일반 HTTP 테스트
# # 경로 작동 데코레이터 : 경로 /의 get 작동
# @app.get("/") #uvicorn 테스트용 #/: 경로, get: 작동(route) 사용
# def read_root(): #비동기
#     return {"Hello": "World"} #pydantic 모델 반환 가능

# # 특정 HTTP 텍스트
# @app.get("items/{item_id}") # 경로 매개변수 (path parameter)
# # async def read_item(item_id): # -> 함수 매개변수에 전달
# async def read_item(item_id: int): # 타입형 -> 데이터 변환 (디버깅)
# # 동기
# # async def read_user_item(item_id: str, needy: str) # query parameter 
# # None : 기본값
#     return {"item_id": item_id}

## user ##
app.include_router(user_service.router)

### FastAPI 서버 ####
if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run(app, host="0.0.0.0", port=1203)

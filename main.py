# 전체 흐름 : main <- controller(router/domain) <- service <- repository(dao) <- (model) <- database(mongodb)
from fastapi import FastAPI  # FastAPI 서버 #의존성 주입
import uvicorn #main 함수로 uvicorn 자동 실행 
from app.controller import user_controller  # user routing
                    # import는 디렉토리명으로 해야함
from app.controller import board_controller # board routing

app = FastAPI() #app 인스턴스에 FastAPI 서버 할당


### route (endpoint) ###
# HTTP protocol : post(생성)/get(읽기)/put(수정)/delet(삭제) 
# => CRUD

## user ##
app.include_router(user_controller.router)

## board ##
app.include_router(board_controller.router)


### FastAPI ####
if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run(app, host="0.0.0.0", port=1203)
# 전체 흐름 : main <- controller(router/domain) <- service <- repository(dao) <- (model) <- database(mongodb)
from fastapi import FastAPI  # FastAPI 프레임워크 
import uvicorn # uvicorn 라이브러리 서버 

from app.controller import user_controller, board_controller, comment_controller, reply_controller
# import = 디렉토리명
# controller = router(crud)
# user (사용자), board (게시판), comment (댓글), reply (대댓글)

# FastAPI의 핵심 
app = FastAPI() 


### route (endpoint) ###
# HTTP protocol : post(생성)/get(읽기)/put(수정)/delet(삭제) 

# routing (CRUD) : 경로 연산
# 사용 이유 : 코드의 가독성과 유지 관리 향상, 
# 대규모 애플리케이션의 구조를 더욱 명확하게 정의함

## 1. user ##
app.include_router(user_controller.router)
## 2. board ## 
app.include_router(board_controller.router)
## 3. comment ##
app.include_router(comment_controller.router)
## 4. reply ##
app.include_router(reply_controller.router)


### FastAPI ####
if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run("main:app", host="0.0.0.0", port=1203, reload=True)
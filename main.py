# 전체 흐름 : main <- controller(router/domain) <- service <- repository(dao) <- (model) <- database(mongodb)
from fastapi import FastAPI  # FastAPI 프레임워크 
import uvicorn # uvicorn 라이브러리 서버 

from app.controller import user_controller, board_controller, comment_controller  
# import = 디렉토리명
# controller = router(crud)
# user (사용자), board (게시판), comment (댓글)

# FastAPI() 
app = FastAPI() 


### route (endpoint) ###
# HTTP protocol : post(생성)/get(읽기)/put(수정)/delet(삭제) 

# CRUD
## 1. user ##
app.include_router(user_controller.router)
## 2. board ##
app.include_router(board_controller.router)
## 3. comment ##
app.include_router(comment_controller.router)


### FastAPI ####
if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run("main:app", host="0.0.0.0", port=1203, reload=True)
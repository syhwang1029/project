from typing import Union
from fastapi import FastAPI  #FastAPI 서버
from app.controller.user_controller import UserController #mongodb와 FastAPI 연동용 컨트롤러

import uvicorn #main 함수로 uvicorn 자동 실행 


app = FastAPI() #app 이란 변수에 FastAPI 서버 할당

user_controller = UserController() #mongobd 연결용 컨트롤러

@app.get("/") #uvicorn 테스트용
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") #path prameter #uvicorn 테스트용
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/") #mongodb 테스트용
def test():
    return{"test keys":"tes values"}

@app.post("/test") #mongodb 연결용 컨트롤러
async def test():
    test = await user_controller.test()
    return test

if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run(app, host="0.0.0.0", port=1203) #uvicorn  
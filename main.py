from typing import Union

from fastapi import FastAPI #FastAPI 서버
import uvicorn #main 함수로 uvicorn 자동 실행 

app = FastAPI()


@app.get("/") #기본
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}") #path prameter
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__": # FastAPI 서버 
    uvicorn.run(app, host="0.0.0.0", port=1203) #uvicorn  
# main -> controller -> service -> model -> repository-> database
from typing import Union 
from fastapi import FastAPI  #FastAPI 서버
import uvicorn #main 함수로 uvicorn 자동 실행 

from app.mongodb.mongodb import MongoClient #MongoDB Client전용 URI 


### app ###
app = FastAPI() #app 이란 변수에 FastAPI 서버 할당
mongocilent = MongoClient() #MongoDB 


### URL ###
@app.get("/") #uvicorn 테스트용
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") #path prameter #uvicorn 테스트용
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



### FastAPI 서버 ####
if __name__ == "__main__": # FastAPI 서버 자동 실행
    uvicorn.run(app, host="0.0.0.0", port=1203) #uvicorn 
    uvicorn.run(mongocilent) # MongoDB connetcion URI 연결

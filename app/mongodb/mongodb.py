from pymongo import MongoClient
# pymongo로 FastAPI와 MongoDB 동기적 연결 
# 참고
# https://blog.poespas.me/posts/2024/05/29/fastapi-mongodb-crud-with-pymongo/

MONGO_URI = "mongodb://localhost:27017/" # MongoDB Client 전용 URI 
client = MongoClient(MONGO_URI )# MongoDB Client 생성 
# -> 각 db는 repository에서 선택함

# 그외 참고 
# mongodb 연결
# 1. database 가져오기
# db = client["db_name"] 
# 2. collection 가져오기
# collection = db["collection_name"]
# mongodb 연결 참조
# https://it-creamstory.tistory.com/entry/Python-MongoDB-connect-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0
# https://wooiljeong.github.io/python/mongodb-01/
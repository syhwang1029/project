from pymongo import MongoClient # MongoDB 연동
# pymongo 동기적 연결 
# https://wooiljeong.github.io/python/mongodb-01/ 

# MongoDB Connection 연결
# MongoDB Client 전용 URI
mongodb_uri = "mongodb://localhost:27017/"
client = MongoClient(mongodb_uri)

db = client #mongodb uri를 db 객체에 저장
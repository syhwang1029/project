from pymongo import MongoClient # MongoDB 연동
# pymongo 동기적 연결 
# https://wooiljeong.github.io/python/mongodb-01/ 

# MongoDB Connection 연결
# MongoDB Client 전용 URI

# MongoDB 클라이언트 생성
def create_mongo_client(host='localhost', port=27017):
    client = MongoClient(host, port)
    return client
# mongodb_uri = "mongodb://localhost:27017/"
#client = MongoClient(mongodb_uri)

#database와 collection 선택
def get_database(client, datanase):
    db = client[datanase]
    return db

# db = client["database"] #db 선택
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# user_collection = db["user"] #collection 선택

#mongodb 연결
# 1. database 가져오기
# db = client["db_name"] 
# 2. collection 가져오기
# collection = db["collection_name"]
# mongodb 연결 참조
# https://it-creamstory.tistory.com/entry/Python-MongoDB-connect-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0

# 문서 삽입(insert)
def insert_user(collection, user):
    collection.insert_one(user)

# 문서 검색(find)    
def find_user(collection, query):
    user = collection.find_one(query)
    return user
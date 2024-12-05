from pymongo import MongoClient # MongoDB 연동

# MongoDB connetcion 연결
# MongoDB Client 전용 URI
mongodb_uri = "mongodb://localhost:27017/"
client = MongoClient(mongodb_uri)
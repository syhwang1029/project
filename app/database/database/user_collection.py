from app.mongodb.mongodb import client # mongodb cilent 정보

# user collection 
db = client["database"] # user database 선택
collection = db["user"] # user collection 선택
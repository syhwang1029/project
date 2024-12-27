from app.mongodb.mongodb import client # mongodb cilent

# comment collection
db = client["database"] # comment database 선택
collection = db["comment"] # comment collection 선택

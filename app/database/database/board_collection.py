from app.mongodb.mongodb import client

db = client["database"] # board database 선택
collection = db["board"] # board collection 선택
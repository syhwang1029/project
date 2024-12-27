from app.mongodb.mongodb import client # mongodb cilent

# reply mongodb
db = client["database"] # reply database 선택
collection = db["reply"] # reply collection 선택
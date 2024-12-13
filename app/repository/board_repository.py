from app.mongodb.mongodb import client #mongodb cilent 연결
from app.model.board import Board # board model
# crud 참고 1
# https://dev.to/programadriano/python-3-fastapi-mongodb-p1j

# crud 참고 2
# https://jay-ji.tistory.com/86

# board mongodb
db = client["database"] # board database 선택 
collection = db["user"] # board collection 선택

        
# 게시판
# board repository
class BoardRepository:   
        
    #1. 생성 (create)
    async def create_repository(self, data: dict): #dict = {key, value}
            datas = collection.insert_one(data) #monnodb data insert 명령어
            return str(datas.inserted_id) #datas => ObjectId 자동 생성    
         
        # insert_id 참고
        # https://stackoverflow.com/questions/8783753/how-to-get-the-object-id-in-pymongo-after-an-insert
    
    
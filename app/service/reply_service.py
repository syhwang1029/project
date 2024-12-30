from app.repository.reply_repository import ReplyRepository # reply repository
# import : 디렉토리명
from app.model.reply import Reply, ReplyUpdate # repositoty model

# reply service
class ReplyService:
    def __init__(self):
        self.repository = ReplyRepository() # reply repository
        
    # 1. 생성 (create) 
    async def crate_service(self, reply: Reply): # reply 생성
        return await self.repository.creat_repository(reply)
       
    # 5. 일부 조회 (read) - replyid
    async def read_service_replyid(self, reply_id: str): # reply id로 일부 reply의 data 조회
        return await self.repository.read_repository_replyid(reply_id)
    
    # 4. 전체 조회 (read)
    async def read_service(self): # relpy의 data 전체 조회
        return await self.repository.read_repository()
    
    # 2. 수정 (update)
    async def update_service(self, reply_id: str, reply: ReplyUpdate): # reply id로 reply의 data 수정
        return await self.repository.update_repository(reply_id, reply)
    
    # 3. 삭제 (delete)
    async def delete_service(self, reply_id: str): # relpy idfh reply 삭제
        return await self.repository.delete_repository(reply_id)
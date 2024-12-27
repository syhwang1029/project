from app.repository.comment_repository import CommentRepositoty # comment repository
from app.model.comment import Comment, CommentUpdate # comment model

# comment service
class CommentService:
    def __init__(self):
        self.repository = CommentRepositoty() # comment repository
        
# 1. 생성 (create)
    async def create_service(self, comment: Comment):
        return await self.repository.create_repository(comment)
    
# 4. 전체 조회 (read) 
    async def read_service(self): 
        return await self.repository.read_repository()   
 
# 5. 일부 조회 (read) - comment id
    async def read_service_commentid(self, comment_id: str):
        return await self.repository.read_repository_commentid(comment_id)
 

    
# 2. 수정 (update)
    async def update_service(self, comment_id: str, comment: CommentUpdate):
        return await self.repository.update_repositoty(comment_id, comment)
    
# 3. 삭제 (delete)
    async def delete_service(self, comment_id: str):
        return await self.repository.delete_repository(comment_id)
    
    



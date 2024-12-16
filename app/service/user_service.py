from typing import List
from app.repository.user_repository import UserRepository # user repository
from app.model.user import UserIn, UserOut # user model 

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        self.repository = UserRepository()
    
    # 5. 전체 조회 (read)
    async def read_service(self): # 조회
        # 비동기 
        return await self.repository.read_repository()
                # 의존성 주입
                
    # 4. 일부 조회 (read)
    async def read_service_userid(self, user_id: str):
        # 비동기
        return await self.repository.read_repository_userid(user_id)
                    # 의존성 주입
    
    
    # 1. 생성 (create)    
    # 비동기
    async def create_service(self, user: UserIn): # 입력 model UserIn
        user = dict(user) # user : dict
        return await self.repository.create_repository(user) 
            # 의존성 주입
                    
    # 3. 수정 (uodate)
    async def update_service(self, user_id: str, user: UserIn): # 입력 model UserIn
        # 비동기  
        user = dict(user) # user : dict
        return await self.repository.update_repository(user_id, user)
            # 의존성 주입
    
    # 4. 삭제 (delete)
    async def delete_service(self, user_id: str): 
        # 비동기 
        return await self.repository.delete_repository(user_id)
            # 의존성 주입
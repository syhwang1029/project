from app.repository.user_repository import *
from app.model.user import User

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        self.user_repository = UserRepository()
    
    # 1. 생성 (create)    
    def create_service(self, user: str):
        user = dict(user)
        return self.user_repository.create_repository(user)
    
    # def read_service(self): # 조회
    #     return self.user_repository.read_repository()
    
    # 3.  수정 (uodate)
    def update_service(self, user_id: str, user: User): 
        userd = dict(user) # user : dict
        return self.user_repository.update_repository(user_id, user)
    
    # def delete_service(self, user_id): # 삭제
    #     return self.user_repository.delete_repository(user_id)
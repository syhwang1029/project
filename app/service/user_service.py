from app.repository.user_repository import *
from app.model.user import *

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        self.user_repository = UserRepository()
        
    def create_user(self): # 생성
        return self.user_repository.create_user(User)
    
    def read_user(self): # 조회
        return self.user_repository.read_user(User)
    
    def update_user(self): # 수정
        return self.user_repository.update_user(UserUpdate)
    
    def delete_user(self): # 삭제
        return self.user_repository.delete_user(UserDelete)
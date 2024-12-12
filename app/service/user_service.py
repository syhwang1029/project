from app.repository.user_repository import *

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        self.user_repository = UserRepository()
        
    def create_user(self, user_data): # 생성
        return self.user_repository.create_user(user_data)
    
    def read_user(self): # 조회
        return self.user_repository.read_user()
    
    def update_user(self, user_data): # 수정
        return self.user_repository.update_user(user_data)
    
    def delete_user(self, user_id): # 삭제
        return self.user_repository.delete_user(user_id)
from app.repository.user_repository import *

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        self.user_repository = UserRepository()
        
    def create_service(self, user_data): # 생성
        return self.user_repository.create_repository(user_data)
    
    def read_service(self): # 조회
        return self.user_repository.read_repository()
    
    def update_service(self, user_id): # 수정
        return self.user_repository.update_repository(user_id)
    
    def delete_service(self, user_id): # 삭제
        return self.user_repository.delete_repository(user_id)
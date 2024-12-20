from app.repository.user_repository import UserRepository # user repository
from app.model.user import UpUser, UserIn, UserOut  # user model 
from app.token.utillity import Token # jwt utillity

# service 의존성 주입 참고 
# https://the-boxer.tistory.com/63

# user service
class UserService:
    def __init__(self): # service가 repository에 의존
        # init :  class가 호출될 때, 자동으로 사용되는 함수 
        # self : 객체의 인스턴스 그 자체
        self.repository = UserRepository() # user repository
        # repositor가 자기 자신을 참조하는 매개변수 
        # init 함수와 self 함수의 설명 
        # https://www.google.com/search?q=__init__+%ED%95%A8%EC%88%98+%EC%97%AD%ED%95%A0&oq=__init__+%ED%95%A8%EC%88%98+%EC%97%AD%ED%95%A0&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigAdIBCjE2MDIzajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8
        
        self.jwt = Token() # token repository
        
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
    async def create_service(self, user: UserIn): # 입력 model UserIn\        
        user = dict(user) # user : dict
        return await self.repository.create_repository(user) 
            # 의존성 주입
            # jwt 참조
            # https://velog.io/@osj1405/FastAPI-보안 
                    
    # 2. 수정 (update)
    async def update_service(self, user_id: str, user: UpUser): # 입력 model UserIn
        # 비동기  
        user = dict(user)
        return await self.repository.update_repository(user_id, user)
            # 의존성 주입
    
    # 3. 삭제 (delete)
    async def delete_service(self, user_id: str): 
        # 비동기 
        return await self.repository.delete_repository(user_id)
            # 의존성 주입
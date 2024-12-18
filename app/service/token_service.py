# token service
from typing import Annotated

from fastapi import Depends
from app.repository.token_repository import TokenRepository
from fastapi.security import OAuth2PasswordBearer
from app.model.user import User
        
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

# token service
class TokenService:
    def __init__(self):
        self.repository = TokenRepository()
   
    
    def fake_decode_token(self, token):
            return User( username = token + "fakedecoded",  
                         email="john@example.com" )
                   
    async def get_crrent_uer(self, token: Annotated[str, Depends(oauth2_scheme)]):
        user = fake_decode_token(token)
        return user
    
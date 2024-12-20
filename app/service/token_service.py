import stat
from typing import Annotated
from fastapi import Depends, HTTPException 
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError # error
import jwt # jwt import
from app.model.token import TokenData # token data model
from app.repository.token_repository import TokenRepository # token repository
from app.token.utillity import Token # token
from app.token.utillity import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM  # jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# token service
class TokenService:
    def __init__(self):
        self.repository = TokenRepository()
        self.jwt = Token() # token
        
# 종속성 업데이트
# 현재 user 정보
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # asuth2 
    
    credentials_exception = HTTPException( # 예외 처리 
        status_code=stats.HTTP_401_UNAUTHORIZED, # 401 error
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # jwt decode : token, 비밀키, 알고리즘
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        username: str = payload.get("sub") # username
        
        if username is None:
            
            raise credentials_exception # token data
        token_data = TokenData(username=username)
        
    except InvalidTokenError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username=token_data.username)
    
    if user is None:
        raise credentials_exception
    return user
         
from passlib.context import CryptContext # bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 일반 텍스트 비밀번호 hashing
def hash_password(password : str):
    return pwd_context.hash(password)

# 비밀번호 검증
def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)
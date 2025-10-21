from datetime import datetime, timedelta
from jose import jwt, JWTError
import os



SECRET_KEY = os.getenv("SECRET_KEY", "say_my_name")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE", "60"))

def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    to_encode = {"sub": subject}
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    try:
        return  jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        raise ValueError(f'Invalid token: {e}')
from fastapi import HTTPException , status
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# loads the env variables
load_dotenv()

# get the env vars os.getenv returns str
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXP = int(os.getenv("ACCESS_TOKEN_EXP"))


pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

# verify helper for login
def verify_password(plain_pass , hashed_pass):
    return pwd_context.verify(plain_pass , hashed_pass)

# hashing pass for register
def hash_password(plain_pass):
    return pwd_context.hash(plain_pass)


# gen access token when login
def create_access_token(data : dict):
    to_encode = data.copy()
    exp = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXP)
    to_encode.update({"exp" : exp})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return encoded_jwt



def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        return None


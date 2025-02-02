from pydantic import BaseModel , EmailStr

class UserCreate(BaseModel):
    user_name : str
    email : EmailStr
    password : str

class User(BaseModel):
    user_name : str
    email : EmailStr
    hashed_password : str



    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token : str
    token_type : str

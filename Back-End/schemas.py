import datetime
from pydantic import BaseModel , EmailStr


class User(BaseModel):
    user_name : str
    email : EmailStr
    hashed_password : str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token : str
    token_type : str

class Resume(BaseModel):
    resume_id = int
    user_name:str
    file_path:str
    uploaded_at: datetime.datetime
    format:str
    original_name:str

    class Config:
        orm_mode = True










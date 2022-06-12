import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool 
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str
    is_company: bool = False
    
    
    @validator('password2')
    def password_match(cls, pwd, values, **kwargs):
        if 'password' in values and pwd != values['password']:
            raise ValueError('password do not match.')
        return pwd
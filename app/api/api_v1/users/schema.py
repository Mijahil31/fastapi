from pydantic import BaseModel

class UserCreate(BaseModel):
    
    name: str
    document: str
    email: str
    password: str
    is_active: bool = True

    class Config:
        orm_mode = True

class UserBy(BaseModel):

    email: str
    password: str

    class Config:
        orm_mode = True
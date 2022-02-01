from datetime import datetime
from pydantic import BaseModel

class UserResponse(BaseModel):

    id: int
    name: str
    document: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

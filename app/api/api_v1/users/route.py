from typing import List
from app.api.api_v1.api import router
from .dto import UserResponse
from .schema import UserCreate
from .controller import *


# Rutas del User
@router.get("/user/{id}", response_model=UserResponse, tags=["Usuario"])
def get_user(id: int):
    return getById(id)

@router.get("/user/", response_model=List[UserResponse], tags=["Usuario"])
def get_all():
    return getAll()

@router.post('/user/', response_model=UserResponse, tags=["Usuario"])
def post_create_user(user:UserCreate):
    return createUser(user=user)

@router.post("/user/by", response_model=UserResponse, tags=["Usuario"])
def post_user_by(user: UserBy):
    return getBy(user=user)
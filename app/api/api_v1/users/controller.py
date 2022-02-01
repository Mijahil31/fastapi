from .schema import UserBy, UserCreate
from .dao import *

def getById(id: int):
    try:
        return get_by_id(id=id)
    except Exception as err:
        print(err)


def getAll():
    try:
        return get_all()
    except Exception as err:
        print(err)


def getBy(user: UserBy):
    try:
        return get_by(user=user)
    except Exception as err:
        print(err)


def createUser(user: UserCreate):
    try:
        return post_create_user(user=user)
    except Exception as err:
        print(err)
from fastapi import APIRouter, Depends
from ..Services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/")
def getUsername():
    return user_service.getUsername()

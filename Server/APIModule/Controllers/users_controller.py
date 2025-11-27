from fastapi import APIRouter, Depends

from Server.APIModule.DTOs import LoginRequest, RegistrationRequest, ApiResult
from ..Services.user_service import UserService
from fastapi import Body

router = APIRouter()
user_service = UserService()

@router.post("/")
def test():
    return  ""

#@router.post("/login")
#def login_user(loginRequest: LoginRequest = Body(...))-> ApiResult:
    #return user_service.login_user(loginRequest)

##@router.post("/register")
#def register_user(registrationRequest: RegistrationRequest = Body(...)) -> ApiResult:
#    return user_service.register_user(registrationRequest)

#@router.post("/updateUsername")
#def update_username(oldUsername: str, newUsername: str) -> ApiResult:
    #return user_service.update_username(oldUsername, newUsername)

#@router.post("/updatePassword")
#def update_password(username: str, newPassword: str) -> ApiResult:
#    return user_service.update_password(username, newPassword)

from ..Interfaces.iuser_service import IUserService
from ..DTOs import RegistrationRequest, LoginRequest, ApiResult
from ...DBModule.db_service import DBService

class UserService(IUserService):
    dbService = DBService()

    def login_user(self, loginRequestDTO: LoginRequest) -> ApiResult:
        return ApiResult.ok()

    def register_user(self, registrationRequestDTO: RegistrationRequest) -> ApiResult:
        return ApiResult.ok()

    def update_username(self, oldUsername: str, newUsername: str) -> ApiResult:
        return ApiResult.ok()

    def update_password(self, username: str, newPassword: str) -> ApiResult:
        return ApiResult.ok()
    
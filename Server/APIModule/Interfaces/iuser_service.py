from abc import ABC, abstractmethod
from ..DTOs import RegistrationRequest, LoginRequest, ApiResult

class IUserService(ABC):
    @abstractmethod
    def login_user(self, loginRequestDTO: LoginRequest) -> ApiResult:
        pass

    @abstractmethod
    def register_user(self, registrationRequestDTO: RegistrationRequest) -> ApiResult:
        pass

    @abstractmethod
    def update_username(self, oldUsername: str, newUsername) -> ApiResult:
        pass

    @abstractmethod
    def update_password(self, username: str, newPassword: str) -> ApiResult:
        pass
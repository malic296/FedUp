from ..Interfaces.iuser_service import IUserService

class UserService(IUserService):
    def getUsername(self):
        return "test"
    
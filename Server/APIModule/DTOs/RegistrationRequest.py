from pydantic import BaseModel

class RegistrationRequest(BaseModel):
    username: str
    email: str
    password: str
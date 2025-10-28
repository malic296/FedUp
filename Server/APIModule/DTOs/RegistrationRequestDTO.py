from pydantic import BaseModel

class RegistrationRequestDTO(BaseModel):
    username: str
    email: str
    password: str
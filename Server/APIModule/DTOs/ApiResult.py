from pydantic import BaseModel
from typing import Optional

class ApiResult(BaseModel):
    success: bool
    message: Optional[str] = None
    
    @classmethod
    def ok(cls):
        return cls(success=True, message=None)

    @classmethod
    def wrong(cls, message: str):
        return cls(success=False, message=message)

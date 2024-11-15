from pydantic import BaseModel


class DoRequest(BaseModel):
    message: str

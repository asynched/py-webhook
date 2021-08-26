from pydantic import BaseModel


class UserType(BaseModel):
    name: str
    email: str
    password: str

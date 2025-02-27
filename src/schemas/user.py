from pydantic import BaseModel


class CreateUserSerializer(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class LoginSerializer(BaseModel):
    username: str
    password: str

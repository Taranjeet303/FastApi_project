from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True
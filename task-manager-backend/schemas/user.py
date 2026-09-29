
from pydantic import BaseModel, Field

from schemas.task import TaskSimpleResponse

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=72)

class UserResponse(BaseModel):
    id: int
    username: str
    tasks: list[TaskSimpleResponse] = Field(default_factory=list)

    model_config = {"from_attributes": True}

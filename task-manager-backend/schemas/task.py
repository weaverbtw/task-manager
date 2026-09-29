
from pydantic import BaseModel, Field

from datetime import datetime

class TaskCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)

class TaskUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)

class TaskResponse(BaseModel):
    id: int
    name: str
    completed: bool
    created_at: datetime

    model_config = {"from_attributes": True}

class TaskSimpleResponse(BaseModel):
    id: int
    name: str
    completed: bool

    model_config = {"from_attributes": True}

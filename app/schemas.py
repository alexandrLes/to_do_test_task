from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    datetime_to_do: datetime
    task_info: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDB(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

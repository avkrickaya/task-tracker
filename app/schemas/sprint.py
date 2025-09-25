# app/schemas/sprint.py
# Схемы для спринтов

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SprintBase(BaseModel):
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class SprintCreate(SprintBase):
    pass

class SprintOut(SprintBase):
    id: int

    class Config:
        orm_mode = True

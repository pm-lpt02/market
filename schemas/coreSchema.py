from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class IDModelMixin(BaseModel):
    id: int

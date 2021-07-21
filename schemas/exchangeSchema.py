from typing import Optional
from schemas.coreSchema import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel


class ExchangeBase(BaseModel):
    name: str
    country: Optional[str]
    abrv: Optional[str]
    city: Optional[str]
    open_time: Optional[str]
    close_time: Optional[str]


class Exchange(ExchangeBase):
    class Config():
        orm_mode = True


class ExchangeInDB(ExchangeBase, DateTimeModelMixin, IDModelMixin):
    class Config():
        orm_mode = True


class ExchangeCreate(BaseModel):
    name: str
    abrv: str
    country: Optional[str]
    city: Optional[str]

    class Config():
        orm_mode = True


class ExchangeDetail(BaseModel):
    name: str
    abrv: str
    country: Optional[str]
    city: Optional[str]
    open_time: Optional[str]
    close_time: Optional[str]

    class Config():
        orm_mode = True


class ExchangeView(BaseModel):
    name: str

    class Config():
        orm_mode = True


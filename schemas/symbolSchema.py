from typing import Optional
from pydantic import BaseModel
from schemas.coreSchema import DateTimeModelMixin, IDModelMixin
from datetime import datetime


class SymbolBase(BaseModel):
    symbol: str
    active: Optional[bool]


class Symbol(SymbolBase):
    class Config():
        orm_mode = True


class SymbolInDB(Symbol, DateTimeModelMixin, IDModelMixin):
    active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config():
        orm_mode = True


class SymbolView(BaseModel):
    symbol: str


class SymbolCreate(BaseModel):
    symbol: str

    class Config():
        orm_mode = True


class SymbolUpdate(BaseModel):
    symbol: Optional[str]
    active: Optional[bool]

    class Config():
        orm_mode = True


class SymbolAPIJoin(IDModelMixin):
    class Config():
        orm_mode = True


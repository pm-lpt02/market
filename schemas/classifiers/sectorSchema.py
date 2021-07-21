from typing import List
from pydantic import BaseModel


class SectorBase(BaseModel):
    sector_id: int
    sector: str


class Sector(SectorBase):
    class Config():
        orm_mode = True


class ViewSector(BaseModel):
    sector: str

    class Config():
        orm_mode = True


class SectorDetail(BaseModel):
    from .ingroupSchema import ViewIndGroup
    sector_id: int
    sector: str
    industrygroups: List[ViewIndGroup] = []

    class Config():
        orm_mode = True

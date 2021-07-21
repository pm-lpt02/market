from typing import Optional
from pydantic import BaseModel


class SubIndustryBase(BaseModel):
    subindustry_id: int
    subindustry: str
    description: Optional[str]
    industry: Optional[int]


class SubIndustry(SubIndustryBase):
    class Config():
        orm_mode = True


class ViewSubIndustry(BaseModel):
    subindustry: str
    subindustry_description: Optional[str]

    class Config():
        orm_mode = True


class SubIndustryDetail(BaseModel):
    from .industrySchema import ViewIndustry
    subindustry_id: int
    subindustry: str
    subindustry_description: Optional[str]
    industry: ViewIndustry

    class Config():
        orm_mode = True


class SubIndustryDB(SubIndustryBase):
    description: str
    industryDB_id: int

    class Config():
        orm_mode = True

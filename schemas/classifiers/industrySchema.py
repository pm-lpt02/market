from typing import List, Optional
from pydantic import BaseModel


class IndustryBase(BaseModel):
    industry_id: int
    industry: str
    industryGroup: Optional[int]


class Industry(IndustryBase):
    class Config():
        orm_mode = True


class ViewIndustry(BaseModel):
    industry: str

    class Config():
        orm_mode = True


class IndustryDetail(BaseModel):
    from .ingroupSchema import ViewIndGroup
    from .subindustSchema import ViewSubIndustry
    industry_id: int
    industry: str
    industry_group: ViewIndGroup
    subindustries: List[ViewSubIndustry] = []

    class Config():
        orm_mode = True


class IndustryDB(IndustryBase):
    industrygroupDB_id: int

    class Config():
        orm_mode = True


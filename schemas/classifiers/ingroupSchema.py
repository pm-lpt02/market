from typing import List, Optional
from pydantic import BaseModel


class IndustryGroupBase(BaseModel):
    industrygroup_id: int
    industryGroup: str
    sector: Optional[int]


class IndustryGroup(IndustryGroupBase):
    class Config():
        orm_mode = True


class ViewIndGroup(BaseModel):
    industryGroup: str

    class Config():
        orm_mode = True


from .industrySchema import ViewIndustry
class IndustryGroupDetail(BaseModel):
    from .sectorSchema import ViewSector
    industrygroup_id: int
    industrygroup : str
    sector: ViewSector
    industries: List[ViewIndustry] = []

    class Config():
        orm_mode = True


class IndustryGroupDB(IndustryGroupBase):
    sector_id: int

    class Config():
        orm_mode = True

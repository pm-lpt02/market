from sqlalchemy import Column, Integer, String, ForeignKey
from databases import Base
from sqlalchemy.orm import relationship


class Sector(Base):
    __tablename__ = 'sectors'

    id = Column(Integer, primary_key=True, index=True)
    sector_id = Column(Integer, nullable=False)
    sector = Column(String)

    industryGroups = relationship('IndustryGroup', back_populates="sector")


class IndustryGroup(Base):
    __tablename__ = 'industryGroups'

    id = Column(Integer, primary_key=True, index=True)
    industrygroup_id = Column(Integer, nullable=False)
    industrygroup = Column(String)
    sectorDB_id = Column(Integer, ForeignKey('sectors.id'))

    sector = relationship("Sector", back_populates="industryGroups")
    industries = relationship('Industry', back_populates="industry_group")


class Industry(Base):
    __tablename__ = 'industries'

    id = Column(Integer, primary_key=True, index=True)
    industry_id = Column(Integer, nullable=False)
    industry = Column(String)
    industrygroupDB_id = Column(Integer, ForeignKey('industryGroups.id'))

    industry_group = relationship("IndustryGroup", back_populates="industries")
    subindustries = relationship('SubIndustry', back_populates="industry")


class SubIndustry(Base):
    __tablename__ = 'subIndustries'

    id = Column(Integer, primary_key=True, index=True)
    subindustry_id = Column(Integer, nullable=False)
    subindustry = Column(String)
    subindustry_description = Column(String)
    industryDB_id = Column(Integer, ForeignKey('industries.id'))

    industry = relationship("Industry", back_populates="subindustries")

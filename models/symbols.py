from sqlalchemy import Column, Integer, String, DateTime, Boolean
from databases import Base
from datetime import datetime


class Symbol(Base):
    __tablename__ = 'symbols'

    Id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

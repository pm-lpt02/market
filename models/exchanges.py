from sqlalchemy import Column, Integer, String, DateTime
from databases import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Exchange(Base):
    __tablename__ = 'exchanges'

    Id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    abrv = Column(String, nullable=True)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    open_time = Column(String, nullable=True)
    close_time = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

from sqlalchemy.orm import Session
from models.gics import Sector
from schemas.classifiers import sectorSchema
from fastapi import HTTPException, status


def get_all(db: Session):
    sectors = db.query(Sector).all()
    return sectors


def create(request: sectorSchema.Sector, db: Session):
    new_sector = Sector(sector_id=request.sector_id, sector=request.sector)
    db.add(new_sector)
    db.commit()
    db.refresh(new_sector)
    return new_sector


def show(id: int, db: Session):
    sector = db.query(Sector).filter(Sector.id == id).first()
    if not sector:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"sector with id: {id} is not available"
        )

    return sector

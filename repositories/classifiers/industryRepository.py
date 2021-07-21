from sqlalchemy.orm import Session
from models.gics import Industry, IndustryGroup
from schemas.classifiers import industrySchema
from fastapi import HTTPException, status


def get_all(db: Session):
    industries = db.query(Industry).all()
    return industries


def create(request: industrySchema.Industry, db: Session):
    new_industry = Industry(
        industry_id=request.industry_id,
        industry=request.industry,
        industGroup=IndustryGroup.id
    )
    db.add(new_industry)
    db.commit()
    db.refresh()
    return new_industry


def show(id: int, db: Session):
    industry = db.query(Industry).filter(Industry.id == id).first()
    if not industry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Industry with id: {id} is not available"
        )
    return industry


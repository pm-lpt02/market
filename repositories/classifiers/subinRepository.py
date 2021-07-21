from sqlalchemy.orm import Session
from models.gics import SubIndustry, Industry
from schemas.classifiers import subindustSchema


def get_all(db: Session):
    subindustries = db.query(SubIndustry).all()
    return subindustries


def create(request: subindustSchema.SubIndustry, db: Session):
    new_subin = SubIndustry(
        subindustry_id=request.subindustry_id,
        subindustry=request.subindustry,
        description=request.description,
        industry=Industry.id
    )
    db.add(new_subin)
    db.commit()
    db.refresh()
    return new_subin


from sqlalchemy.orm import Session
from models.gics import IndustryGroup, Sector
from schemas.classifiers import ingroupSchema
from fastapi import HTTPException, status


def get_all(db: Session):
    industrygroups = db.query(IndustryGroup).all()
    return industrygroups


def create(request: ingroupSchema.IndustryGroup, db: Session):
    new_ingroup = IndustryGroup(industrygroup_id=request.industrygroup_id,
                                industrygroup=request.industryGroup,
                                sector=Sector.id
                                )
    db.add(new_ingroup)
    db.commit()
    db.refresh(new_ingroup)
    return new_ingroup


def show(id: int, db:Session):
    ingroup = db.query(IndustryGroup).filter(IndustryGroup.id == id).first()
    if not ingroup:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Industry Group with id: {id} is not available"
        )
    return ingroup


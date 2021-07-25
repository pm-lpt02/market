from sqlalchemy.orm import Session
from models.symbols import Symbol
from schemas import symbolSchema
from fastapi import HTTPException, status
from datetime import datetime


def get_all(db: Session):
    symbols = db.query(Symbol).all()
    return symbols


def create(request: symbolSchema.Symbol, db: Session):
    new_symbol = Symbol(symbol=request.symbol)
    new_symbol.active=True
    new_symbol.created_at=datetime.utcnow()
    new_symbol.updated_at=datetime.utcnow()

    db.add(new_symbol)
    db.commit()
    db.refresh(new_symbol)
    return new_symbol


def show(id: int, db: Session):
    symbol = db.query(Symbol).filter(Symbol.Id == id).first()
    if not symbol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"symbol with id: {id} is not available"
        )

    return symbol


def update(id: int, request: symbolSchema.Symbol, db: Session):
    symbol = db.query(Symbol).filter(Symbol.Id == id)

    if not symbol.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Symbol with id: {id} not found"
        )
    symbol.updated_at = datetime.utcnow()
    symbol.update(request)
    db.commit()
    return symbol


def destroy(id: int, db: Session):
    symbol = db.query(Symbol).filter(Symbol.Id == id)

    if not symbol.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Symbol with id: {id} not found"
        )

    symbol.delete(synchronize_session=False)
    db.commit()
    return 'done'


def get_by_str(name: str, db: Session):
    symbol = db.query(Symbol).filter(Symbol.symbol == name).first()
    if not symbol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Symbol: {name} not found, if you wish to track please add"
        )
    return symbol


from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from schemas import exchangeSchema
from models.exchanges import Exchange


def get_all(db: Session):
    markets = db.query(Exchange).all()
    return markets


def create(request: exchangeSchema.ExchangeCreate, db: Session):
    new_exchange = Exchange(name=request.name,
                        abrv=request.abrv,
                        country=request.country,
                        city=request.city,
                        open_time='-',
                        close_time='-',
                        created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow()
    )

    db.add(new_exchange)
    db.commit()
    db.refresh(new_exchange)

    return new_exchange


def show(id: int, db: Session):
    exchange = db.query(Exchange).filter(Exchange.Id == id).first()

    if not exchange:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Market with id: {id} not found"
        )
    return exchange


def update(id: int, request: exchangeSchema.Exchange, db: Session):
    exchange = db.query(Exchange).filter(Exchange.Id == id)

    if not exchange.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exchange with id: {id} not found"
        )

    exchange.update(request)
    exchange.updated_at = datetime.utcnow()
    db.commit()

    return exchange


def destroy(id: int, db: Session):
    exchange = db.query(Exchange).filter(Exchange.Id == id).first()

    if not exchange:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exchange with id: {id} not found"
        )
    exchange.delete(sunchronize_session=False)
    db.commit()
    return 'Exchange Deleted'

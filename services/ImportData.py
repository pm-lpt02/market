import csv
from fastapi import HTTPException, status
from models.exchanges import Exchange
from models.symbols import Symbol
from sqlalchemy.orm import Session
from datetime import datetime


def dataImport(filePath: str, requestor: str, db: Session):

    if requestor == "symbolRout":
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    new_symbol = Symbol(symbol=str(row[0]),
                                        created_at=datetime.utcnow(),
                                        updated_at=datetime.utcnow()
                                        )
                    new_symbol.active = True
                    db.add(new_symbol)

                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue
        db.commit()

    elif requestor == "exchangeRout":
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    new_exchange = Exchange(name=str(row[0]),
                                        abrv=str(row[1]),
                                        country=str(row[2]),
                                        city = str(row[3]),
                                        open_time = str(row[4]),
                                        close_time = str(row[5]),
                                        created_at =datetime.utcnow(),
                                        updated_at=datetime.utcnow()
                                        )
                    db.add(new_exchange)
                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue

        db.commit()

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"not recognized as an importable data file"
        )

    return {'detail': f"dataImport has been imported to the database"}

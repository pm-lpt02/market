from fastapi import APIRouter, Depends, status, Response, \
    UploadFile, File, HTTPException
from databases import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas import exchangeSchema
from repositories import exchangeRepository
from services.ImportData import dataImport
import os


router = APIRouter(
    prefix="/exchange",
    tags=['Exchanges']
)

app_root = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(app_root, 'data_files')
prefix = os.path.abspath(upload_folder)


@router.get('/', response_model=List[exchangeSchema.ExchangeView])
def all(db: Session = Depends(get_db)):
    return exchangeRepository.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: exchangeSchema.ExchangeCreate, db: Session = Depends(get_db)):
    return exchangeRepository.create(request, db)


@router.post("/uploadfile/", status_code=status.HTTP_201_CREATED)
async def upload_data_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    location = f"{prefix}/{file.filename}"
    if file.content_type == "text/csv":
        with open(location, "wb+") as file_object:
            file_object.write(file.file.read())

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Only csv files can be uploaded"
        )
    requestor = "exchangeRout"

    dataImport(location, requestor, db)

    return {"Info": f"file '{file.filename}' has been uploaded"}


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return exchangeRepository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: exchangeSchema.Exchange,
           db: Session = Depends(get_db)):
    return exchangeRepository.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=exchangeSchema.ExchangeDetail)
def show(id: int, response: Response,
         db: Session = Depends(get_db)):
    return exchangeRepository.show(id, db)

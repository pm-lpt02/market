from fastapi import APIRouter, Depends, status, Response, File, UploadFile, HTTPException
from databases import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas import symbolSchema
from repositories import symbolRepository
import os
from services.ImportData import dataImport

router = APIRouter(
    prefix='/symbol',
    tags=['Symbols']
)

app_root = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(app_root, 'data_files')
prefix = os.path.abspath(upload_folder)


@router.get('/', response_model=List[symbolSchema.Symbol])
def symbols(db: Session = Depends(get_db)):
    return symbolRepository.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: symbolSchema.SymbolCreate, db: Session = Depends(get_db)):
    return symbolRepository.create(request, db)


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
    requestor = "symbolRout"

    dataImport(location, requestor, db)

    return {"Info": f"file '{file.filename}' has been uploaded"}


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return symbolRepository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: symbolSchema.Symbol, db: Session = Depends(get_db)):
    return symbolRepository.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=symbolSchema.Symbol)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return symbolRepository.show(id, db)

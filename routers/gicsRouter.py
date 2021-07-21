from fastapi import APIRouter, Depends, HTTPException, status, \
    Response, File, UploadFile
from databases import get_db
from sqlalchemy.orm import Session
from repositories.classifiers import sectorRepository, ingroupRepository, \
    industryRepository, subinRepository
from typing import List
from schemas.classifiers.sectorSchema import Sector, SectorDetail
from schemas.classifiers.ingroupSchema import ViewIndGroup, IndustryGroupDetail
from schemas.classifiers.industrySchema import Industry, IndustryDetail
from schemas.classifiers.subindustSchema import ViewSubIndustry, SubIndustryDetail
import os
from services.ImportClassifiers import DataExtract

router = APIRouter(
    prefix='/classifiers',
    tags=['Classifiers']
)

app_root = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(app_root, 'data_files')
prefix = os.path.abspath(upload_folder)


@router.get('/sectors/', response_model=List[Sector])
def get_sectors(db: Session = Depends(get_db)):
    return sectorRepository.get_all(db)


@router.get('/ingroups/', response_model=List[ViewIndGroup])
def get_ingroups(db: Session = Depends(get_db)):
    return ingroupRepository.get_all(db)


@router.get('/industries/', response_model=List[Industry])
def get_industries(db: Session = Depends(get_db)):
    return industryRepository.get_all(db)


@router.get('/subInds/', response_model=List[ViewSubIndustry])
def get_subInds(db: Session = Depends(get_db)):
    return subinRepository.get_all(db)


@router.post('/uploadfile/', status_code=status.HTTP_201_CREATED)
async def upload_data_file(file: UploadFile = File(...),
                           db: Session = Depends(get_db)):
    location = f"{prefix}/{file.filename}"
    if file.content_type == "text/csv":
        with open(location, "wb+") as file_object:
            file_object.write(file.file.read())
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Only csv files can be uploaded"
        )

    DataExtract.verifyData(location, db)
    return {"Info": f"file '{file.filename}' has been uploaded"}




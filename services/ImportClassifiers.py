from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.gics import Sector, IndustryGroup, Industry, SubIndustry
import csv


def compareKeys(validkey, inputkey):
    validkey.sort()
    inputkey.sort()
    if validkey == inputkey:
        return True
    else:
        return False


sector_keys = ['SectorId', 'Sector']
ingroup_keys = ['IndustryGroupId', 'IndustryGroup', 'Sector']
industry_keys = ['IndustryId', 'Industry', 'IndustryGroup']
subin_keys = ['SubIndustryId', 'SubIndustry', 'SubIndustryDescription', 'Industry']


class DataExtract:

    def verifyData(filePath: str, db: Session):

        dataImported = ''
        with open(filePath, 'r') as f:
            primary_reader = csv.DictReader(f)
            columns = dict(list(primary_reader)[0])
            column_keys = list(columns.keys())

        if compareKeys(sector_keys, column_keys):
            DataExtract.uploadSectors(filePath, db)
            dataImported = 'sectors'

        elif compareKeys(ingroup_keys, column_keys):
            DataExtract.uploadIndustryGroup(filePath, db)
            dataImported = 'IndustryGroups'

        elif compareKeys(industry_keys, column_keys):
            DataExtract.uploadindustry(filePath, db)
            dataImported = 'Industries'

        elif compareKeys(subin_keys, column_keys):
            DataExtract.uploadsubind(filePath, db)
            dataImported = 'subindustries'

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"data does not match any uploadable object"
            )

        return dataImported

    def uploadSectors(filePath: str, db: Session):
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    new_sector = Sector(sector_id=int(row[0]), sector=str(row[1]))
                    db.add(new_sector)
                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue

        db.commit()

        return {'detail': f"sectors from uploaded successfully"}

    def uploadIndustryGroup(filePath: str, db: Session):
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            # skips headers
            next(reader)

            for row in reader:
                try:
                    sec = db.query(Sector).filter(Sector.sector == str(row[2])).first()

                    new_ingroup = IndustryGroup(
                        industrygroup_id=int(row[0]),
                        industrygroup=str(row[1]),
                        sector=sec
                    )

                    db.add(new_ingroup)

                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue

        db.commit()

        return {'detail': f"IndustrGroups from {filePath}, uploaded successfully"}

    def uploadindustry(filePath: str, db: Session):
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            # skips headers
            next(reader)

            for row in reader:
                try:
                    group = db.query(IndustryGroup).filter(IndustryGroup.industrygroup == str(row[2])).first()
                    new_industry = Industry(
                        industry_id=int(row[0]),
                        industry=str(row[1]),
                        industry_group=group
                    )

                    db.add(new_industry)

                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue
        db.commit()

        return {'detail': f"industries from {filePath}, uploaded successfully"}

    def uploadsubind(filePath: str, db: Session):
        with open(filePath, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    indust = db.query(Industry).filter(Industry.industry == str(row[3])).first()
                    new_subin = SubIndustry(
                        subindustry_id=int(row[0]),
                        subindustry=str(row[1]),
                        subindustry_description=str(row[2]),
                        industry=indust
                    )

                    db.add(new_subin)

                except ValueError as err:
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason: {}'.format(row, err))
                    continue
        db.commit()

        return {'detail': f"subindustries from {filePath}, uploaded successfully"}




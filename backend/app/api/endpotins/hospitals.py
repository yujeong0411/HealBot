from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...crud import hospital as crud
from ...schemas.hospital import Hospital
from ...database import get_db

router = APIRouter()

@router.get("/by-disease/{disease_id}", response_model=List[Hospital])
def read_hospitals_by_disease(disease_id: int, db: Session = Depends(get_db)):
    hospitals = crud.get_hospitals_by_disease(db, disease_id=disease_id)
    if not hospitals:
        raise HTTPException(status_code=404, detail="No hospitals found for this disease")
    return hospitals
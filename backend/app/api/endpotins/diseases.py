from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...crud import disease as crud
from ...schemas.disease import Disease
from ...database import get_db

router = APIRouter()

@router.get("", response_model=List[Disease])
def read_diseases(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    diseases = crud.get_diseases(db, skip=skip, limit=limit)
    return diseases


@router.get("/{disease_id}", response_model=Disease)
def read_disease(disease_id:int, db:Session=Depends(get_db)):
    disease = crud.get_disease(db, disease_id=disease_id)
    if disease is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    return disease

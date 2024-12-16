from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...crud import symptom as crud
from ...schemas.symptom import Symptom
from ...database import get_db


router = APIRouter()

# 여러 증상 조회회
@router.get("", response_model=List[Symptom])
def read_symptoms(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    symptoms = crud.get_symptoms(db, skip=skip, limit=limit)
    return symptoms

# 특정 증상 조회
@router.get("/{symptom_id}", response_model=Symptom)
def read_symptom(symptom_id:int, db:Session=Depends(get_db)):
    symptom = crud.get_symptom(db, symptom_id=symptom_id)
    if symptom is None:
        raise HTTPException(status_code=404, detail="Symptom not found")
    return symptom


from sqlalchemy.orm import Session
from ..models.models import Symptom
from ..schemas.symptom import SymptomCreate

def get_symptom(db: Session, symptom_id: int):
    return db.query(Symptom).filter(Symptom.symptom_id == symptom_id).first()


def get_symptoms(db:Session, skip: int = 0, limit: int = 100):
    return db.query(Symptom).offset(skip).limit(limit).all()


def creaste_symptoms(db:Session, symptom: SymptomCreate):
    db_symptom = Symptom(
        name = symptom.name,
        description = symptom.description,
        severity = symptom.severity
    )
    db.add(db_symptom)   # 추가
    db.commit()    # 저장
    db.refresh(db_symptom)   # 다시 읽기
    return db_symptom


def update_symptom(db:Session, symptom_id:int, symptom:SymptomCreate):
    db_symptom = db.query(Symptom).filter(Symptom.symptom_id == symptom_id).first()
    if db_symptom:
        for key, value in symptom.dict().items():
            setattr(db_symptom, key, value)
        db.commit()
        db.refresh(db_symptom)
    return db_symptom


def delete_symptom(db:Session, symptom_id: int):
    db_symptom = db.query(Symptom).filter(Symptom.symptom_id == symptom_id).first()
    if db_symptom:
        db.delete(db_symptom)
        db.commit()
    return db_symptom
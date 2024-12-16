from sqlalchemy.orm import Session
from ..models.models import Disease

def get_disease(db: Session, disease_id: int):
    return db.query(Disease).filter(Disease.disease_id == disease_id).first()


def get_diseases(db: Session, skip: int=0, limit: int=100):
    return db.query(Disease).offset(skip).limit(limit).all()


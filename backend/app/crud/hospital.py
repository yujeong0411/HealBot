from sqlalchemy.orm import Session
from ..models.models import Hospital, DiseaseHospital

def get_hospitals_by_disease(db:Session, disease_id: int):
    return db.query(Hospital).join(DiseaseHospital).filter(
        DiseaseHospital.disease_id == disease_id
    ).all()


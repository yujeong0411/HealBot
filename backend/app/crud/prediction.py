from sqlalchemy.orm import Session
from ..models.models import Prediction

def get_predictions_by_symptom(db:Session, symptom_id:int):
    return db.query(Prediction).filter(Prediction.symptom_id == symptom_id).all()
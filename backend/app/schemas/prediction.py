from pydantic import BaseModel, Field
from .symptom import Symptom
from .disease import Disease

class PredictionBase(BaseModel):
    symptom_id : int
    disease_id : int
    probability: float = Field(ge=0, le=1)  # 0과 1 사이의 확률값


class PredictionCreate(PredictionBase):
    pass 


class Prediction(PredictionBase):
    prediction_id: int
    symptom: Symptom
    disease: Disease

    class Config:
        from_attributes = True
        
from pydantic import BaseModel
from typing import Optional

class SymptomBase(BaseModel):
    name:str
    description: Optional[str] = None
    severity: Optional[int] = None

class SymptomCreate(SymptomBase):
    pass 

class Symptom(SymptomBase):
    symptom_id: int

    class Config:
        from_attributes = True


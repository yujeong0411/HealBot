from pydantic import BaseModel
from typing import Optional

class DiseaseBase(BaseModel):
    name: str
    description: Optional[str] = None
    department: str


class DiseaseCreate(DiseaseBase):
    pass 


class Disease(DiseaseBase):
    disease_id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel

class HospitalBase(BaseModel):
    name: str
    location: str
    department: str


class HospitalCreate(HospitalBase):
    pass 


class Hospital(HospitalBase):
    hospital_id: int

    class Config:
        from_attributes = True
        
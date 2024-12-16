from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Symptom(Base):
    __tablename__ = "symptom"

    symptom_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    severity = Column(Integer)

    # 1:N relationship 
    predictions = relationship("Prediction", back_populates="symptom")


class Prediction(Base):
    __tablename__ = "prediction"

    prediction_id = Column(Integer, primary_key=True, index=True)
    symptom_id = Column(Integer, ForeignKey("symptom.symptom_id"), nullable=False)
    disease_id = Column(Integer, ForeignKey("disease.disease_id"), nullable=False)
    probability = Column(Float)

    # N:1
    symptom = relationship("Symptom", back_populates="predictions")
    disease = relationship("Disease", back_populates="predictions")


class Disease(Base):
    __tablename__ = 'disease'

    disease_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    department = Column(String(50))

    # 1:N relationship
    predictions = relationship("Prediction", back_populates="disease")

    # N:M 
    hospitals = relationship("Hospital", secondary="disease_hospital", back_populates="diseases")


class Hospital(Base):
    __tablename__ = "hospital"

    hospital_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    location = Column(String(200))
    department = Column(String(50))

    # N:M
    diseases = relationship("Disease", secondary="disease_hospital", back_populates="hospitals")


class DiseaseHospital(Base):
    __tablename__ = "disease_hospital"

    disease_id = Column(Integer, ForeignKey("disease.disease_id"), primary_key=True)
    hospital_id = Column(Integer, ForeignKey("hospital.hospital_id"), primary_key=True)
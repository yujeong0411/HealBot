from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...crud import prediction as crud
from ...schemas.prediction import Prediction
from ...database import get_db
from ...services.symptom_analyzer import SymptomAnalyzer

router = APIRouter()

# 기본 예측 데이터 조회
@router.get("/by-symptom/{symptom_id}", response_model=List[Prediction])
def read_predictions_by_symptom(symptom_id: int, db: Session = Depends(get_db)):
    predictions = crud.get_predictions_by_symptom(db, symptom_id=symptom_id)
    if not predictions:
        raise HTTPException(status_code=404, detail="No predictions found for this symptom")
    return predictions


# 증상 분석 결과 조회
@router.get("/analyze/{symptom_id}")
async def analyze_symptom(symptom_id:int, db:Session=Depends(get_db)):
    # SymptomAnalyzer 인스턴스 생성
    analyzer = SymptomAnalyzer(db)

    # 증상 분석
    try:
        results = await analyzer.analyze_symptom(symptom_id)
        if not results:
            raise HTTPException(
                status_code=404,
                detail="No analysis results available for this symptom"
            )
        
        # 결과반환
        return {
            "symptom_id":symptom_id,
            "predictions":results
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occured during analysis: {str(e)}")
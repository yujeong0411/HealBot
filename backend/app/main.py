from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .database import engine, get_db
from .models.models import Base
from .api.endpotins import symptoms, diseases, hospitals, predictions

# 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 인스턴스 생성
app = FastAPI(
    title="HealBot API",
    description="AI 기반 증상 분석 및 병원 추천 시스템",
    version="1.0.0"
)

# 라우터 등록
app.include_router(
    symptoms.router,
    prefix="/symptoms",
    tags=["symptoms"]
)

app.include_router(
    diseases.router,
    prefix="/diseases",
    tags=["diseases"]
)

app.include_router(
    hospitals.router,
    prefix="/hospitals",
    tags=["hospitals"]
)

app.include_router(
    predictions.router,
    prefix="/predictions",
    tags=["predictions"]
)

@app.get("/")
def read_root():
    return {"message":"welcom to HealBot API"}


@app.get("/health")
def health_check():
    return {"status":'healthy'}

# 데이터 베이스 연결 테스트 
@app.get("/db-test")
def test_db(db:Session = Depends(get_db)):
    try:
        # 데이터 베이스 뭐리 실행
        db.execute(text("SELECT 1"))
        return {"message":"Database connection successful"}
    except Exception as e:
        return {"error":f"Database connection failed: {str(e)}"}


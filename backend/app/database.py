from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 연결 URL 설정
# format: mysql+pymysql://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:mpyuj9933!@localhost/healbot"

# 엔진 생성 -  echo=True를 추가하여 SQL 로그 확인 가능
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
Base = declarative_base()

# DB 세션 의존성
def get_db():
    db = SessionLocal()   # 세션 객체 생성
    try:
        yield db   # 세션 객체를 반환
    finally:
        db.close()   # 작업이 끝나면 세션 종료
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    # API
    HEALTH_API_KEY : str = os.getenv("HEALTH_API_KEY", "")  # 환경변수에서 직접 가져오기
    HOSPITAL_API_URL: str = "http://apis.data.go.kr/B551182/MadmDtlInfoService2.7"

    class Config:
        env_file = ".env"

settings = Settings()

# API 키가 제대로 로드되었는지 확인
print(f"Loaded API KEY: {settings.HEALTH_API_KEY[:10]}...")

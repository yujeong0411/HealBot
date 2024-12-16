import asyncio
import sys
import os

# 상위 디렉토리의 app을 import 할 수 있도록 경로 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.api_client.health_insurance import HealthInsuranceAPI

async def test_api():
    client = HealthInsuranceAPI()
    result = await client.get_hospital_info()
    print(result)

if __name__ == "__main__":
    asyncio.run(test_api())
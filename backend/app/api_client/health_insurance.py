import httpx   # 비동기 HTTP 요청을 위한 라이브러리
from typing import Optional   # 선택적 매개변수 타입 힌트를 위한 모듈
from ..config import settings   # 프로젝트 설정 파일에서 API 키와 URL 가져오기
import xml.etree.ElementTree as ET   # XML 파싱을 위한 표준 라이브러리

class HealthInsuranceAPI:
    def __init__(self):
         # API 키와 기본 URL을 설정 파일에서 가져옴
        self.api_key = settings.HEALTH_API_KEY
        self.hospital_base_url = settings.HOSPITAL_API_URL
        # print(f"Initialized with API key: {self.api_key[:10]}...")  # API 키 확인용

    async def get_hospital_info(
            self,
            location: Optional[str] = None,   # 선택적 지역 매개변수
            page: int = 1,    # 페이지 번호 (기본값 1)
            rows: int = 10    # 한 페이지당 조회할 데이터 수 (최대 10개)
    ) -> dict[str, any]:   # 반환 타입은 문자열 키를 가진 딕셔너리
        # API 요청에 필요한 파라미터 설정
        params = {
            "serviceKey": self.api_key,   # API 인증 키
            "pageNo" : str(page),    # 페이지 번호 (문자열로 변환)
            "numOfRows" : str(rows),   # 조회할 데이터 수 (문자열로 변환)
            "type": "xml"   # 응답 형식 (XML)
        }

        # 지역 정보가 제공되면 파라미터에 추가
        if location:
            params['location'] = location

        # HTTP 요청을 비동기로 처리하기 위한 클라이언트
        async with httpx.AsyncClient() as client:
            try:
                # 최종 요청 URL 구성 (진료과목 정보 조회 엔드포인트)
                url = f"{self.hospital_base_url}/getDgsbjtInfo2.7"
                print(f"요청 URL: {url}")
                print(f"파라미터: {params}")

                # 비동기 GET 요청 수행
                response = await client.get(url, params=params)
                print(f"상태 코드: {response.status_code}")
                print(f"응답 내용: {response.text}")
                

                # XML 문자열을 파싱하여 트리 구조로 변환
                root = ET.fromstring(response.text)

                # header 정보추출
                # .//resultCode: XML 문서 전체에서 resultCode 요소 찾기
                header = {
                    "resultCode": root.find('.//resultCode').text,   # 결과 코드
                    "resultMsg": root.find('.//resultMsg').text      # 결과 메시지
                }

                # body 정보추출
                body = {
                    "numOfRows": root.find('.//numOfRows').text,   # 페이지당 데이터 수
                    "pageNo": root.find('.//pageNo').text,         # 현재 페이지 번호
                    "totalCount": root.find('.//totalCount').text  # 전체 데이터 수
                }                

                # items 처리
                items_elem = root.find('.//items')
                item = []
                # items 요소가 존재하면 각 항목을 문자열로 변환
                if items_elem is not None:
                    items = [ET.tostring(item).decode() for item in items_elem]

                return {
                    "header": header,    # API 호출 상태 정보
                    "body" : body,       # 페이징 관련 메타데이터
                    "items": items       # 조회된 데이터 항목들
                }
            
            except Exception as e:
                print(f'API 호출 오류 : {str(e)}')
                return {"error": str(e)}

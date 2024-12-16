# 규칙 기반 예측 시스템  -> 추후 ML 모델 확장
from sqlalchemy.orm import Session
from ..crud import prediction as prediction_crud
from ..crud import disease as disease_crud

class SymptomAnalyzer:
    """
    SymptomAnalyzer 초기화
    Args:
        db (Session): 데이터베이스 세션
    """
    # __init__: 클래스의 생성자 (초기화 메서드)
    # 클래스의 인스턴스가 생성될 때 자동으로 호출됨
    def __init__(self, db: Session):
        # self: 클래스의 인스턴스를 가리킴
        # self.db: 인스턴스 변수로 db를 저장
        self.db = db
        # 나중에 ML 모델이 추가되면:
        # self.model = self._load_model()

    # 클래스의 메서드
    # self를 첫 번째 매개변수로 받아 인스턴스 변수에 접근 가능
    async def analyze_symptom(self, symptom_id:int) -> list[dict]:
        """
        증상 ID를 받아서 가능한 질병들을 예측
        Args:
            symptom_id(int) : 분석할 증상 ID
        Returns: 
            list[dict]: 예측된 질병목록과 확률
        """
        # 1. 데이터 베이스에서 증상 예측 데이터 가져오기
        predictions = prediction_crud.get_predictions_by_symptom(self.db, symptom_id=symptom_id)

        # 2. 예측 결과를 확률 기준으로 정렬
        sorted_predictions = sorted(predictions, key=lambda x:x.probability, reverse=True)

        # 3. 결과 형식화
        results = []
        for pred in sorted_predictions:
            # 각 예측에 해당하는 질병 정보 가져오기
            disease = disease_crud.get_disease(db=self.db, disease_id=pred.disease_id)

            # 결과 딕셔너리 저장
            results.append({
                "disease_name":disease.name,
                "probability":pred.probability,
                "department":disease.department,
                "description":disease.description
            })

        return results
    

    def _load_model(self):
        """
        ML 모델을 로드하는 메서드 (향후 구현)
        """
        pass
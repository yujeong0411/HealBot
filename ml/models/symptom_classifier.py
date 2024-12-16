import numpy as np

class SymtomClassifier:
    def __init__(self):
        # 간단한 규칙 기반 시스템
        self.symptom_disease_rules = {
            "두통" : {
                "편두통":0.8,
                "긴장성 두통":0.6,
                "군발 두통": 0.3
            },
            # 규칙 추가
        }
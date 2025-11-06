# -*- coding: utf-8 -*-
import warnings
import torch
from transformers import (
    AutoTokenizer as AutoTokCls,
    AutoModelForSequenceClassification,
    pipeline
)
from typing import Dict

# 경고 메시지 억제 (모델 체크포인트 가중치 경고는 정상 동작)
warnings.filterwarnings("ignore", message=".*weights.*were not used.*")
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

# ===== 모델 ID =====
SENTIMENT_MODEL_ID = "joeddav/xlm-roberta-large-xnli"  # 제로샷 감성 분류

# ===== 전역 모델 로드 =====
_zero_tok = None
_zero_model = None
_zero = None

# 감정 -> 분위기 매핑
MOOD_MAP = {"긍정": "잔잔한", "중립": "담담한", "부정": "쓸쓸한"}


def _pipeline_device_index() -> int:
    """pipeline의 device 인덱스 반환 (GPU면 0, 아니면 -1)"""
    return 0 if torch.cuda.is_available() else -1


def _load_sentiment_model():
    """감정 분류 모델 로드 (싱글톤 패턴)"""
    global _zero_tok, _zero_model, _zero
    
    if _zero is None:
        try:
            print(f"감정 분류 모델 로딩 중: {SENTIMENT_MODEL_ID}")
            _zero_tok = AutoTokCls.from_pretrained(SENTIMENT_MODEL_ID)
            _zero_model = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL_ID)
            _zero = pipeline(
                "zero-shot-classification",
                model=_zero_model,
                tokenizer=_zero_tok,
                device=_pipeline_device_index()
            )
            print("감정 분류 모델 로딩 완료")
        except Exception as e:
            print(f"감정 분류 모델 로드 오류: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    return _zero


def detect_sentiment(text: str, labels=("긍정", "중립", "부정")) -> str:
    """
    텍스트의 감정을 분류합니다 (긍정/중립/부정)
    
    Args:
        text: 입력 텍스트
        labels: 분류할 감정 라벨
    
    Returns:
        감정 ("긍정", "중립", "부정" 중 하나)
    """
    if not text or len(text.strip()) == 0:
        return "중립"
    
    classifier = _load_sentiment_model()
    
    if classifier is None:
        return "중립"
    
    try:
        out = classifier(
            text,
            candidate_labels=list(labels),
            hypothesis_template="이 문장은 {} 감성이다."
        )
        return out["labels"][0] if out and len(out["labels"]) > 0 else "중립"
    except Exception as e:
        print(f"감정 분류 오류: {e}")
        return "중립"


def classify_emotion(text: str) -> Dict[str, any]:
    """
    텍스트의 감정을 분류하고 분위기를 반환합니다.
    
    Args:
        text: 입력 텍스트
    
    Returns:
        감정 분류 결과 딕셔너리 (sentiment, mood, confidence 포함)
    """
    sentiment = detect_sentiment(text)
    mood = MOOD_MAP.get(sentiment, "담담한")
    
    # 실제 confidence 값 가져오기
    confidence = 0.5  # 기본값
    if not text or len(text.strip()) == 0:
        confidence = 0.0
    else:
        classifier = _load_sentiment_model()
        if classifier is not None:
            try:
                out = classifier(
                    text,
                    candidate_labels=["긍정", "중립", "부정"],
                    hypothesis_template="이 문장은 {} 감성이다."
                )
                if out and "scores" in out and len(out["scores"]) > 0:
                    confidence = float(out["scores"][0])
            except Exception as e:
                print(f"감정 분류 confidence 계산 오류: {e}")
    
    # 기존 API 호환성을 위한 감정 매핑
    emotion_map = {
        "긍정": "기쁨",
        "중립": "중립",
        "부정": "슬픔"
    }
    
    return {
        "emotion": emotion_map.get(sentiment, "중립"),  # 기존 API 호환
        "sentiment": sentiment,  # 긍정/중립/부정
        "mood": mood,  # 잔잔한/담담한/쓸쓸한
        "confidence": confidence  # 실제 confidence 값
    }

# -*- coding: utf-8 -*-
import warnings
import re
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer

# sklearn 경고 억제 (tokenizer 사용 시 token_pattern은 무시되지만 정상 동작)
# 전역 필터링으로 모든 sklearn 경고 억제
warnings.filterwarnings("ignore", message=".*token_pattern.*will not be used.*")
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.feature_extraction.text")


def _tok_ko(text: str) -> List[str]:
    """한글/영문/숫자 토큰, 2글자 이상"""
    return [t for t in re.findall(r"[가-힣A-Za-z0-9]+", text) if len(t) >= 2]


def _split_to_docs(ctx: str) -> List[str]:
    """TF-IDF용 소문서 쪼개기(문단/문장 기준 단순 분할)"""
    docs = [s.strip() for s in re.split(r"[.\n!?]+", ctx) if s.strip()]
    if len(docs) < 3:
        # 너무 적으면 복제해서 최소 문서 수 확보
        docs = (docs or [ctx.strip()]) * 3
    return docs[:10]  # 과도한 길이 방지


def _remove_similar_keywords(keywords: List[str]) -> List[str]:
    """
    의미적으로 유사하거나 중복되는 키워드를 제거합니다.
    - 한 키워드가 다른 키워드에 포함되는 경우 제거
    - 너무 짧은 키워드(1-2자) 중복 제거
    """
    if not keywords:
        return []
    
    # 길이순 정렬 (긴 것부터) - 긴 키워드가 더 의미있음
    sorted_kws = sorted(keywords, key=len, reverse=True)
    result = []
    seen = set()
    
    for kw in sorted_kws:
        kw_lower = kw.lower()
        # 이미 포함된 키워드인지 확인
        is_duplicate = False
        for existing in result:
            existing_lower = existing.lower()
            # 한 키워드가 다른 키워드에 포함되거나 동일한 경우
            if kw_lower in existing_lower or existing_lower in kw_lower:
                if len(kw) < len(existing):
                    # 더 짧은 키워드는 스킵
                    is_duplicate = True
                    break
                elif len(kw) > len(existing) and kw_lower != existing_lower:
                    # 더 긴 키워드로 교체
                    result.remove(existing)
                    seen.discard(existing_lower)
                    break
        
        if not is_duplicate and kw_lower not in seen:
            result.append(kw)
            seen.add(kw_lower)
    
    return result


def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
    """
    TF-IDF를 사용하여 텍스트에서 키워드를 추출합니다.
    개선사항:
    - 더 많은 키워드 추출 (기본값: 10개)
    - 의미적으로 유사한 키워드 제거
    - 중복 제거 강화
    
    Args:
        text: 입력 텍스트
        max_keywords: 추출할 최대 키워드 개수 (기본값: 10)
    
    Returns:
        추출된 키워드 리스트 (중복 제거됨)
    """
    if not text or len(text.strip()) == 0:
        return []
    
    try:
        docs = _split_to_docs(text)
        # tokenizer를 사용하므로 token_pattern 파라미터를 전달하지 않음
        # warnings.catch_warnings()로 경고 억제
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message=".*token_pattern.*will not be used.*")
            warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
            # tokenizer를 사용할 때는 token_pattern 파라미터 자체를 전달하지 않음
            vec = TfidfVectorizer(tokenizer=_tok_ko, min_df=1, max_df=0.95)  # 너무 흔한 단어 제외
        vec.fit(docs + [text])
        scores = vec.transform([text]).toarray()[0]
        terms = vec.get_feature_names_out()
        idx = scores.argsort()[::-1]
        
        # 더 많은 키워드 추출 (나중에 필터링)
        candidate_kws = []
        seen = set()
        for i in idx:
            w = terms[i]
            # 숫자만 있는 키워드 제외
            if w.isdigit():
                continue
            # 너무 짧은 단어 제외 (1글자는 제외, 2글자 이상만)
            if len(w) < 2:
                continue
            # 중복 확인
            if w.lower() in seen:
                continue
            seen.add(w.lower())
            candidate_kws.append(w)
            # 충분한 후보를 모으면 중단 (필터링 전에 더 많이 수집)
            if len(candidate_kws) >= max_keywords * 2:
                break
        
        # 의미적으로 유사한 키워드 제거
        filtered_kws = _remove_similar_keywords(candidate_kws)
        
        # 최대 개수로 제한
        return filtered_kws[:max_keywords]
    
    except Exception as e:
        # 오류 발생 시 간단한 단어 추출
        korean_words = re.findall(r'[가-힣]+', text)
        unique_words = list(dict.fromkeys([w for w in korean_words if len(w) >= 2]))
        # 중복 제거
        filtered = _remove_similar_keywords(unique_words)
        return filtered[:max_keywords]


def make_keyword_tag(keywords: List[str]) -> str:
    """키워드를 태그 형식으로 변환"""
    return f"<k>{', '.join(keywords)}</k>"

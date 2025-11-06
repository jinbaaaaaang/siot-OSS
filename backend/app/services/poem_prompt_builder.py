# -*- coding: utf-8 -*-
"""
시 생성 프롬프트 구성 관련 함수
"""

from typing import List, Optional


def _build_messages_kogpt2(
    keywords: List[str], 
    mood: str, 
    lines: int, 
    original_text: str = "",
    banned_words: Optional[List[str]] = None,
    use_rhyme: bool = False,
    acrostic: Optional[str] = None,
) -> str:
    """
    koGPT2용 텍스트 프롬프트 생성 (chat template 없음)
    koGPT2는 작은 모델이므로 간결하고 명확한 프롬프트가 필요합니다.
    """
    kw_list = keywords[:6] if keywords else []
    if not kw_list:
        kw_str = "일상"
    else:
        kw_str = ", ".join(kw_list)
    
    # 옵션 문자열 생성
    constraints = []
    if banned_words:
        constraints.append(f"금지 단어: {', '.join(banned_words)} (절대 사용하지 마세요)")
    if use_rhyme:
        constraints.append("두운이나 두행두운을 사용하여 운율을 만들어주세요")
    if acrostic:
        acrostic_chars = " ".join(list(acrostic))
        constraints.append(f"아크로스틱: 각 줄의 첫 글자가 순서대로 '{acrostic_chars}'가 되도록 (총 {len(acrostic)}줄)")
    
    constraint_text = "\n".join([f"- {c}" for c in constraints]) if constraints else ""
    
    # koGPT2에 최적화된 프롬프트
    # 시적인 표현 강조
    prompt = f"""다음 키워드와 분위기를 바탕으로 시를 작성하세요. 시는 일상적인 글과 다릅니다. 감성적이고 은유적인 표현을 사용하세요.

예시:
키워드: 봄, 꽃, 희망
분위기: 따뜻한
시:
봄날 꽃잎이
희망처럼 피어나고
따뜻한 바람이
새로운 시작을 안고
꽃향기 속에
미래가 흐른다

키워드: 밤, 별, 꿈
분위기: 잔잔한
시:
밤하늘 별들이
꿈을 비추고
잔잔한 마음에
희망이 스며든다
별빛 속에서
내일이 기다린다

키워드: {kw_str}
분위기: {mood}
{constraint_text if constraint_text else ""}
시:
"""
    
    return prompt


def _build_messages(
    keywords: List[str], 
    mood: str, 
    lines: int, 
    original_text: str = "",
    banned_words: Optional[List[str]] = None,
    use_rhyme: bool = False,
    acrostic: Optional[str] = None,
) -> list:
    """
    Instruct 모델에 맞는 대화 템플릿 구성.
    - system: 역할 명시 (시인)
    - user: 요구조건(분위기, 줄 수, 키워드, 원본 텍스트 맥락, 시만 출력)
    """
    # 키워드를 명확하게 구성 (최대 6개까지 사용)
    kw_list = keywords[:6] if keywords else []
    if not kw_list:
        kw_str = "일상"
        print("[_build_messages] ⚠️ 키워드가 비어있어 '일상'을 사용합니다.")
    else:
        # 키워드를 명확하게 나열하고 강조
        kw_str = ", ".join(kw_list)
        print(f"[_build_messages] 사용할 키워드: {kw_list}")
    
    # 원본 텍스트의 핵심 문장 추출 (최대 100자)
    context_hint = ""
    if original_text:
        # 원본 텍스트의 앞부분 일부를 맥락으로 제공 (너무 길지 않게)
        context_preview = original_text[:100].strip()
        if len(original_text) > 100:
            context_preview += "..."
        context_hint = f"\n원본 글의 맥락: {context_preview}\n"
    
    # 제약 조건 구성
    constraints = []
    if banned_words:
        constraints.append(f"- 금지 단어: {', '.join(banned_words)} (이 단어들을 절대 사용하지 마세요)")
    if use_rhyme:
        constraints.append("- 두운(첫소리)이나 두행두운(첫 두 소리)을 사용하여 운율을 만들어주세요")
    if acrostic:
        # 아크로스틱: 각 줄의 첫 글자가 지정된 문자여야 함
        acrostic_chars = " ".join(list(acrostic))
        constraints.append(f"- 아크로스틱: 각 줄의 첫 글자가 순서대로 '{acrostic_chars}'가 되도록 작성하세요 (총 {len(acrostic)}줄)")
    
    constraint_text = "\n".join(constraints) if constraints else ""
    
    # SOLAR-Instruct 모델에 최적화된 프롬프트 (키워드와 맥락 강조)
    user_msg = (
        f"다음 키워드와 맥락을 바탕으로 {lines}줄 이상의 한국어 시를 작성해주세요.\n\n"
        f"**중요**: 반드시 한국어로만 작성하세요. 중국어, 일본어, 영어 등 다른 언어를 사용하지 마세요.\n\n"
        f"**반드시 포함해야 할 키워드**: {kw_str}\n"
        f"**분위기**: {mood}\n"
        f"{context_hint}"
        f"**요구사항**:\n"
        f"- 반드시 위의 키워드들을 시에 자연스럽게 포함시키세요\n"
        f"- 키워드의 의미와 감정을 잘 반영하여 시를 작성하세요\n"
        f"- {mood}한 분위기를 느낄 수 있도록 작성하세요\n"
        f"- 한국어로만 작성 (다른 언어 절대 사용 금지)\n"
        f"- 최소 {lines}줄 이상 작성\n"
    )
    
    if constraint_text:
        user_msg += f"{constraint_text}\n"
    
    user_msg += f"- 시 내용만 출력 (설명이나 주석 없이)"
    
    messages = [
        {"role": "system", "content": "당신은 한국어 전용 시인입니다. 오직 한국어(한글)로만 시를 작성합니다. 중국어, 일본어, 영어 등 다른 언어는 절대 사용하지 않습니다. 주어진 키워드와 원본 글의 맥락을 반드시 반영하여 감성적인 한국어 시를 작성합니다. 키워드의 의미와 감정을 잘 이해하고 시에 자연스럽게 녹여내세요."},
        {"role": "user", "content": user_msg},
    ]
    
    # 프롬프트에 키워드가 제대로 들어갔는지 확인
    user_content = user_msg.lower()
    for kw in kw_list[:3]:  # 최대 3개만 확인
        if kw.lower() in user_content:
            print(f"[_build_messages] ✓ 키워드 '{kw}'가 프롬프트에 포함됨")
        else:
            print(f"[_build_messages] ⚠️ 키워드 '{kw}'가 프롬프트에 포함되지 않았습니다!")
    
    return messages


__all__ = ['_build_messages', '_build_messages_kogpt2']


# -*- coding: utf-8 -*-
"""
시 생성 메인 함수 (SOLAR / koGPT2 공용)

- Colab에서는 보통 MODEL_TYPE = "solar" 로 사용
- 프롬프트 구성: app.services.poem_prompt_builder
- 모델/토크나이저 로딩: app.services.poem_model_loader
- 후처리(줄 정리 등): app.services.poem_text_processor
- 번역: app.services.translator (비한국어 시 → 한국어로 자동 번역)
"""

import time
import traceback
from typing import List, Optional

import torch

from app.services.poem_config import (
    USE_ML_MODEL,
    MODEL_TYPE,
    DEFAULT_LINES,
    DEFAULT_MAX_NEW_TOKENS_GPU,
    DEFAULT_MAX_NEW_TOKENS_CPU,
)
from app.services.poem_model_loader import (
    _load_poem_model,
    _is_gpu,
    _device_info,
)
from app.services.poem_prompt_builder import (
    _build_messages,
    _build_messages_kogpt2,
)
from app.services.poem_text_processor import (
    _postprocess_poem,
)
from app.services.translator import (
    translate_poem_with_retry,
    detect_language,
)

# =====================================================================
# Colab BrokenPipeError 방지용 안전한 print
# =====================================================================
import builtins
import errno

_original_print = builtins.print


def safe_print(*args, **kwargs):
    """
    Colab에서 stdout 파이프가 끊어진 뒤에도 BrokenPipeError가 나지 않도록 하는 print.

    - EPIPE(Broken pipe) 에러만 조용히 무시
    - 나머지 에러는 그대로 발생시켜서 디버깅에 쓰기
    """
    try:
        _original_print(*args, **kwargs)
    except OSError as e:
        if e.errno == errno.EPIPE:
            # 출력 파이프가 끊어졌을 때는 그냥 무시
            return
        raise


# 이 모듈 안에서는 print -> safe_print 사용
print = safe_print  # noqa: E305


# =====================================================================
# 내부 디버깅용 함수
# =====================================================================

def _log_header(title: str):
    """블록 단위 로그 헤더"""
    try:
        print("\n" + "=" * 80, flush=True)
        print(f"[poem_generator] {title}", flush=True)
        print("=" * 80, flush=True)
    except Exception:
        # 여기서까지 에러 나면 그냥 조용히 무시 (BrokenPipe 등)
        pass


def _debug_tensor(name: str, tensor: torch.Tensor):
    """텐서 모양/타입 출력 (필요할 때만 참조용)"""
    try:
        print(
            f"[debug] {name}: shape={tuple(tensor.shape)}, "
            f"dtype={tensor.dtype}, device={tensor.device}",
            flush=True,
        )
    except Exception:
        print(f"[debug] {name}: <unavailable>", flush=True)


def _messages_to_prompt(messages: List[dict]) -> str:
    """
    chat_template 없이 messages(list[role/content]) → 단일 프롬프트 문자열로 변환.

    SOLAR 토크나이저에 chat_template 이 없어도 동작하도록 하기 위한 유틸.
    """
    parts = []
    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        if not content:
            continue

        # 역할에 따라 간단한 태그만 붙여줌 (모델이 크게 민감하지 않도록)
        if role == "system":
            parts.append(f"[시스템]\n{content}")
        elif role == "user":
            parts.append(f"[사용자]\n{content}")
        elif role == "assistant":
            parts.append(f"[어시스턴트]\n{content}")
        else:
            parts.append(str(content))
    prompt = "\n\n".join(parts).strip()
    return prompt


# =====================================================================
# 핵심: 키워드/분위기 기반 시 생성 함수
# =====================================================================

@torch.no_grad()
def generate_poem_from_keywords(
    keywords: List[str],
    mood: str = "잔잔한",
    lines: int = DEFAULT_LINES,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS_GPU,
    original_text: str = "",
    banned_words: Optional[List[str]] = None,
    use_rhyme: bool = False,
    acrostic: Optional[str] = None,
    model_type: Optional[str] = None,  # "solar" 또는 "kogpt2"
) -> str:
    func_start = time.time()
    _log_header("시 생성 함수 진입 (단순 버전)")

    print(f"[args] keywords={keywords}", flush=True)
    print(f"[args] mood={mood}, lines={lines}, max_new_tokens={max_new_tokens}", flush=True)
    print(f"[env] MODEL_TYPE(default)={MODEL_TYPE}, device={_device_info()}, USE_ML_MODEL={USE_ML_MODEL}", flush=True)

    if not USE_ML_MODEL:
        raise RuntimeError("USE_ML_MODEL=False 상태입니다. (ML 모델 생성 비활성화)")

    from app.services.poem_config import MODEL_TYPE as DEFAULT_MODEL_TYPE
    actual_model_type = (model_type or DEFAULT_MODEL_TYPE).lower()
    if actual_model_type not in ["solar", "kogpt2"]:
        print(f"[warn] 잘못된 model_type '{actual_model_type}' → 기본값 '{DEFAULT_MODEL_TYPE}' 사용", flush=True)
        actual_model_type = DEFAULT_MODEL_TYPE

    # 1) 모델 로딩
    print(f"[step] 1. 모델 로딩 시작 (model_type={actual_model_type})", flush=True)
    tok, model = _load_poem_model(actual_model_type)
    print(f"[step] ✓ 모델 로딩 완료 (device={_device_info()})", flush=True)

    # 2) 프롬프트 & 토크나이즈 (최소 버전)
    print(f"[step] 2. 프롬프트 구성 및 토크나이즈", flush=True)
    t_enc = time.time()

    if not lines or lines <= 0:
        lines = DEFAULT_LINES

    # === 여기서부터 chat_template 안 쓰도록 수정 ===
    if actual_model_type == "kogpt2":
        # koGPT2용 프롬프트
        prompt_text = _build_messages_kogpt2(
            keywords=keywords,
            mood=mood,
            lines=lines,
            original_text=original_text,
            banned_words=banned_words,
            use_rhyme=use_rhyme,
            acrostic=acrostic,
        )
        print(f"[step] koGPT2 프롬프트 (앞 200자): {repr(prompt_text[:200])}", flush=True)
        enc_ids = tok.encode(prompt_text, return_tensors="pt")
    else:
        # SOLAR(또는 기타 chat 모델) → messages(list[dict])를 직접 문자열로 풀어서 사용
        messages = _build_messages(
            keywords=keywords,
            mood=mood,
            lines=lines,
            original_text=original_text,
            banned_words=banned_words,
            use_rhyme=use_rhyme,
            acrostic=acrostic,
        )
        prompt_text = _messages_to_prompt(messages)
        print(f"[step] SOLAR 프롬프트 (앞 200자): {repr(prompt_text[:200])}", flush=True)

        # chat_template 없이 그냥 일반 텍스트 프롬프트로 인코딩
        enc = tok(prompt_text, return_tensors="pt")
        enc_ids = enc["input_ids"]

    # Tensor 형태 정리
    if isinstance(enc_ids, torch.Tensor):
        if enc_ids.dim() == 1:
            enc_ids = enc_ids.unsqueeze(0)
    else:
        enc_ids = torch.tensor(enc_ids, dtype=torch.long).unsqueeze(0)

    enc_ids = enc_ids.to(dtype=torch.long)
    print(f"[step] ✓ 토크나이즈 완료 ({time.time() - t_enc:.2f}s)", flush=True)
    _debug_tensor("input_ids(raw)", enc_ids)

    # 2-2) device 이동
    model_device = next(model.parameters()).device
    input_ids = enc_ids.to(model_device)
    attention_mask = torch.ones_like(input_ids, dtype=torch.long, device=model_device)

    # 3) 생성 파라미터 (최소 인자)
    print("[step] 3. 생성 파라미터 설정 (단순)", flush=True)
    is_gpu = _is_gpu()
    safe_max_new = max_new_tokens
    min_required = max(30, lines * 8)
    if safe_max_new < min_required:
        safe_max_new = min_required

    if is_gpu:
        safe_max_new = min(safe_max_new, 80)
    else:
        safe_max_new = min(safe_max_new, 40)

    # eos / pad 토큰 방어 코드
    eos_token_id = tok.eos_token_id
    pad_token_id = tok.pad_token_id

    if eos_token_id is None:
        # 일부 토크나이저는 eos_token_id가 None인 경우가 있음
        if getattr(tok, "eos_token", None) is not None:
            eos_token_id = tok.convert_tokens_to_ids(tok.eos_token)
    if pad_token_id is None:
        pad_token_id = eos_token_id

    # 혹시라도 이상한 값이면 vocab 범위 안으로 보정
    try:
        vocab_size = getattr(model.config, "vocab_size", None)
        if vocab_size is not None:
            if eos_token_id is None or not (0 <= int(eos_token_id) < vocab_size):
                print(f"[warn] eos_token_id({eos_token_id})가 vocab 범위를 벗어남 → 마지막 토큰으로 보정", flush=True)
                eos_token_id = vocab_size - 1
            if pad_token_id is None or not (0 <= int(pad_token_id) < vocab_size):
                print(f"[warn] pad_token_id({pad_token_id})가 vocab 범위를 벗어남 → eos_token_id로 보정", flush=True)
                pad_token_id = eos_token_id
    except Exception as e:
        print(f"[warn] eos/pad 토큰 보정 중 예외 발생: {type(e).__name__}: {str(e)[:100]}", flush=True)

    gen_kwargs = {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "max_new_tokens": safe_max_new,
        "eos_token_id": int(eos_token_id) if eos_token_id is not None else None,
        "pad_token_id": int(pad_token_id) if pad_token_id is not None else None,
        "do_sample": True,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    print(
        "[gen_kwargs(simple)]",
        {k: (v if not isinstance(v, torch.Tensor) else f"Tensor(shape={tuple(v.shape)})") for k, v in gen_kwargs.items()},
        flush=True,
    )

    # 4) model.generate()
    print("[step] 4. model.generate() 호출 (단순)", flush=True)
    t_gen = time.time()
    try:
        out = model.generate(**gen_kwargs)
    except Exception as e:
        traceback.print_exc()
        # 이 에러는 FastAPI 쪽에서 잡아서 detail로 내려감
        raise Exception(f"model.generate() 단계에서 오류 발생: {type(e).__name__}: {str(e)[:200]}")

    print(f"[step] ✓ 생성 완료 ({time.time() - t_gen:.2f}s)", flush=True)

    # 5) 디코딩 (입력 이후 토큰만)
    print("[step] 5. 디코딩 및 (옵션) 후처리", flush=True)
    if out.dim() != 2 or out.shape[0] != 1:
        raise Exception(f"출력 텐서 형태가 이상합니다: {tuple(out.shape)}")

    input_len = input_ids.shape[1]
    output_len = out.shape[1]
    new_tokens = output_len - input_len
    if new_tokens <= 0:
        raise Exception(f"모델이 새 토큰을 생성하지 않았습니다. (input_len={input_len}, output_len={output_len})")

    generated_ids = out[0, input_len:]
    decoded = tok.decode(generated_ids, skip_special_tokens=True).strip()
    if not decoded:
        decoded = tok.decode(out[0], skip_special_tokens=True).strip()
    if not decoded:
        raise Exception("디코딩 결과가 비어 있습니다.")

    # =================================================================
    # 번역 단계: 비한국어가 섞여 있으면 translator로 한국어로 변환
    # =================================================================
    try:
        lang_name, lang_code = detect_language(decoded)
        print(f"[translator] 생성된 시 언어 감지 결과: {lang_name} ({lang_code})", flush=True)

        # 한국어가 아니거나, 언어를 확실히 못 잡은 경우 → 번역 시도
        if lang_code != "ko":
            print("[translator] 생성된 시가 한국어가 아님 → 한국어 번역 시도", flush=True)
            decoded = translate_poem_with_retry(decoded)
        else:
            print("[translator] 생성된 시가 이미 한국어로 인식됨 → 번역 생략", flush=True)
    except Exception as e:
        # 번역 실패해도 최소한 원문은 그대로 사용
        print(
            f"[translator] 번역 과정에서 예외 발생, 원문 그대로 사용: "
            f"{type(e).__name__}: {str(e)[:200]}",
            flush=True,
        )

    # 6) 후처리 오류를 무시하고 최소한 텍스트는 반환
    try:
        poem = _postprocess_poem(decoded, min_lines=lines, max_lines=lines * 3).strip()
        if not poem:
            raise ValueError("후처리 결과가 비었습니다.")
        result_text = poem
        print(f"[done] 최종 시 길이: {len(result_text)}자 (후처리 적용)", flush=True)
    except Exception as e:
        print(f"[warn] _postprocess_poem 예외 → 후처리 없이 원문 사용: {type(e).__name__}: {str(e)[:200]}", flush=True)
        result_text = decoded
        print(f"[done] 최종 시 길이: {len(result_text)}자 (후처리 없이)", flush=True)

    print(f"[done] 총 소요 시간: {time.time() - func_start:.2f}s", flush=True)
    return result_text


# =====================================================================
# 기존 API 호환용 (감정 → 분위기 매핑)
# =====================================================================

def generate_poem(keywords: List[str], emotion: str, max_length: int = 120) -> str:
    """
    감정 레이블을 받아 분위기로 매핑해서 generate_poem_from_keywords를 호출하는
    기존 호환용 래퍼 함수.
    """
    emotion_to_mood = {
        "기쁨": "잔잔한",
        "슬픔": "쓸쓸한",
        "중립": "담담한",
        "사랑": "잔잔한",
        "그리움": "쓸쓸한",
    }
    mood = emotion_to_mood.get(emotion, "담담한")

    max_new = min(
        max_length,
        DEFAULT_MAX_NEW_TOKENS_GPU if _is_gpu() else DEFAULT_MAX_NEW_TOKENS_CPU,
    )

    return generate_poem_from_keywords(
        keywords=keywords,
        mood=mood,
        lines=DEFAULT_LINES,
        max_new_tokens=max_new,
    )
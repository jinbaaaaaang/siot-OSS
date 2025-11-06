# -*- coding: utf-8 -*-
"""
시 생성 메인 함수
"""

import time
import traceback
from typing import List, Optional

import torch

# 번역 모듈 import
from app.services.translator import (
    translate_poem_with_retry,
    detect_language,
)

# 분리된 모듈들 import
from app.services.poem_config import (
    USE_ML_MODEL,
    MODEL_TYPE,
    DEFAULT_LINES,
    DEFAULT_MAX_NEW_TOKENS_GPU,
    DEFAULT_MAX_NEW_TOKENS_CPU,
    DEFAULT_TEMPERATURE,
    DEFAULT_TOP_P,
    DEFAULT_TOP_K,
    DEFAULT_REPETITION_PENALTY,
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


def _log_header(title: str):
    """로깅 헤더 출력"""
    print("[_log_header] 함수 시작", flush=True)
    try:
        print("[_log_header] 첫 번째 print 전", flush=True)
        print("\n" + "=" * 80, flush=True)
        print("[_log_header] 두 번째 print 전", flush=True)
        print(f"[poem_generator] {title}", flush=True)
        print("[_log_header] 세 번째 print 전", flush=True)
        print("=" * 80, flush=True)
        print("[_log_header] 함수 완료", flush=True)
    except Exception as e:
        print(f"[_log_header] 오류 발생: {e}", flush=True)
        import traceback
        traceback.print_exc()
        raise


def _debug_tensor(name: str, tensor: torch.Tensor):
    """텐서 디버깅 정보 출력"""
    try:
        print(f"[debug] {name}: shape={tuple(tensor.shape)}, dtype={tensor.dtype}, device={tensor.device}")
    except Exception:
        print(f"[debug] {name}: <unavailable>")


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
    model_type: Optional[str] = None,  # "solar" 또는 "kogpt2", None이면 기본값 사용
) -> str:
    """
    키워드/분위기 기반 시 생성 (채팅 템플릿 + 4bit 양자화).
    템플릿 폴백 없음 → 실패 시 예외 발생.
    """
    _log_header("시 생성 함수 진입")
    func_start = time.time()
    print(f"[args] keywords={keywords}")
    print(f"[args] mood={mood}, lines={lines}, max_new_tokens={max_new_tokens}")
    print(f"[env] device={_device_info()}, USE_ML_MODEL={USE_ML_MODEL}")

    if not USE_ML_MODEL:
        raise RuntimeError("USE_ML_MODEL=False 상태입니다. 이 구현은 ML 생성만 지원합니다.")

    # 사용할 모델 타입 결정
    from app.services.poem_config import MODEL_TYPE as DEFAULT_MODEL_TYPE
    actual_model_type = (model_type or DEFAULT_MODEL_TYPE).lower()
    if actual_model_type not in ["solar", "kogpt2"]:
        print(f"[generate_poem_from_keywords] ⚠️ 잘못된 모델 타입: {actual_model_type}, 기본값 사용")
        actual_model_type = DEFAULT_MODEL_TYPE

    # 1) 모델 로딩
    print(f"[step] 1. 모델 로딩 (모델 타입: {actual_model_type})")
    tok, model = _load_poem_model(actual_model_type)

    # 2) 프롬프트 구성 및 토크나이즈 (모델 타입에 따라 분기)
    print(f"[step] 2. 프롬프트 구성 및 토크나이즈 (모델 타입: {actual_model_type})")
    t_enc = time.time()
    
    if actual_model_type == "kogpt2":
        # koGPT2는 chat template 없이 일반 토크나이저 사용
        prompt_text = _build_messages_kogpt2(keywords, mood, lines, original_text, banned_words, use_rhyme, acrostic)
        print(f"[step] koGPT2 프롬프트 텍스트:")
        print(f"  {repr(prompt_text[:400])}")
        
        try:
            enc_ids = tok.encode(prompt_text, return_tensors="pt")
            print(f"[step] ✓ 토크나이즈 완료 (길이: {enc_ids.shape[1]} 토큰)")
        except Exception as e:
            print(f"[error] koGPT2 토크나이즈 오류: {e}")
            traceback.print_exc()
            raise Exception(f"프롬프트 토크나이즈 실패: {str(e)[:200]}")
    else:
        # SOLAR는 chat template 사용
        messages = _build_messages(keywords, mood, lines, original_text, banned_words, use_rhyme, acrostic)
        
        # 프롬프트에 키워드가 제대로 반영되었는지 확인
        print(f"[step] 입력 키워드: {keywords}")
        user_msg_content = messages[1]["content"] if len(messages) > 1 else ""
        print(f"[step] 프롬프트에 포함된 키워드 확인:")
        for kw in keywords[:5]:
            if kw in user_msg_content:
                print(f"  ✓ '{kw}' 포함됨")
            else:
                print(f"  ⚠️ '{kw}' 누락됨!")
        
        # 프롬프트 텍스트 미리보기 (디버깅용)
        try:
            prompt_text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            print(f"[step] 최종 프롬프트 텍스트 (앞 400자):")
            print(f"  {repr(prompt_text[:400])}")
            
            prompt_lower = prompt_text.lower()
            keywords_found = [kw for kw in keywords[:5] if kw.lower() in prompt_lower]
            if keywords_found:
                print(f"[step] ✓ 최종 프롬프트에 {len(keywords_found)}개 키워드 포함됨: {keywords_found[:3]}")
            else:
                print(f"[step] ⚠️ 최종 프롬프트에 키워드가 포함되지 않았습니다!")
        except Exception as e:
            print(f"[step] 프롬프트 텍스트 미리보기 실패: {e}")
        
        try:
            enc_result = tok.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
            )
            # apply_chat_template는 return_tensors="pt"일 때 텐서를 반환
            if isinstance(enc_result, torch.Tensor):
                if enc_result.dim() == 1:
                    enc_ids = enc_result.unsqueeze(0)
                elif enc_result.dim() == 2 and enc_result.shape[0] == 1:
                    enc_ids = enc_result
                else:
                    print(f"[warning] 예상치 못한 텐서 형태: {enc_result.shape}, 첫 번째 배치만 사용")
                    enc_ids = enc_result[0:1]
            elif isinstance(enc_result, list):
                enc_ids = torch.tensor([enc_result], dtype=torch.long)
            else:
                enc_ids = torch.tensor([[enc_result]], dtype=torch.long)
            
            enc_ids = enc_ids.to(dtype=torch.long)
            
            if enc_ids.shape[0] != 1:
                raise Exception(f"입력 텐서의 배치 크기가 1이 아닙니다: {enc_ids.shape}")
            if enc_ids.shape[1] < 10:
                raise Exception(f"입력 텐서가 너무 짧습니다: {enc_ids.shape[1]} 토큰")
            if enc_ids.shape[1] > 2048:
                print(f"[warning] ⚠️ 입력 텐서가 매우 깁니다: {enc_ids.shape[1]} 토큰")
        except Exception as e:
            print(f"[error] chat 템플릿 적용 오류: {e}")
            traceback.print_exc()
            raise Exception(f"프롬프트 토크나이즈 실패: {str(e)[:200]}")
    
    print(f"[step] ✓ 토크나이즈 완료 ({time.time() - t_enc:.2f}s)")
    _debug_tensor("input_ids(raw)", enc_ids)

    # device_map=auto 일 때 모델 파라미터 device로 이동
    try:
        model_device = next(model.parameters()).device
        print(f"[step] 모델 device 확인: {model_device}")
    except StopIteration:
        print("[error] ❌ 모델 파라미터를 찾을 수 없습니다!")
        raise Exception("모델이 제대로 로드되지 않았습니다. 모델 로딩 상태를 확인하세요.")
    
    # input_ids를 모델 device로 이동 (메모리 효율을 위해 필요한 시점에만)
    try:
        input_ids = enc_ids.to(model_device)
        _debug_tensor("input_ids(final)", input_ids)
    except RuntimeError as e:
        error_msg = str(e)
        print(f"[error] ❌ input_ids를 device로 이동 실패: {error_msg}")
        if "out of memory" in error_msg.lower():
            raise Exception(f"GPU 메모리 부족으로 input_ids를 이동할 수 없습니다. 런타임을 재시작하세요.")
        raise Exception(f"Device 이동 실패: {error_msg[:200]}")
    
    # attention_mask 생성 (패딩 토큰 문제 방지)
    # input_ids와 같은 shape으로 모든 값을 1로 설정 (패딩 없음)
    try:
        attention_mask = torch.ones_like(input_ids, dtype=torch.long, device=model_device)
        print(f"[step] attention_mask 생성: shape={tuple(attention_mask.shape)}, dtype={attention_mask.dtype}, device={attention_mask.device}")
    except RuntimeError as e:
        error_msg = str(e)
        print(f"[error] ❌ attention_mask 생성 실패: {error_msg}")
        if "out of memory" in error_msg.lower():
            raise Exception(f"GPU 메모리 부족으로 attention_mask를 생성할 수 없습니다.")
        raise Exception(f"attention_mask 생성 실패: {error_msg[:200]}")

    # 3) 생성 파라미터 확정
    print("[step] 3. 생성 파라미터 설정")
    is_gpu = _is_gpu()
    # max_new_tokens는 호출자가 지정한 값 사용 (GPU: 150, CPU: 기본값)
    safe_max_new = max_new_tokens
    
    # 모델 타입에 따라 최소값 조정
    if actual_model_type == "kogpt2":
        min_required = max(30, lines * 8)  # koGPT2: 충분한 길이 보장
    else:
        min_required = max(30, lines * 8)  # SOLAR는 더 긴 생성 가능
    
    if safe_max_new < min_required:
        print(f"[warning] max_new_tokens({safe_max_new})가 너무 작습니다. 최소 {min_required}로 조정합니다.", flush=True)
        safe_max_new = min_required
    
    if is_gpu:
        if actual_model_type == "kogpt2":
            safe_max_new = min(safe_max_new, 100)  # koGPT2 GPU: 100토큰으로 증가 (더 나은 시 생성)
        else:
            safe_max_new = min(safe_max_new, 100)  # SOLAR GPU: 100토큰 제한
    else:
        if actual_model_type == "kogpt2":
            safe_max_new = min(safe_max_new, 60)  # koGPT2 CPU: 60토큰으로 증가
        else:
            safe_max_new = min(safe_max_new, DEFAULT_MAX_NEW_TOKENS_CPU)  # SOLAR CPU: 24토큰 제한
    
    print(f"[step] 최종 max_new_tokens: {safe_max_new} (요청: {max_new_tokens}, 최소: {min_required})")

    # 생성 파라미터 구성 (안정적인 설정)
    gen_kwargs = {
        "input_ids": input_ids,
        "attention_mask": attention_mask,  # 패딩 토큰 문제 방지
        "max_new_tokens": safe_max_new,
        "eos_token_id": tok.eos_token_id,
        "pad_token_id": tok.pad_token_id or tok.eos_token_id,
    }
    
    # GPU 메모리 상태 확인 (디버깅용)
    if _is_gpu():
        try:
            mem_allocated = torch.cuda.memory_allocated(0) / (1024**3)
            mem_reserved = torch.cuda.memory_reserved(0) / (1024**3)
            print(f"[step] GPU 메모리 (생성 전): 할당={mem_allocated:.2f}GB, 캐시={mem_reserved:.2f}GB")
        except:
            pass
    
    # 모델 타입과 디바이스에 따라 생성 파라미터 조정
    if actual_model_type == "kogpt2":
        # koGPT2는 작은 모델이므로 프롬프트를 더 잘 따르도록 파라미터 조정
        if is_gpu:
            gen_kwargs.update({
                "do_sample": True,
                "temperature": 0.5,  # 더 낮춰서 프롬프트를 더 잘 따르도록
                "top_p": 0.75,        # 더 제한적인 후보 선택
                "top_k": 25,          # 더 적은 후보 고려
                "repetition_penalty": 1.3,  # 반복 방지 더 강화
                "no_repeat_ngram_size": 2,  # 2-gram 반복 방지
            })
        else:
            # CPU에서도 샘플링 사용
            gen_kwargs.update({
                "do_sample": True,
                "temperature": 0.45,   # 더 낮춰서 프롬프트를 더 잘 따르도록
                "top_p": 0.7,
                "top_k": 20,
                "repetition_penalty": 1.3,  # 반복 방지 강화
                "no_repeat_ngram_size": 2,  # 2-gram 반복 방지
            })
    else:
        # SOLAR 모델
        if is_gpu:
            # 빠른 생성: 샘플링 파라미터를 최적화하여 속도 향상
            gen_kwargs.update({
                "do_sample": True,
                "temperature": DEFAULT_TEMPERATURE,  # 0.7로 낮춰서 더 결정적으로 생성
                "top_p": DEFAULT_TOP_P,              # 0.85로 낮춰서 후보 제한
                "top_k": DEFAULT_TOP_K,              # 30으로 낮춰서 후보 제한
                "repetition_penalty": DEFAULT_REPETITION_PENALTY,  # 1.05로 완화
                # num_beams=1 (빠른 생성, 기본값)
            })
        else:
            # CPU에서는 greedy 디코딩 (더 빠름)
            gen_kwargs.update({
                "do_sample": False,
            })
    print("[gen_kwargs]", {k: (v if not isinstance(v, torch.Tensor) else f"Tensor(shape={tuple(v.shape)})")
                            for k, v in gen_kwargs.items()})

    # 4) 생성
    print("[step] 4. model.generate() 호출")
    print(f"[step] 생성 파라미터 요약:")
    print(f"   - max_new_tokens: {safe_max_new}")
    print(f"   - do_sample: {gen_kwargs.get('do_sample', False)}")
    print(f"   - device: {model_device}")
    
    t_gen = time.time()
    try:
        out = model.generate(**gen_kwargs)
    except RuntimeError as e:
        error_msg = str(e)
        print(f"[error] generate() RuntimeError 발생")
        print(f"[error] 오류 메시지: {error_msg}")
        traceback.print_exc()
        
        # 메모리 부족 오류 체크
        if "out of memory" in error_msg.lower() or "cuda" in error_msg.lower():
            raise Exception(f"GPU 메모리 부족 또는 CUDA 오류입니다: {error_msg[:200]}")
        else:
            raise Exception(f"모델 생성 중 런타임 오류: {error_msg[:200]}")
    except ValueError as e:
        error_msg = str(e)
        print(f"[error] generate() ValueError 발생")
        print(f"[error] 오류 메시지: {error_msg}")
        traceback.print_exc()
        raise Exception(f"생성 파라미터 오류입니다: {error_msg[:200]}")
    except Exception as e:
        error_msg = str(e)
        print(f"[error] generate() 예외 발생: {type(e).__name__}")
        print(f"[error] 오류 메시지: {error_msg}")
        traceback.print_exc()
        raise Exception(f"시 생성 중 오류가 발생했습니다: {type(e).__name__}: {error_msg[:200]}")
    gen_sec = time.time() - t_gen
    print(f"[step] ✓ 생성 완료 ({gen_sec:.2f}s)")
    try:
        print(f"[debug] output shape={tuple(out.shape)}, device={out.device}")
        # GPU 메모리 상태 확인 (디버깅용)
        if _is_gpu():
            mem_allocated = torch.cuda.memory_allocated(0) / (1024**3)
            mem_reserved = torch.cuda.memory_reserved(0) / (1024**3)
            print(f"[step] GPU 메모리 (생성 후): 할당={mem_allocated:.2f}GB, 캐시={mem_reserved:.2f}GB")
    except Exception:
        pass

    # 5) 디코딩 (프롬프트 길이 이후만)
    print("[step] 5. 디코딩 및 후처리")
    input_len = input_ids.shape[1]
    
    # 출력 검증
    if out.shape[0] != 1:
        print(f"[error] ❌ 출력 배치 크기가 1이 아닙니다: {out.shape}")
        raise Exception(f"출력 텐서 형태 오류: {out.shape}")
    
    output_len = out.shape[1]
    new_tokens = output_len - input_len
    
    print(f"[debug] 입력 길이: {input_len} 토큰, 출력 길이: {output_len} 토큰")
    print(f"[debug] 생성된 새 토큰 수: {new_tokens}")
    
    # 생성된 토큰 수 확인
    if new_tokens <= 0:
        print(f"[error] ❌ 모델이 새로운 토큰을 생성하지 않았습니다!")
        print(f"[error] 입력 토큰 수: {input_len}, 출력 토큰 수: {output_len}")
        print(f"[error] 생성 파라미터를 확인하세요 (max_new_tokens={safe_max_new})")
        
        # 전체 출력을 디코딩해서 확인
        try:
            full_decoded = tok.decode(out[0], skip_special_tokens=False)
            print(f"[error] 전체 출력 (처음 500자): {repr(full_decoded[:500])}")
            print(f"[error] 전체 출력 (마지막 500자): {repr(full_decoded[-500:])}")
        except:
            pass
        
        raise Exception(f"모델이 새로운 토큰을 생성하지 않았습니다. (입력: {input_len}, 출력: {output_len} 토큰)")
    
    if new_tokens < 5:
        print(f"[warning] ⚠️ 생성된 토큰이 매우 적습니다 ({new_tokens} 토큰)")
    
    # 생성된 부분만 디코딩 (input_len 이후)
    try:
        # 방법 1: 슬라이싱으로 생성된 부분만 디코딩
        generated_ids = out[0][input_len:]
        # 깨진 문자 방지를 위해 errors='replace' 사용 (나중에 후처리에서 제거)
        decoded = tok.decode(generated_ids, skip_special_tokens=True, errors='replace').strip()
        
        print(f"[debug] 생성된 토큰 ID 샘플 (처음 10개): {generated_ids[:10].tolist()}")
        print(f"[debug] decoded(앞 300자): {repr(decoded[:300])}")
        print(f"[debug] decoded 전체 길이: {len(decoded)}자")
        
        # 디코딩 결과가 너무 짧으면 경고
        if len(decoded.strip()) < 10:
            print(f"[warning] ⚠️ 디코딩 결과가 매우 짧습니다: {len(decoded)}자")
            # 전체 출력을 다시 확인
            try:
                full_decoded = tok.decode(out[0], skip_special_tokens=False)
                print(f"[debug] 전체 출력 확인 (마지막 200자): {repr(full_decoded[-200:])}")
                
                # 생성된 부분을 다른 방법으로 추출 시도
                if input_len < output_len:
                    # 방법 2: 전체 디코딩 후 입력 부분 제거 시도
                    full_decoded_clean = tok.decode(out[0], skip_special_tokens=True, errors='replace')
                    # 입력 프롬프트를 디코딩
                    input_decoded = tok.decode(input_ids[0], skip_special_tokens=True, errors='replace')
                    if full_decoded_clean.startswith(input_decoded):
                        decoded_alt = full_decoded_clean[len(input_decoded):].strip()
                        print(f"[debug] 대체 디코딩 방법 결과 (앞 300자): {repr(decoded_alt[:300])}")
                        if len(decoded_alt) > len(decoded):
                            print("[debug] 대체 방법이 더 긴 결과를 반환했습니다. 이를 사용합니다.")
                            decoded = decoded_alt
            except Exception as e2:
                print(f"[warning] 대체 디코딩 시도 실패: {e2}")
                
    except Exception as e:
        print(f"[error] 디코딩 오류: {e}")
        traceback.print_exc()
        
        # 대체 방법 시도
        try:
            print("[debug] 대체 디코딩 방법 시도 중...")
            decoded = tok.decode(out[0], skip_special_tokens=True, errors='replace').strip()
            # 입력 프롬프트 길이만큼 앞부분 제거 시도
            if len(decoded) > input_len * 2:  # 대략적인 추정
                decoded = decoded[input_len * 2:].strip()  # 토큰 대비 문자 비율 고려
            print(f"[debug] 대체 디코딩 결과: {repr(decoded[:300])}")
        except Exception as e2:
            print(f"[error] 대체 디코딩도 실패: {e2}")
            raise Exception(f"디코딩 중 오류가 발생했습니다: {str(e)[:200]}")
    
    if not decoded or len(decoded.strip()) == 0:
        print(f"[error] ❌ 디코딩 결과가 비어있습니다!")
        print(f"[error] 생성된 토큰 수: {new_tokens}")
        # 원본 출력 일부 확인 (디버깅용)
        if new_tokens > 0:
            try:
                raw_decoded = tok.decode(out[0], skip_special_tokens=False)
                print(f"[error] 전체 디코딩 (skip_special_tokens=False, 처음 500자): {repr(raw_decoded[:500])}")
                print(f"[error] 전체 디코딩 (skip_special_tokens=False, 마지막 500자): {repr(raw_decoded[-500:])}")
            except:
                pass
        raise Exception("디코딩 결과가 비어있습니다. 생성 파라미터를 확인하세요.")

    poem = _postprocess_poem(decoded, min_lines=lines, max_lines=lines * 3)
    poem = poem.strip()
    print("[debug] postprocessed(앞 200자):", repr(poem[:200]))
    print("[debug] 생성된 텍스트 전체:", repr(poem))
    # 생성된 텍스트의 언어 확인
    korean_debug = sum(1 for c in poem if ord('가') <= ord(c) <= ord('힣'))
    chinese_debug = sum(1 for c in poem if ord('\u4e00') <= ord(c) <= ord('\u9fff'))
    print(f"[debug] 언어 분석: 한국어={korean_debug}자, 중국어={chinese_debug}자")

    # 6) 검증: 내용이 있는지, 한글 포함 여부 간단 체크
    if not poem or len(poem.strip()) == 0:
        print("[check] ❌ 생성된 시가 비어있음")
        print(f"[check] 원본 디코딩 결과: {repr(decoded[:500])}")
        raise Exception("시 생성에 실패했습니다. 생성된 내용이 없습니다.")
    
    # 한글이 없어도 내용이 있으면 허용
    korean_chars = sum(1 for c in poem if ord('가') <= ord(c) <= ord('힣'))
    print(f"[check] 최종 시 길이={len(poem)}자, 한글문자수={korean_chars}자")
    
    # 최소 한 글자 이상은 있어야 함
    if len(poem.strip()) < 1:
        raise Exception("시 생성에 실패했습니다. 생성된 내용이 너무 짧습니다.")
    
    # 7) 한국어 검증
    print("[check] 한국어 검증:")
    korean_chars = sum(1 for c in poem if ord('가') <= ord(c) <= ord('힣'))
    total_chars = len([c for c in poem if c.strip()])
    korean_ratio = korean_chars / total_chars if total_chars > 0 else 0
    
    print(f"[check] 한국어 문자 수: {korean_chars}자 / 전체 문자 수: {total_chars}자 (비율: {korean_ratio:.2%})")
    
    # 다른 언어 문자 확인
    chinese_chars = sum(1 for c in poem if ord('\u4e00') <= ord(c) <= ord('\u9fff'))
    japanese_hiragana = sum(1 for c in poem if ord('\u3040') <= ord(c) <= ord('\u309f'))
    japanese_katakana = sum(1 for c in poem if ord('\u30a0') <= ord(c) <= ord('\u30ff'))
    japanese_chars = japanese_hiragana + japanese_katakana
    english_chars = sum(1 for c in poem if c.isalpha() and ord('a') <= ord(c.lower()) <= ord('z'))
    
    # 언어 감지
    detected_lang_name, detected_lang_code = detect_language(poem)
    
    if chinese_chars > 0:
        print(f"[check] ⚠️ 중국어 문자 감지: {chinese_chars}자")
    if japanese_chars > 0:
        print(f"[check] ⚠️ 일본어 문자 감지: 히라가나 {japanese_hiragana}자, 가타카나 {japanese_katakana}자")
    if english_chars > total_chars * 0.5 and korean_chars < total_chars * 0.3:
        print(f"[check] ⚠️ 영어 텍스트 감지: {english_chars}자")
    print(f"[check] 감지된 언어: {detected_lang_name} (코드: {detected_lang_code})")
    
    # 한국어가 아니거나 한국어 비율이 낮으면 번역 필요
    needs_translation = (
        detected_lang_code != "ko" or  # 한국어가 아님
        (korean_chars == 0 and total_chars > 5) or  # 한국어가 하나도 없음
        (korean_ratio < 0.5 and total_chars > 10)  # 한국어 비율이 50% 미만
    )
    
    # ===== 비한국어 감지 시 무조건 한국어로 번역 =====
    # 한국어가 아니거나 비한국어가 감지되면 번역
    needs_translation_or_other_language = needs_translation or (
        chinese_chars > 0 or 
        japanese_chars > 0 or 
        (english_chars > total_chars * 0.3 and korean_chars < total_chars * 0.5) or
        (korean_ratio < 0.7 and total_chars > 10)
    )
    
    if needs_translation_or_other_language:
        # translator 모듈의 translate_poem_with_retry 함수 사용 (재시도 로직 포함)
        poem = translate_poem_with_retry(poem, max_retries=5)
        
        # 번역 후 언어 분석 재실행
        korean_chars = sum(1 for c in poem if ord('가') <= ord(c) <= ord('힣'))
        chinese_chars = sum(1 for c in poem if ord('\u4e00') <= ord(c) <= ord('\u9fff'))
        japanese_hiragana = sum(1 for c in poem if ord('\u3040') <= ord(c) <= ord('\u309f'))
        japanese_katakana = sum(1 for c in poem if ord('\u30a0') <= ord(c) <= ord('\u30ff'))
        japanese_chars = japanese_hiragana + japanese_katakana
        english_chars = sum(1 for c in poem if c.isalpha() and ord('a') <= ord(c.lower()) <= ord('z'))
        total_chars = len([c for c in poem if c.strip()])
        korean_ratio = korean_chars / total_chars if total_chars > 0 else 0
    
    # 한국어 비율이 너무 낮으면 경고
    if korean_ratio < 0.5 and total_chars > 10:
        print(f"[check] ⚠️ 한국어 비율이 낮습니다 ({korean_ratio:.2%})")
        if chinese_chars > 0:
            print(f"[check] ⚠️ 중국어가 포함되어 있습니다. 재생성을 권장합니다.")
    
    # 키워드 반영 여부 확인 (참고용, 강제하지는 않음)
    print("[check] 키워드 반영 여부 확인:")
    poem_lower = poem.lower()
    keywords_in_poem = []
    for kw in keywords[:5]:
        kw_lower = kw.lower()
        # 키워드가 시에 포함되어 있는지 확인 (부분 문자열 포함도 허용)
        if kw_lower in poem_lower:
            keywords_in_poem.append(kw)
            print(f"  ✓ 키워드 '{kw}' 반영됨")
        else:
            # 키워드의 일부라도 포함되는지 확인 (2글자 이상인 경우)
            if len(kw) >= 2:
                found_partial = False
                for i in range(len(kw) - 1):
                    if kw[i:i+2].lower() in poem_lower:
                        found_partial = True
                        print(f"  ~ 키워드 '{kw}' 일부 반영됨 (참고)")
                        break
                if not found_partial:
                    print(f"  ⚠️ 키워드 '{kw}' 직접 반영 안 됨 (의미적으로는 포함될 수 있음)")
            else:
                print(f"  ⚠️ 키워드 '{kw}' 직접 반영 안 됨 (의미적으로는 포함될 수 있음)")
    
    if keywords_in_poem:
        print(f"[check] ✓ {len(keywords_in_poem)}개 키워드가 시에 반영됨")
    else:
        print(f"[check] ⚠️ 키워드가 직접적으로 보이지 않지만, 의미적으로는 반영되었을 수 있습니다.")

    print(f"[done] 총 소요 시간: {time.time() - func_start:.2f}s")
    return poem


def generate_poem(keywords: List[str], emotion: str, max_length: int = 120) -> str:
    """
    기존 API 호환: 감정 → 분위기 매핑 후 시 생성.
    """
    emotion_to_mood = {
        "기쁨": "잔잔한",
        "슬픔": "쓸쓸한",
        "중립": "담담한",
        "사랑": "잔잔한",
        "그리움": "쓸쓸한",
    }
    mood = emotion_to_mood.get(emotion, "담담한")
    max_new = min(max_length, DEFAULT_MAX_NEW_TOKENS_GPU if _is_gpu() else DEFAULT_MAX_NEW_TOKENS_CPU)
    return generate_poem_from_keywords(
        keywords=keywords,
        mood=mood,
        lines=DEFAULT_LINES,
        max_new_tokens=max_new,
    )

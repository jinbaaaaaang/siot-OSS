⡤⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⢤   
⢣⡀⠀⠉⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⠉⠀⢀⡜   
⢸⡉⠒⠄⠀⠀⠀⢉⡙⢢⠀⠀⡔⢋⡉⠀⠀⠀⠠⠒⢉⡇   
⠀⠉⢖⠒⠀⠀⠀⣇⠀⣸⠀⠀⣇⠀⣸⠀⠀⠀⠒⡲⠉   
⠀⠀⠀⠀⠉⠙⠫⠤⠚⠉⠀⠀⠀⠀⠉⠓⠤⠝⠋⠉   

# <img src="./frontend/public/favicon.svg" alt="siot favicon" width="28" style="vertical-align:middle; margin-right:6px;" /> 시옷 (SIOT) - 일기를 시로 변환하는 웹 애플리케이션

︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹

**AI 기반 한국어 시 생성 플랫폼**  
일상의 내용을 담은 일기를 시로 변환하는 웹 애플리케이션입니다. SOLAR-10.7B-Instruct와 파인튜닝된 koGPT2 모델을 활용하여 고품질의 한국어 시를 생성합니다.

---

## ☆ 목차

- [☆ 시연 과정 가이드](#-시연-과정-가이드-설명-전용)
- [☆ 프로젝트 소개](#-프로젝트-소개)
- [☆ 시연 과정 가이드 (설명 전용)](#-시연-과정-가이드-설명-전용)
- [☆ 프로젝트 구조](#-프로젝트-구조)
- [☆ 주요 파일 설명](#-주요-파일-설명)
- [☆ 아키텍처](#-아키텍처)
- [☆ 기술 스택](#-기술-스택)
- [☆ 기능](#-기능)
- [☆ 설치 및 설정](#-설치-및-설정)
- [☆ 실행 방법](#실행-방법)
- [☆ API 문서](#api-문서)
- [☆ 개발 가이드](#-개발-가이드)
- [☆ 프론트엔드 사용 흐름](#-프론트엔드-사용-흐름)
- [☆ 데이터 시각화](#데이터-시각화)
- [☆ 기여 가이드](#기여-가이드)
- [☆ 라이선스](#-라이선스)
- [☆ FAQ (자주 묻는 질문)](#-faq-자주-묻는-질문)
- [☆ 추가 자료](#-추가-자료)
- [☆ 감사의 말](#-감사의-말)

---

## ☆ 프로젝트 소개

## 프로젝트 개요

**시옷(SIOT)**은 사용자의 일기를 분석하여 감성을 담은 한국어 시로 변환하는 AI 기반 웹 애플리케이션입니다. 일상의 기록, 감정, 생각을 시로 표현하고 싶지만 시 창작에 어려움을 느끼는 사람들을 위해 개발되었으며, 최신 AI 기술을 활용해 누구나 쉽게 자신만의 시를 생성할 수 있도록 돕습니다.

## ☆ 시연 과정

### 1. 시작 및 화면 소개

시옷은 일기를 시로 변환하는 웹 애플리케이션입니다. 메인 화면인 PoemGeneration 페이지에서는 상단에 SOLAR와 koGPT2 두 가지 모델을 선택할 수 있는 버튼이 있고, 아래에는 일상을 입력할 수 있는 텍스트 영역이 있습니다.

### 2. 입력 및 모델 선택

오늘 하루 있었던 일을 간단히 적어봅니다. 예를 들어 "오늘 날씨가 좋아서 산책을 했다. 친구와 함께 커피를 마시며 이야기를 나눴다" 같은 일상적인 내용이면 됩니다. 입력이 비어있으면 버튼이 비활성화되어 입력 검증이 이루어집니다. SOLAR 모델은 GPU 환경에서 더 고품질의 시를 생성하는 모델이고, koGPT2는 CPU 환경에서도 사용할 수 있는 모델입니다.

### 3. 시 생성 과정

"시 생성하기" 버튼을 클릭하면 로딩 애니메이션이 나타나고 "시 생성 중..."이라는 메시지가 표시됩니다. 시 생성에는 몇 초에서 수십 초가 걸릴 수 있습니다.

백엔드에서는 입력된 텍스트를 분석하여 키워드를 추출하고, 감정을 분류한 다음, AI 모델이 시를 생성합니다. 추출된 키워드와 분류된 감정은 시 생성 프롬프트에 포함되어 최종 시의 내용과 분위기에 반영됩니다.

### 4. 결과 확인

시가 생성되면 화면에 여러 정보가 카드 형태로 표시됩니다. 생성된 시 본문이 가장 위에 표시되고, 그 아래에는 감정 분석 결과가 나타납니다. 예를 들어 "기쁨"이라는 감정이 0.85의 신뢰도로 분류되었다는 정보가 표시됩니다. 추출된 키워드들도 함께 보여지며, 각 키워드는 시 생성 시 프롬프트에 포함되어 시의 내용에 반영됩니다. 이 시는 자동으로 브라우저의 localStorage에 저장되며, 필요하면 "보관함에 저장" 버튼을 눌러 수동으로도 저장할 수 있습니다.

### 5. 감정 추이 시각화

상단 메뉴에서 EmotionTrend 페이지로 이동하면 생성한 시들의 감정 데이터를 시각화하여 볼 수 있습니다. 최근 7일간의 감정 추이를 라인 차트로 보여주고, 전체 기간의 감정 분포를 파이 차트로, 감정 신뢰도 분포를 바 차트로 확인할 수 있습니다. 방금 생성한 시의 감정이 차트에 반영되어 시간에 따른 감정 변화 패턴을 한눈에 파악할 수 있습니다.

### 6. 보관함 및 설정

Archive 페이지로 이동하면 지금까지 생성하고 저장한 모든 시를 시간순으로 볼 수 있습니다. 각 시를 클릭하면 복사하거나 삭제할 수 있습니다. Settings 페이지에서는 기본 모델을 선택하거나 자동 저장 기능을 켜고 끌 수 있습니다. 설정을 변경하면 다음 시 생성부터 적용됩니다.

### 마무리

시옷은 일상의 기록을 시로 변환하고, 키워드 추출과 감정 분류를 통해 텍스트를 분석한 후, AI 모델이 시를 생성합니다. 생성된 시와 감정 분석 결과는 자동으로 저장되어 시각화를 통해 감정 패턴을 확인할 수 있습니다. 복잡한 설정 없이 간단하게 시를 만들어볼 수 있고, 자신의 감정 패턴도 확인할 수 있는 도구입니다.

## 프로젝트 배경 및 목적

### 시옷을 만들게 된 이유

일상에서 일기나 메모를 쓰다 보면, 시간이 지나 다시 읽어봤을 때 그때의 감정이 제대로 전달되지 않는 아쉬움이 있습니다. 단순한 텍스트로만 남아있어서 그 의미가 희미해지는 것이죠. 이러한 일상의 기록들을 **시**로 변환하면 어떨까 하는 생각에서 시작했습니다. 시는 감정을 압축하고, 핵심만 남기며, 시간이 지나도 그 느낌을 간직할 수 있기 때문입니다.

하지만 시를 직접 써보려고 하면 막막한 경우가 많습니다. 감정은 있지만 어떻게 표현해야 할지 모르겠고, 운율이나 형식 같은 것도 부담스럽습니다. 그래서 AI를 활용하여 누구나 쉽게 시를 만들어볼 수 있는 도구를 만들고자 했습니다. 복잡한 설정 없이, 오늘 하루 있었던 일을 적으면 시가 나오는 그런 경험을 제공하고 싶었습니다.

시옷은 이런 고민에서 시작했습니다. 일상의 기록을 더 의미 있게 보존하고 싶은 사람들, 시를 쓰고 싶지만 어려워하는 사람들을 위한 도구가 되고자 합니다.

### 핵심 가치와 활용 장면

**가벼운 시작**  
긴 글을 쓸 필요가 없습니다. 오늘 점심에 무엇을 먹었는지, 날씨가 어땠는지 같은 작은 일상 몇 줄만 적어도 시가 생성됩니다. 일기처럼 생각나는 대로 적으면 되므로 부담이 적습니다.

**내 목소리 그대로**  
모델을 선택할 수 있고, 분위기나 줄 수도 조절할 수 있습니다. 같은 내용이라도 SOLAR로 만들면 더 함축적인 느낌이 나고, koGPT2로 만들면 더 현대적인 느낌이 납니다. 누구에게 보여줄지, 어떤 톤으로 남길지에 따라 선택하면 됩니다.

**기억 정리와 보관**  
산문으로 흩어져 있던 감정들을 시로 압축해두면, 나중에 다시 읽어봤을 때 그때의 핵심만 남아있습니다. 자동으로 번역도 되고, 표현도 다듬어지므로 더 깔끔하게 보관할 수 있습니다.

**감정 들여다보기**  
생성된 시마다 감정 분석 결과가 함께 제공됩니다. 이를 차트로 모아보면 며칠간의 감정 변화를 한눈에 확인할 수 있습니다. 가끔 "이번 주에는 슬픈 시를 많이 만들었구나" 같은 패턴을 발견하기도 합니다.

**창작 연습 파트너**  
시를 쓰고 싶은데 아이디어가 막힐 때도 활용할 수 있습니다. 키워드나 분위기만 지정하여 초안을 받아보고, 거기서 시작해서 고쳐나가면 됩니다. 다양한 설정을 바꿔보면서 "이렇게 하면 어떤 느낌이 나지?" 같은 실험도 가능합니다.

## 작동 원리

시옷은 다음과 같은 단계로 일상글을 시로 변환합니다:

1. **텍스트 분석** – TF-IDF로 핵심 키워드를 추출하고, XNLI 기반 제로샷 학습으로 감정을 분류하며 감정 신뢰도를 계산합니다.
2. **프롬프트 구성** – 키워드와 감정, 사용자 옵션(줄 수, 분위기, 운율 등)을 조합해 모델별 최적화된 프롬프트를 생성합니다.
3. **시 생성** – SOLAR-10.7B-Instruct 또는 파인튜닝된 koGPT2 모델이 GPU/CPU 환경에 맞춰 자동으로 선택되어 시를 생성합니다.
4. **후처리 및 개선** – 자동 줄바꿈, 산문 필터링, 불필요한 텍스트 제거, Gemini API 기반 시 개선, 자동 번역을 수행합니다.
5. **결과 제공** – 완성된 시를 사용자에게 전달하고 감정 데이터를 저장해 감정 추이 시각화에 활용합니다.

## 주요 특징

### ☆ 다중 AI 모델 지원

- **SOLAR-10.7B-Instruct**: GPU 환경에서 고품질 시 생성 (약 10.7B 파라미터)  
- **파인튜닝된 koGPT2**: CPU 환경에서도 고품질 시 생성 가능 (KPoEM 데이터셋으로 학습)  
- **기본 koGPT2**: 빠른 프로토타이핑 및 테스트용  

시스템이 자동으로 GPU/CPU 환경을 감지하여 최적의 모델을 선택합니다.

### ☆ 지능형 감정 분석

- **XNLI 기반 제로샷 학습**으로 별도 학습 없이 감정 분류  
- **다양한 감정 인식**: 기쁨, 슬픔, 중립, 사랑, 그리움 등  
- **신뢰도 제공**: 감정 분류의 신뢰도를 수치로 제공  
- **분위기 매핑**: 감정을 시의 분위기(잔잔한/담담한/쓸쓸한)로 자동 변환

> **제로샷 분류란?**  
> 레이블이 붙은 학습 데이터 없이도 미리 학습된 언어모델이 자연어 레이블을 비교해 감정을 판별하는 방식입니다. 시옷은 Hugging Face XNLI 모델에 “이 문장은 기쁨/슬픔 중 무엇에 가까운가?” 같은 질의를 던져 결과를 얻습니다.

### ☆ 자동 번역 기능

AI 모델이 비한국어로 시를 생성한 경우, Google Cloud Translation API를 통해 자동으로 한국어로 번역합니다. 이를 통해 항상 한국어 시를 제공할 수 있습니다.

### ☆ 감정 추이 시각화

생성된 시들의 감정 데이터를 수집하여 다음과 같은 시각화를 제공합니다:

- **최근 7일 감정 추이** – 일주일간 감정 변화를 라인 차트로 표시  
- **감정 분포** – 전체 기간 동안의 감정 비율을 파이 차트로 표시  
- **감정 신뢰도 분포** – 감정 분석의 신뢰도를 바 차트로 표시  
- **전체 기간 감정 추이** – 모든 시 생성 기록의 감정 변화 추이

### ☆ Gemini 기반 후처리

감정 데이터를 Gemini API를 활용하여 사용자 친화적인 스토리로 변환합니다. 단순한 통계가 아닌 자연스러운 문장으로 감정 패턴을 설명합니다.

## 기술적 특징

### 하이브리드 AI 접근

- **시 생성**: SOLAR, koGPT2  
- **감정 분류**: 제로샷 감정 분석 (XNLI)  
- **키워드 추출**: TF-IDF  
- **후처리**: Gemini API  
- **번역**: Google Cloud Translation  

### 확장 가능한 아키텍처

- **서비스 지향 아키텍처(SOA)** – 기능별 독립 서비스  
- **모듈화된 코드 구조** – 기능 추가 및 수정 용이  
- **환경별 최적화** – GPU/CPU 환경에 맞춰 자동 모델 선택

### 사용자 경험 중심 설계

- **직관적인 UI** – 복잡한 설정 없이 간단하게 시 생성  
- **실시간 피드백** – 시 생성 과정을 시각적으로 표시  
- **데이터 시각화** – 감정 추이를 차트로 확인하여 직관적 이해

### 사용 모델 상세

- **SOLAR-10.7B-Instruct**  
  - Upstage가 공개한 107억 파라미터급 한국어/영어 LLM입니다. 긴 문맥을 잃지 않고 함축적인 시어를 만드는 능력이 뛰어나며, Colab GPU에서 bitsandbytes 4bit NF4 양자화를 적용해 VRAM 사용량을 최소화합니다. 시옷은 instruct 프롬프트와 세밀한 샘플링 파라미터를 함께 사용해 줄 수·분위기·필수 키워드를 자연스럽게 반영합니다.

- **koGPT2-base-v2 (파인튜닝)**  
  - SKT koGPT2를 KPoEM 데이터셋으로 k-fold fine-tuning 해 CPU에서도 시다운 표현을 유지하게 만들었습니다. Temperature 0.65, Top-p 0.85, 반복 패널티 1.6 등 시 특화 하이퍼파라미터를 적용했고, `trained_models/`에 fold별 체크포인트를 보관해 로컬 FastAPI가 즉시 불러옵니다. 줄 수·분위기·필수 키워드 옵션에 특히 민감해 사용자가 원하는 스타일을 섬세하게 조절할 수 있습니다.

- **XNLI 기반 제로샷 감정 분류기**  
  - XLM-RoBERTa-large-XNLI 모델을 사용하여 제로샷 감정 분류를 수행합니다. 제로샷 분류는 별도의 학습 데이터 없이도 미리 학습된 모델이 자연어 레이블을 비교하여 감정을 판별하는 방식입니다.
  - 입력 텍스트와 13가지 감정 라벨(기쁨, 슬픔, 사랑, 그리움, 분노, 놀람, 두려움, 혐오, 평온, 불안, 희망, 실망, 중립)을 비교합니다.
  - 모델은 "이 문장은 기쁨에 가까운가, 슬픔에 가까운가?" 같은 형태로 각 감정과의 유사도를 계산합니다.
  - 각 감정에 대한 신뢰도 점수를 0과 1 사이의 값으로 제공하며, 가장 높은 점수를 받은 감정이 최종 분류 결과가 됩니다. 예를 들어 "기쁨"이 0.85, "사랑"이 0.12, "중립"이 0.03의 점수를 받았다면 "기쁨"이 선택되고 신뢰도는 0.85가 됩니다.
  - 분류된 감정은 자동으로 시의 분위기로 매핑됩니다. 예를 들어 "기쁨"은 "밝은", "슬픔"은 "쓸쓸한", "사랑"은 "따뜻한" 분위기로 변환됩니다.
  - 감정 후보 문자열만 바꾸면 새로운 레이블도 재학습 없이 곧바로 사용할 수 있습니다.

- **TF-IDF 기반 키워드 추출기**  
  - TF-IDF(Term Frequency-Inverse Document Frequency) 알고리즘을 사용하여 텍스트에서 핵심 키워드를 추출합니다.
  - 입력된 텍스트를 문장 단위로 분할하여 여러 개의 소문서로 나눕니다. TF-IDF는 특정 단어가 해당 문서에서는 자주 나타나지만 다른 문서에서는 드물게 나타날수록 높은 점수를 받는 방식입니다.
  - 한국어 특성을 고려하여 조사(을/를, 이/가, 은/는, 와/과, 에/에서, 의, 도, 만 등)를 자동으로 제거하고, 2글자 이상의 의미 있는 단어만 추출합니다.
  - 의미적으로 유사한 키워드(예: "친구"와 "친구들")를 제거하여 중복을 방지합니다.
  - 최종적으로 상위 10개의 핵심 키워드를 선별하여 시 생성 프롬프트에 포함시킵니다.

- **Google Cloud Translation API**  
  - 모델이 비한국어 시를 출력하면 자동으로 한국어로 번역합니다. 서비스 계정(ADC) 또는 API 키 방식으로 인증하며, 필요하면 특정 언어만 번역하거나 문체를 조정하는 옵션도 활용할 수 있습니다. 번역이 실패하면 원문을 안전하게 반환하고 경고 로그로 상태를 남깁니다.

- **Google Gemini API**  
  - 감정 데이터를 서술형 스토리로 풀어내거나 시를 자연스럽게 다듬는 후처리에 사용합니다. Prompt 기반 호출만으로 동작하므로 별도 파인튜닝 없이도 높은 품질을 제공하며, 감정 코멘트·사용자 맞춤 메시지 같은 다양한 추가 응답을 만들 수 있습니다.

## ☆ 프로젝트 구조

```
siot-OSS/
├── backend/                    # 백엔드 서버
│   ├── app/                    # FastAPI 애플리케이션
│   │   ├── main.py            # FastAPI 엔트리포인트
│   │   └── services/          # 핵심 비즈니스 로직
│   │       ├── poem_generator.py          # 시 생성 메인 로직
│   │       ├── poem_model_loader.py       # 모델 로딩
│   │       ├── poem_prompt_builder.py      # 프롬프트 구성
│   │       ├── poem_text_processor.py     # 후처리
│   │       ├── emotion_classifier.py      # 감정 분류
│   │       ├── keyword_extractor.py       # 키워드 추출
│   │       ├── translator.py              # 번역
│   │       └── poem_config.py            # 설정
│   ├── colab_server.py        # Colab 실행 스크립트
│   ├── requirements.txt       # Python 의존성
│   ├── start.sh              # 서버 시작 스크립트
│   └── trained_models/        # 학습된 모델 저장소
│
├── frontend/                   # 프론트엔드 (React + Vite)
│   ├── src/
│   │   ├── pages/            # 페이지 컴포넌트
│   │   │   ├── PoemGeneration.jsx    # 시 생성 페이지
│   │   │   ├── EmotionTrend.jsx      # 감정 추이 페이지
│   │   │   ├── Archive.jsx           # 아카이브 페이지
│   │   │   └── Settings.jsx          # 설정 페이지
│   │   ├── components/       # 재사용 가능한 컴포넌트
│   │   └── layouts/          # 레이아웃 컴포넌트
│   ├── package.json          # Node.js 의존성
│   └── vite.config.js       # Vite 설정
│
└── README.md                 # 프로젝트 문서
```

## ☆ 아키텍처

## 시스템 아키텍처
```
┌─────────────────┐
│   프론트엔드     │  React + Vite
│  (React App)    │  └─ 시 생성 UI
└────────┬────────┘  └─ 감정 시각화
         │ HTTP/REST
         ▼
┌─────────────────┐
│   백엔드 API     │  FastAPI
│  (FastAPI)      │  └─ /api/poem/generate
└────────┬────────┘  └─ /api/emotion/analyze-cute
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌──────────┐
│ AI 모델│ │ 외부 API │
│        │ │          │
│ SOLAR  │ │ Gemini   │
│ koGPT2 │ │ Google   │
│        │ │ Translate│
└────────┘ └──────────┘
```

## 데이터 흐름
1. **사용자 입력** → 프론트엔드에서 일상글 입력  
2. **키워드 추출** → TF-IDF로 핵심 키워드 추출  
3. **감정 분석** → XNLI 기반 제로샷 감정 분류  
4. **프롬프트 구성** → 키워드, 감정, 옵션을 조합해 프롬프트 생성  
5. **시 생성** → SOLAR/koGPT2 모델로 생성  
6. **후처리** → 줄바꿈, 산문 필터링, 필요 시 Gemini 개선  
7. **번역** → 비한국어 시는 한국어로 자동 번역  
8. **결과 반환** → 시/메타데이터를 프론트엔드로 전달

## 시 생성 파이프라인 (엔드투엔드)

1. **프론트엔드 입력 (`PoemGeneration.jsx`)**  
   - 모델 타입(SOLAR/koGPT2) 선택, SOLAR는 `VITE_COLAB_API_URL` 검증 필수  
   - AbortController 기반 5분 타임아웃을 걸고 `/api/poem/generate` 호출

2. **FastAPI 진입 (`app/main.py`)**  
   - 요청 스키마 검증 후 서비스 계층 호출  
   - 텍스트 공백/길이, 모델 타입 등 사전 검증 수행

3. **메타데이터 추출**  
   - `keyword_extractor.py`: TF-IDF + 형태소로 핵심 키워드 결정  
   - `emotion_classifier.py`: XNLI 제로샷으로 감정·신뢰도 계산  
   - `poem_prompt_builder.py`: 모델별 템플릿으로 프롬프트 구성

4. **모델 로딩 (`poem_model_loader.py`)**  
   - GPU 여부와 `POEM_MODEL_TYPE`에 따라 SOLAR(4bit NF4) 또는 koGPT2 로딩  
   - 전역 캐시 재사용, SOLAR 실패 시 koGPT2 폴백

5. **생성 (`poem_generator.py`)**  
   - `model.generate()`에 모델별 하이퍼파라미터 적용  
   - `safe_print`로 Colab 환경의 `BrokenPipeError` 예방

6. **후처리 (`poem_text_processor.py`)**  
   - 프롬프트 잔여 텍스트 제거, 줄 수 조정, 산문 패턴 필터  
   - 옵션(줄 수/금칙어 등)에 맞춰 추가 정리

7. **번역 (`translator.py`)**  
   - 언어 감지 후 비한국어면 Google Translation API 호출  
   - 실패/미설정 시 원문 유지하면서 경고 로그

8. **응답 조립 (`app/main.py`)**  
   - 시·키워드·감정·신뢰도·번역 여부를 JSON으로 반환  
   - 옵션에 따라 Gemini 기반 감정 스토리 생성

9. **프론트엔드 후처리**  
   - 결과 카드 렌더링, localStorage(`saved_poems`) 자동 저장  
   - EmotionTrend/Archive 페이지에서 재사용

## ☆ 기술 스택

## 백엔드

| 기술 | 버전 | 용도 |
|------|------|------|
| **Python** | 3.8+ | 백엔드 언어 |
| **FastAPI** | 0.120.3 | 웹 프레임워크 |
| **Uvicorn** | 0.38.0 | ASGI 서버 |
| **PyTorch** | 2.0.0+ | 딥러닝 프레임워크 |
| **Transformers** | 4.40.0+ | Hugging Face 모델 라이브러리 |
| **scikit-learn** | 1.3.0+ | TF-IDF 키워드 추출 |
| **google-cloud-translate** | 3.15.0+ | 번역 API |
| **google-generativeai** | 0.3.0+ | Gemini API |

## 프론트엔드

| 기술 | 버전 | 용도 |
|------|------|------|
| **React** | 19.1.1 | UI 프레임워크 |
| **Vite** | 7.1.7 | 번들러/개발 서버 |
| **React Router** | 7.9.5 | 라우팅 |
| **Recharts** | 3.3.0 | 데이터 시각화 |
| **Tailwind CSS** | 4.1.16 | 스타일링 |

## AI 모델

- **SOLAR-10.7B-Instruct**: GPU 환경에서 고품질 시 생성  
- **koGPT2-base-v2 (파인튜닝)**: CPU 친화적 시 생성 (KPoEM 데이터셋 파인튜닝)  
- **koGPT2-base-v2 (기본)**: 빠른 테스트용  
- **XNLI 기반 분류기**: 감정 분류  
- **Gemini API**: 감정 분석 후처리

## ☆ 기능

- 일상글에서 핵심 키워드 추출 (TF-IDF)
- 감정 분석 및 분위기 매핑 (XNLI 제로샷)
- AI 기반 한국어 시 생성
  - **SOLAR-10.7B-Instruct** (GPU 권장, 고품질)
  - **koGPT2 파인튜닝 모델** (CPU 친화적, KPoEM 데이터셋 학습)
- 비한국어 자동 번역 (Google Cloud Translation API)
- 감정 추이 시각화
  - 최근 7일 감정 추이, 감정 분포, 신뢰도 분포 등
- 모델 학습 및 평가
  - k-fold 교차 검증, Google Colab GPU 활용 학습, 학습 모델 자동 로드
- Gemini API 기반 감정 분석 후처리
  - 감정 데이터를 사용자 친화적인 스토리로 변환

## ☆ 설치 및 설정

## 필수 요구사항
- Python 3.8+
- GPU (권장) 또는 CPU
- Node.js 16+ (프론트엔드)

## 환경 변수 설정 (선택 사항)

### 시 생성 모델 선택

시스템이 자동으로 GPU/CPU를 감지하여 적절한 모델을 선택합니다.

- **GPU 감지 시**: SOLAR 모델 자동 선택 (고품질, 10.7B 파라미터)
- **CPU만 사용 가능 시**: koGPT2 모델 자동 선택 (CPU 친화적, 124M 파라미터)

### 수동으로 모델 지정하기

```bash
# koGPT2 강제 사용 (CPU 친화적, 로컬 개발 권장)
export POEM_MODEL_TYPE=kogpt2

# SOLAR 강제 사용 (GPU 권장, 고품질)
export POEM_MODEL_TYPE=solar
```

`.env` 방식:
```bash
cd backend
touch .env
```

`backend/.env` 예시:
```
# koGPT2 강제 사용 (로컬 개발 시 권장)
POEM_MODEL_TYPE=kogpt2

# 또는 SOLAR 강제 사용
# POEM_MODEL_TYPE=solar
```

> **팁**: 로컬 개발 시 `POEM_MODEL_TYPE=kogpt2`를 설정하면 GPU가 있어도 koGPT2로 빠르게 테스트할 수 있습니다.  
> **참고**: 환경 변수를 설정하지 않으면 자동으로 GPU/CPU를 감지해 적절한 모델을 선택합니다. SOLAR는 GPU가 필요하며, koGPT2는 CPU에서도 실행 가능합니다.

> 📄 API·외부 서비스 전체 가이드는 [`docs/API.md`](docs/API.md)를 참고하세요. Google Cloud Translation, Gemini, ngrok/Colab 연동, cURL 예시는 해당 문서에서 관리됩니다.

## 모델 비교 및 선택 가이드

### 모델 업그레이드 히스토리
1. **polyglot-ko-1.3b** – 초기 1.3B 한국어 모델  
2. **skt/kogpt2-base-v2** – CPU 친화적 대안, 124M 파라미터  
3. **SOLAR-10.7B-Instruct** – GPU용 고품질 모델, 자연스러운 시 표현  
4. **koGPT2 파인튜닝 모델** – KPoEM 데이터셋 기반, k-fold 검증 완료

현재 구조:
- **CPU 환경**: koGPT2 파인튜닝 모델
- **GPU 환경**: SOLAR

| 항목 | SOLAR-10.7B-Instruct | koGPT2-base-v2 (파인튜닝) |
|------|----------------------|---------------------------|
| **권장 환경** | GPU (6-8GB VRAM) | CPU / GPU 모두 가능 |
| **생성 속도** | 빠름 (GPU 기준) | 중간 (CPU 기준) |
| **한국어 이해도** | 우수 | 양호 (파인튜닝 후 개선) |
| **시적 표현력** | 자연스럽고 감성적 | 시다운 표현력 향상 |
| **맥락 이해** | 우수 | 개선됨 |
| **학습 여부** | 사전 학습 | KPoEM 파인튜닝 완료 |
| **상태** | GPU 환경 권장 | CPU 환경 권장 |

### SOLAR 모델 선택의 장점
1. 향상된 시적 품질  
2. 뛰어난 한국어 이해  
3. 일관된 출력  
4. 프롬프트 옵션 활용도 ↑

### 파인튜닝된 koGPT2를 선택해야 하는 경우
- GPU가 없거나 메모리가 부족할 때  
- 빠른 프로토타이핑/테스트가 필요할 때  
- 모델 크기 제약이 있을 때  
- CPU 환경에서도 시다운 품질이 필요할 때

### 권장사항
- GPU가 있으면 SOLAR 사용 권장  
- CPU만 가능하면 파인튜닝 koGPT2 사용  
- 프론트엔드에서 "koGPT2 (CPU)" 버튼을 누르면 학습 모델 자동 사용

> **표현 스타일 차이**  
> **SOLAR**: 한 줄에 여러 이미지를 압축해 넣는 편이며, 은유·상징을 자연스럽게 섞어 묵직한 고전 시 분위기를 만듭니다. 줄 수를 많이 지정하지 않아도 스스로 호흡을 조절하고, 감정 톤을 부드럽게 감싸는 경향이 있습니다.  
> **koGPT2**: 감정과 사건을 비교적 직접적으로 서술해 현대 자유시·일기체에 가깝고, 줄 수·분위기·필수 키워드 옵션에 따라 표현이 즉시 달라집니다. 구어체에 가까운 말투나 솔직한 감정 표현을 원하는 경우 더 자연스럽게 느껴집니다.

### AI 모델 활용 전략
1. **시 생성** – koGPT2 파인튜닝, k-fold 평가, 학습 모델 자동 로드  
2. **감정 분석 후처리** – Gemini API로 감정 스토리 생성

### ☆ koGPT2 파인튜닝 완료
- **데이터셋**: KPoEM  
- **방법**: Full Fine-tuning, 5-fold, Colab GPU  
- **하이퍼파라미터**: EPOCHS=2, LR=5e-5, BATCH=4, GradAccum=4  
- **성과**: 시 형식 유지, 키워드·감정 반영도 향상, 자동 줄바꿈·산문 필터링  
- **파라미터**: Temp=0.65, Top-p=0.85, Top-k=35, Repetition Penalty=1.6, no-repeat-ngram=5  
- **사용법**: 프론트엔드에서 koGPT2 선택 → `trained_models/` 최신 폴더 자동 로드

### 모델 평가 지표
- 시 품질 점수  
- 키워드/감정 관련성  
- 한국어 비율  
- 성공률

## Colab 학습 파이프라인 상세

### 학습 데이터셋

**KPoEM (Korean Poem Dataset)**
- **소스**: Hugging Face `AKS-DHLAB/KPoEM`
- **형식**: TSV 파일 (`KPoEM_poem_dataset_v4.tsv`)
- **내용**: 한국어 시 데이터셋으로, 시 원문 텍스트를 포함
- **사용량**: 학습 시 최대 100개 샘플 사용 (전체 데이터셋 사용 가능, `MAX_DATA_SIZE` 파라미터로 조절)

### 학습 설정 및 하이퍼파라미터

**기본 모델**: `skt/kogpt2-base-v2` (124M 파라미터)

**학습 방법**: k-fold 교차 검증 (5-fold)

k-fold 교차 검증은 데이터를 k개 그룹으로 나누어 각 그룹을 한 번씩 검증 세트로 사용하고 나머지를 학습 세트로 사용하는 방법입니다. 이를 통해 데이터의 모든 부분을 학습과 검증에 활용할 수 있어 모델의 일반화 성능을 더 정확히 평가할 수 있습니다.

**k-fold 교차 검증 작동 원리**:
1. **데이터 분할**: 전체 데이터를 5개 fold로 균등하게 분할 (sklearn의 `KFold` 사용, `shuffle=True`, `random_state=42`로 재현 가능)
2. **Fold별 학습**: 각 fold마다 다음 과정을 반복:
   - **Fold 1**: Fold 1을 검증 세트, Fold 2~5를 학습 세트로 사용
   - **Fold 2**: Fold 2를 검증 세트, Fold 1, 3~5를 학습 세트로 사용
   - **Fold 3**: Fold 3을 검증 세트, Fold 1~2, 4~5를 학습 세트로 사용
   - **Fold 4**: Fold 4를 검증 세트, Fold 1~3, 5를 학습 세트로 사용
   - **Fold 5**: Fold 5를 검증 세트, Fold 1~4를 학습 세트로 사용
3. **독립적 모델 생성**: 각 fold마다 독립적인 모델이 학습되어 `fold_1`, `fold_2`, ..., `fold_5` 디렉터리에 저장
4. **성능 평가**: 각 fold 모델의 validation 성능을 비교하여 최적 모델 선정

**k-fold 교차 검증의 장점**:
- **데이터 활용 극대화**: 모든 데이터가 학습과 검증에 한 번씩 사용되어 데이터 낭비 최소화
- **과적합 방지**: 각 fold마다 다른 데이터로 검증하므로 모델의 일반화 성능을 더 정확히 평가
- **안정적인 성능 평가**: 단일 train/test 분할보다 더 신뢰할 수 있는 성능 지표 제공
- **모델 다양성**: 5개의 서로 다른 모델을 생성하여 최적 모델 선택 가능

**하이퍼파라미터**:
- **에포크 (EPOCHS)**: 2
- **학습률 (LEARNING_RATE)**: 5e-5
- **배치 크기 (BATCH_SIZE)**: 4
- **그래디언트 누적 스텝 (GRADIENT_ACCUMULATION_STEPS)**: 4
- **블록 크기 (BLOCK_SIZE)**: 512 (토큰 단위)
- **Warmup 스텝**: 설정에 따라 자동 계산

**학습 전략**:
1. **시 원문 학습**: 시 텍스트만으로 학습하여 시의 형식, 구조, 표현 방식을 학습
2. **산문 → 시 변환 학습**: 산문을 시로 변환하는 패턴을 학습하여 일상글을 시로 변환하는 능력 향상

### 학습 과정

1. **데이터 준비** – `download_kpoem_data()`로 KPoEM 데이터셋을 Hugging Face에서 다운로드하고 정규화
2. **k-fold 분할** – `prepare_datasets()`로 데이터를 5개 fold로 분할
3. **fold별 학습** – 각 fold마다:
   - 토크나이저 준비 및 데이터셋 전처리
   - `Trainer` API를 사용한 학습 실행
   - Validation 세트로 성능 평가
   - Checkpoint 저장 (Google Drive에 저장)
4. **평가 및 선별** – `evaluate_folds_colab.py`로 각 fold 모델의 성능을 평가하여 최적 fold 선정
5. **배포 준비** – 선택된 fold 모델을 로컬 `backend/trained_models/`에 복사, `find_model_folder.py`로 최신 모델 자동 감지

### 학습 결과

**학습 완료 모델**:
- 각 fold마다 독립적인 모델이 생성되어 `fold_1`, `fold_2`, ..., `fold_5` 디렉터리에 저장
- 모델 파일은 Google Drive (`/content/drive/MyDrive/siot/fold_X`)에 저장되며, 필요시 로컬로 다운로드

**성능 개선**:
- **기본 koGPT2 대비**: 시 생성 품질 향상, 한국어 시 형식에 더 적합한 표현 생성
- **옵션 반영**: 줄 수, 분위기, 필수 키워드 등 사용자 옵션에 더 민감하게 반응
- **CPU 환경**: 파인튜닝된 모델은 CPU 환경에서도 시다운 표현을 유지하며 빠른 추론 가능

**평가 지표**:
- Perplexity (혼란도): 낮을수록 좋음
- 토큰 손실 (Token Loss): 학습 손실 값
- 생성 품질: 키워드 관련성, 한국어 비율, 시 형식 준수도
- `evaluate_folds_colab.py`를 통해 각 fold의 성능을 비교하여 최적 모델 선정

**실제 사용**:
- 학습된 모델은 `backend/trained_models/` 디렉터리에 배치되면 FastAPI가 자동으로 로드
- 프론트엔드에서 "koGPT2 (CPU)" 모델 선택 시 파인튜닝된 모델이 사용됨
- Temperature 0.65, Top-p 0.85, 반복 패널티 1.6 등 시 특화 하이퍼파라미터로 추론 수행

## 모델 심화 비교 (SOLAR vs 파인튜닝 koGPT2)

| 항목 | SOLAR-10.7B-Instruct | koGPT2-base-v2 (KPoEM 파인튜닝) |
|------|----------------------|--------------------------------|
| **모델 유형** | 10.7B Instruct (Upstage) | 124M 한국어 GPT2 |
| **필수 환경** | CUDA GPU | CPU 또는 GPU |
| **로딩 방식** | bitsandbytes 4bit NF4 + device_map=auto | float16/float32, `trained_models/` 캐시 |
| **표현 스타일** | 함축적, 상징적, 고전 시 느낌 | 일상 언어, 직접적 감정 묘사 |
| **장점** | 고품질, 긴 문맥, 옵션 없이도 안정적 | 가벼움, 빠른 추론, 옵션 제어 용이 |
| **단점** | 21GB 로딩, GPU 의존 | 표현 다양성 제한, 긴 문맥 취약 |
| **추천 시나리오** | 감성·고전 시, GPU 보유 | 로컬 개발, 데모, 옵션 세밀 제어 필요 시 |

프론트엔드 `PoemGeneration`은 사용자가 모델을 명시적으로 선택할 수 있고, SOLAR는 ngrok URL 검증을 통과해야 요청을 보냅니다.

## Jupyter 노트북 실험 요약

### GPU_backend.ipynb
- **하는 일**: Colab GPU 런타임에서 FastAPI 서버를 띄우고 ngrok으로 외부에 공개하는 과정을 한 번에 실행합니다.  
- **포함된 단계**: 저장소 클론 → 환경 변수 입력 → CUDA 대응 패키지 설치 → `uvicorn app.main:app` 실행 → pyngrok으로 8000번 포트 노출 → `/health` 테스트.  
- **언제 쓰는가**: 프론트엔드에서 SOLAR 모델을 호출할 수 있도록 Colab 백엔드를 띄울 때, 일일이 셸 명령을 치지 않고 노트북 셀만 순서대로 실행하면 됩니다.

### train_koGPT2.ipynb
- **하는 일**: `train_kogpt2_colab.py`, `find_model_folder.py`, `evaluate_folds_colab.py`를 노트북 셀로 묶어 koGPT2 k-fold 학습→평가→다운로드 과정을 자동화합니다.  
- **포함된 단계**: 의존성 설치 → 학습 스크립트 실행 → 생성된 fold 경로 탐색 → 각 fold 평가 → 원하는 fold를 zip으로 압축해 `files.download`로 내려받기.  
- **언제 쓰는가**: Colab에서 여러 번 실험을 돌린 뒤 결과 모델을 `backend/trained_models/`로 옮기고 싶을 때, 이 노트북을 실행하면 전체 파이프라인을 한 자리에서 관리할 수 있습니다.

> Google Cloud Translation / Gemini / ngrok 설정 요약은 [`docs/API.md`](docs/API.md)를 확인하세요.

## ♥ 실행 방법

## 백엔드 서버 실행

### 1. 가상환경 설정
```bash
cd backend

# 가상환경 확인
ls -la | grep -E "(venv|\.venv)"

# 가상환경이 없으면 생성
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 2. 모델 미리 다운로드 (권장)
```bash
cd backend
source .venv/bin/activate
python download_model.py
```
> 모델은 `~/.cache/huggingface/hub/`에 저장됩니다. SOLAR는 약 21GB, koGPT2는 약 500MB입니다. `POEM_MODEL_TYPE`에 따라 다운로드 대상이 달라집니다.

### 3. 서버 실행
- **start.sh 사용**
  ```bash
  cd backend
  chmod +x start.sh
  ./start.sh
  ```
- **직접 실행**
  ```bash
  cd backend
  source .venv/bin/activate
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```
- **koGPT2 강제 실행**
  ```bash
  cd backend
  export POEM_MODEL_TYPE=kogpt2
  source .venv/bin/activate
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```
- **Python 모듈 실행**
  ```bash
  python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```

### 4. 서버 확인
- 서버: http://localhost:8000  
- Swagger UI: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc  
- 헬스 체크: http://localhost:8000/health

헬스 체크 예시:
```json
{
  "status": "healthy",
  "model_type": "kogpt2",
  "device": "cpu",
  "has_gpu": false,
  "has_trained_model": true
}
```

### 5. 서버 종료
`Ctrl + C`

## 프론트엔드 서버 실행
```bash
cd frontend
npm install   # 최초 1회
npm run dev   # http://localhost:5173
```

`.env` 예시:
```env
VITE_API_URL=http://localhost:8000/api/poem/generate
VITE_COLAB_API_URL=https://your-ngrok-url.ngrok-free.dev
```
> SOLAR 사용 시 ngrok URL을 설정하고 프론트엔드를 재시작하세요.

## Google Colab에서 실행

### 1. 노트북 준비
Colab에서 새 노트북을 열고 `backend/colab_server.py` 내용을 실행합니다.

### 2. 환경 변수
```python
import os
os.environ['NGROK_TOKEN'] = 'your-ngrok-token'
os.environ['GOOGLE_CLOUD_PROJECT_ID'] = 'your-project-id'
os.environ['GEMINI_API_KEY'] = 'your-gemini-api-key'
```

### 3. 서버 실행
```python
!python colab_server.py
```
또는 패키지를 수동 설치한 뒤 `uvicorn` 실행.

### 4. ngrok 터널
```python
from pyngrok import ngrok
ngrok.set_auth_token(os.getenv('NGROK_TOKEN'))
tunnel = ngrok.connect(8000, bind_tls=True)
print(tunnel.public_url)
```

### 5. 프론트엔드 연결
생성된 ngrok URL을 `VITE_COLAB_API_URL`에 설정합니다.  
> Colab 세션이 종료되면 URL이 무효화되며, 무료 플랜은 세션당 2시간 제한이 있습니다.

## 문제 해결

### 포트가 이미 사용 중일 때
```bash
lsof -i :8000          # macOS/Linux
netstat -ano | findstr :8000  # Windows
kill -9 <PID>          # macOS/Linux
taskkill /PID <PID> /F # Windows
```
또는 다른 포트 사용: `uvicorn ... --port 8001`

### 모듈을 찾을 수 없을 때
```bash
pip install -r requirements.txt
pip list | grep -E "(fastapi|uvicorn|transformers|torch)"
```

### 학습된 모델을 찾을 수 없을 때
```bash
ls -la backend/trained_models/
```
모델이 없으면 Colab에서 다운로드한 폴더를 복사하거나 다운로드 스크립트를 실행합니다.

## 서버 실행 옵션
- `--reload`: 코드 변경 시 자동 재시작 (개발 모드)
- `--host 0.0.0.0`: 외부 접근 허용
- `--port 8000`: 기본 포트 (변경 가능)

## 서버 실행 로그 예시
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
[Config] .env 파일 로드됨: /path/to/.env
[Model] 모델 로딩 중...
[Model] koGPT2 모델 로딩 완료
[Model] 학습된 모델 찾기: backend/trained_models/
[Model] 학습된 모델 로드 완료: backend/trained_models/20251109_08...
INFO:     Application startup complete.
```

## ♥ API 문서

시옷 백엔드/프론트엔드가 정상 동작하려면 API 엔드포인트와 외부 서비스(Google Cloud Translation, Gemini 등) 설정을 정확히 맞춰야 합니다. 이 문서는 README에 흩어져 있던 환경 변수와 API 관련 내용을 한 곳에 정리한 것입니다.

## 1. 백엔드 환경 변수 (.env)

`backend/.env` 파일을 생성하고 다음 항목을 필요에 따라 채웁니다.

```bash
# 모델 선택 (미설정 시 GPU 감지로 자동 선택)
POEM_MODEL_TYPE=kogpt2   # 또는 solar

# Google Cloud Translation
GOOGLE_CLOUD_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
# 또는
GOOGLE_TRANSLATION_API_KEY=your-translation-api-key

# Gemini (감정 스토리/시 개선)
GEMINI_API_KEY=your-gemini-api-key

# Colab에서 ngrok 토큰을 사용할 경우
NGROK_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx
```

> 💡 로컬 개발 시 CPU만 사용할 계획이라면 `POEM_MODEL_TYPE=kogpt2`를 미리 지정해 두면 매번 자동 감지를 기다리지 않아도 됩니다.

## 2. 프론트엔드 환경 변수 (`frontend/.env`)

```bash
# 로컬 FastAPI 백엔드
VITE_API_URL=http://localhost:8000/api/poem/generate

# SOLAR (Colab) 백엔드 URL
VITE_COLAB_API_URL=https://<your-ngrok>.ngrok-free.dev
```

프론트엔드 `PoemGeneration` 페이지는 모델 선택에 따라 위 값 중 하나를 사용합니다. SOLAR를 선택하면 **반드시** ngrok URL이 필요하며, 로컬 URL을 넣으면 거부합니다.

## 3. Google Cloud Translation API 설정

1. [Google Cloud Console](https://console.cloud.google.com/) 접속 → 프로젝트 생성/선택  
2. “APIs & Services → Library”에서 **Cloud Translation API v3**를 활성화  
3. 인증 방식 선택
   - **ADC**: 로컬 터미널에서 `gcloud auth application-default login` 실행 후 `GOOGLE_CLOUD_PROJECT_ID` 설정
   - **서비스 계정**: 키 JSON을 만들고 `GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json` 지정
4. (선택) API 키 발급 → `GOOGLE_TRANSLATION_API_KEY`에 넣으면 간단한 테스트가 가능  
5. Colab에서는 키 파일을 `/content/key.json`에 업로드한 뒤 환경 변수로 연결합니다.

번역 설정이 누락되면 한국어가 아닌 시를 생성해도 번역 단계가 건너뛰어지며, 로그에 경고가 표시됩니다.

## 4. Gemini API (감정 스토리, 시 개선)

1. [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급  
2. `GEMINI_API_KEY` 환경 변수에 저장  
3. FastAPI 서버에서 감정 요약(`analyze_emotions_cutely`)이나 Gemini 시 개선(`improve_poem_with_gemini`) 호출 시 자동 사용  

> 무료 티어라도 일일 호출 제한이 있으므로, 다량 테스트 시 quota에 유의하세요.

## 5. API 엔드포인트 요약

| 엔드포인트 | 메서드 | 설명 | 비고 |
|------------|--------|------|------|
| `/health` | GET | 서버/모델 상태 확인 | 모델 ID, GPU 여부, has_trained_model 표시 |
| `/api/poem/generate` | POST | 시 생성 요청 | `PoemRequest` (text, mood, lines, model_type 등) |
| `/api/emotion/analyze-cute` | POST | 감정 데이터 요약 | Gemini 기반 감정 스토리 생성 |

주요 요청 예시는 README “API 문서” 섹션의 cURL 스니펫을 참고하세요.

## 6. Colab + ngrok 연동 체크리스트

1. `GPU_backend.ipynb`를 실행해 `/backend` 디렉토리에서 `uvicorn`을 띄웁니다.  
2. ngrok 토큰 설정 → `ngrok.connect(8000)`으로 public URL 획득  
3. 프론트엔드 `.env`의 `VITE_COLAB_API_URL`을 해당 URL로 업데이트하고 `npm run dev` 재시작  
4. health 체크 (`curl <ngrok-url>/health`) 후 프론트엔드에서 SOLAR 모델을 선택합니다.

## 7. API 테스트 명령어 모음

### Health 체크
```bash
curl -H "ngrok-skip-browser-warning: true" https://<ngrok-url>/health
```

### 시 생성 (로컬 예시)
```bash
curl -X POST http://localhost:8000/api/poem/generate \
  -H "Content-Type: application/json" \
  -d '{
        "text": "오늘 하루는 힘들었지만 친구 덕분에 웃을 수 있었다.",
        "lines": 4,
        "mood": "잔잔한",
        "model_type": "kogpt2"
      }'
```

### 감정 스토리 생성
```bash
curl -X POST http://localhost:8000/api/emotion/analyze-cute \
  -H "Content-Type: application/json" \
  -d '{
        "poems": [
          {"emotion": "기쁨", "createdAt": "2024-01-15T10:30:00Z"},
          {"emotion": "슬픔", "createdAt": "2024-01-16T14:20:00Z"}
        ]
      }'
```

## 8. 문제 해결 팁

- **SOLAR 요청이 실패하는 경우**  
  - ngrok URL이 만료되었는지, 브라우저에서 직접 접속해 “Visit site”를 눌렀는지 확인  
  - Colab 세션이 잠들면 uvicorn을 재실행해야 함

- **koGPT2 로컬 추론이 번역 없이 끝나는 경우**  
  - Google Translation 환경 변수가 정확히 설정되었는지 확인  
  - Colab에서는 키 파일을 `/content/key.json` 경로로 업로드했는지 체크

이 문서는 API/환경 설정과 외부 서비스 연동을 한 번에 볼 수 있도록 유지보수하며, README에는 간단한 링크만 남겨 가독성을 확보합니다.



## 상세 API 스펙 (README에서 이동)


### 시 생성 API

**엔드포인트:** `POST /api/poem/generate`

**설명:** 사용자의 일상글을 받아 키워드 추출, 감정 분석, 시 생성을 수행합니다.

**요청 본문:**

```json
{
  "text": "오늘 하루 정말 힘들었어. 하지만 친구들이 많이 응원해줘서 기분이 좋아졌다.",
  "lines": 4,
  "mood": "잔잔한",
  "required_keywords": ["친구", "응원"],
  "banned_words": ["힘들"],
  "use_rhyme": false,
  "acrostic": null,
  "model_type": "solar",
  "use_trained_model": false,
  "use_gemini_improvement": true
}
```

**요청 파라미터:**

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|---------|------|------|--------|------|
| `text` | string | ✅ | - | 시로 변환할 일상글 |
| `lines` | integer | ❌ | 4 | 생성할 시의 줄 수 |
| `mood` | string | ❌ | 자동 감지 | 시의 분위기 (잔잔한/담담한/쓸쓸한) |
| `required_keywords` | array | ❌ | [] | 시에 반드시 포함할 키워드 |
| `banned_words` | array | ❌ | [] | 시에서 사용하지 않을 단어 |
| `use_rhyme` | boolean | ❌ | false | 운율 사용 여부 |
| `acrostic` | string | ❌ | null | 아크로스틱 (예: "사랑해") |
| `model_type` | string | ❌ | 자동 선택 | 사용할 모델 ("solar" 또는 "kogpt2") |
| `use_trained_model` | boolean | ❌ | false | 학습된 모델 사용 여부 |
| `use_gemini_improvement` | boolean | ❌ | true | Gemini로 시 개선 여부 |

**응답 예시:**

```json
{
  "keywords": ["친구", "응원", "기분", "하루"],
  "emotion": "기쁨",
  "emotion_confidence": 0.85,
  "poem": "친구들의 따뜻한 응원\n하루의 힘듦을 잊게 하네\n기분이 좋아지는 순간\n함께하는 소중함 느껴",
  "success": true,
  "message": "시가 성공적으로 생성되었습니다."
}
```

**응답 필드:**

| 필드 | 타입 | 설명 |
|------|------|------|
| `keywords` | array | 추출된 키워드 목록 |
| `emotion` | string | 감정 분류 결과 (기쁨/슬픔/중립 등) |
| `emotion_confidence` | float | 감정 분류 신뢰도 (0.0 ~ 1.0) |
| `poem` | string | 생성된 시 |
| `success` | boolean | 성공 여부 |
| `message` | string | 응답 메시지 |

**에러 응답:**

```json
{
  "detail": "텍스트가 비어있습니다."
}
```

**cURL 예시:**

```bash
curl -X POST "http://localhost:8000/api/poem/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "오늘 하루 정말 힘들었어",
    "lines": 4,
    "mood": "쓸쓸한"
  }'
```

### 감정 분석 API

**엔드포인트:** `POST /api/emotion/analyze-cute`

**설명:** 생성된 시들의 감정 데이터를 받아 Gemini API로 사용자 친화적인 스토리로 변환합니다.

**요청 본문:**

```json
{
  "poems": [
    {
      "emotion": "기쁨",
      "createdAt": "2024-01-15T10:30:00Z"
    },
    {
      "emotion": "슬픔",
      "createdAt": "2024-01-16T14:20:00Z"
    }
  ]
}
```

**응답 예시:**

```json
{
  "story": "이번 주는 감정 변화가 다양했습니다. 월요일에는 기쁨이 많이 나타났고, 화요일에는 슬픔이 증가했습니다...",
  "summary": "전체적으로 기쁨과 슬픔이 번갈아 나타나는 패턴을 보입니다.",
  "emoji": "😊",
  "message": "오늘도 수고하셨어요!",
  "success": true
}
```

### 헬스 체크 API

**엔드포인트:** `GET /health`

**설명:** 서버 상태 및 모델 정보를 확인합니다.

**응답 예시:**

```json
{
  "ok": true,
  "service": "poem",
  "model_type": "kogpt2",
  "model_id": "skt/kogpt2-base-v2",
  "device": "cpu",
  "has_gpu": false,
  "model": "KOGPT2 (CPU)"
}
```

**인터랙티브 API 문서:**

서버 실행 후 다음 URL에서 Swagger UI를 통해 API를 테스트할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## ☆ 개발 가이드

### 코드 구조

백엔드는 **서비스 지향 아키텍처(SOA)**를 따릅니다:

```
backend/app/
├── main.py                    # FastAPI 엔트리포인트, API 라우팅
└── services/                  # 비즈니스 로직 레이어
    ├── poem_generator.py      # 시 생성 메인 로직
    ├── poem_model_loader.py   # 모델 로딩 및 관리
    ├── poem_prompt_builder.py # 프롬프트 구성
    ├── poem_text_processor.py # 후처리 (줄바꿈, 필터링)
    ├── emotion_classifier.py  # 감정 분류 (XNLI)
    ├── keyword_extractor.py  # 키워드 추출 (TF-IDF)
    ├── translator.py          # 번역 (Google Cloud)
    └── poem_config.py         # 설정 관리
```

### 주요 파일 설명

이 문서는 시옷 프로젝트에서 핵심이 되는 파이썬 모듈과 학습 스크립트를 한 곳에서 정리한 것입니다. 파일별 역할과 주요 함수, 커스터마이징 포인트를 참고해 개발 흐름을 빠르게 파악할 수 있습니다.

#### Backend FastAPI 애플리케이션

**backend/app/main.py**

FastAPI 애플리케이션의 엔트리포인트입니다.

- **역할**: API 엔드포인트 정의, 요청/응답 처리
- **주요 함수**:
  - `generate_poem_from_text()`: 시 생성 API 핸들러
  - `improve_poem_with_gemini()`: Gemini 기반 시 개선
  - `analyze_emotions_cutely()`: 감정 분석 후처리

**backend/app/services/poem_generator.py**

시 생성의 핵심 로직을 담당합니다.

- **역할**: 모델 호출, 생성 파라미터 설정, 후처리 및 번역
- **주요 함수**:
  - `generate_poem_from_keywords()`: 키워드 기반 시 생성
  - 내부에서 SOLAR/koGPT2 분기, 모델 캐시, 후처리와 번역 호출까지 담당

**backend/app/services/poem_model_loader.py**

AI 모델을 로딩하고 관리합니다.

- **역할**: 모델 및 토크나이저 로딩, GPU/CPU 자동 감지
- **주요 함수**:
  - `_load_poem_model()`: 모델 로딩
  - `_is_gpu()`: GPU 사용 가능 여부 확인
- **세부 사항**:
  - SOLAR 선택 시 bitsandbytes 4bit NF4 양자화, device_map=auto 설정
  - GPU 메모리 확인 후 오류 시 koGPT2로 폴백
  - 성공적으로 로드한 토크나이저/모델을 모듈 전역 캐시에 저장해 재사용

**backend/app/services/poem_prompt_builder.py**

시 생성 프롬프트를 구성합니다.

- **역할**: 키워드, 감정, 옵션을 조합하여 프롬프트 생성
- **주요 함수**:
  - `_build_messages()`: SOLAR 모델용 프롬프트
  - `_build_messages_kogpt2()`: koGPT2 모델용 프롬프트
- **커스터마이징 포인트**: `_build_messages` 계열 함수를 수정해 줄 수, 분위기, 금칙어 규칙 등을 조정할 수 있습니다.

**backend/app/services/emotion_classifier.py**

XNLI 기반 제로샷 감정 분류를 수행합니다.

- **역할**: 텍스트의 감정을 분류하고 분위기로 매핑
- **주요 함수**:
  - `classify_emotion()`: 감정 분류

**backend/app/services/keyword_extractor.py**

TF-IDF 기반 키워드 추출을 수행합니다.

- **역할**: 텍스트에서 핵심 키워드 추출
- **주요 함수**:
  - `extract_keywords()`: 키워드 추출

**backend/app/services/poem_text_processor.py**

생성된 시를 후처리합니다. 산문처럼 보이는 패턴을 걸러내고 줄 수를 맞춥니다.

- **역할**: 줄바꿈 정리, 산문 패턴 제거, 길이 조정
- **주요 함수**:
  - `_postprocess_poem()`: 후처리 메인 함수
- **주요 로직**:
  - 문장 길이·마침표 기반으로 줄바꿈 재구성
  - "산문:" 같은 프롬프트 잔여 패턴 제거
  - 최소 줄 수/최대 줄 수 조건을 만족하지 못하면 원본을 반환

**backend/app/services/translator.py**

Google Cloud Translation API를 통해 번역을 수행합니다.

- **역할**: 시 언어 감지, 비한국어 시를 한국어로 번역
- **주요 함수**:
  - `translate_poem_with_retry()`: 재시도 로직을 포함한 번역
  - `detect_language()`: 언어 감지
- **환경 변수**:
  - `GOOGLE_CLOUD_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS`, `GOOGLE_TRANSLATION_API_KEY` 중 하나가 필요
  - API 키 또는 ADC가 없으면 번역을 건너뛰고 원문을 반환

#### 로컬 추론/학습 유틸리티

**backend/use_trained_model.py**

- **역할**: Colab에서 학습한 koGPT2 모델 폴더를 로컬에서 로드해 산문→시 생성
- **주요 함수**:
  - `load_trained_model()`: 모델과 토크나이저 로딩
  - `generate_poem_from_prose()`: 산문→시 생성 파이프라인
- **특징**:
  - `MODEL_PATH`를 변경해 원하는 fold 모델을 지정
  - 키워드 추출 모듈이 있으면 프롬프트에 자동으로 주제 키워드를 삽입
  - CPU/GPU/MPS를 자동 감지하며, `FORCE_CPU`로 강제 변경 가능

#### Colab 실행/학습 파일

**backend/colab_server.py**

- **역할**: Colab 런타임에서 FastAPI 서버를 자동으로 띄우는 런처 스크립트
- **실행 흐름**:
  1. `pip install -r requirements.txt`로 의존성 설치
  2. `NGROK_TOKEN` 설정 후 포트 8000을 랜덤 ngrok 도메인으로 공개
  3. `.env` 템플릿을 불러와 Colab 전용 환경 변수를 주입
  4. `uvicorn app.main:app --host 0.0.0.0 --port 8000` 실행
- **특징**: hostname을 지정하지 않아 ngrok 주소가 매번 달라지며, Colab 출력창에 즉시 공유 가능한 URL과 `/api/poem/generate` 예시를 찍어줍니다.

**GPU_backend.ipynb**

- **역할**: Colab에서 백엔드를 운영할 때 사용하는 노트북 스텝-by-스텝 가이드
- **주요 셀**:
  - 런타임 GPU 설정/점검 (`!nvidia-smi`)
  - 프로젝트 클론 및 `pip install -r backend/requirements.txt`
  - `python backend/colab_server.py` 실행
  - health 체크 및 샘플 API 호출 (`requests.post(...)`)
- **팁**: 발급된 ngrok URL을 프론트 `.env`(`VITE_COLAB_API_URL`)에 넣으면 SOLAR 선택 시 자동으로 Colab 서버를 호출합니다.

**backend/train_kogpt2_colab.py**

- **역할**: koGPT2를 KPoEM 데이터셋으로 k-fold 파인튜닝하는 Colab 전용 스크립트
- **구성**:
  - `download_kpoem_data()`: Hugging Face에서 데이터 다운로드 후 JSON/CSV 캐시
  - `prepare_tokenizer()` / `prepare_datasets()`: 토크나이저 세팅과 fold 분리
  - `train_fold()`: fold별 학습, validation 평가, Checkpoint 저장
  - `save_model_to_drive()`: Google Drive (`/content/drive/MyDrive/siot/fold_X`)에 저장
- **주요 파라미터**: `K_FOLDS`, `EPOCHS`, `BATCH_SIZE`, `LEARNING_RATE`, `BLOCK_SIZE`, `WARMUP_STEPS`
- **실행 순서**:
  1. Colab에서 GPU 런타임 선택 후 드라이브 마운트
  2. 필요한 하이퍼파라미터 수정
  3. 스크립트 실행 → `fold_1`~`fold_K` 디렉터리 생성

**backend/evaluate_folds_colab.py**

- **역할**: 학습된 fold 모델 전체를 불러와 일괄 평가
- **세부 기능**:
  - `BASE_MODEL_DIR` 아래 `fold_*` 디렉터리 스캔
  - 각 fold마다 예제 입력을 넣어 perplexity, 토큰 손실 등을 계산
  - 결과를 표/JSON/로그로 출력하여 베스트 fold를 선정
- **활용**: Colab에서 즉시 최고의 fold를 찾고, 해당 폴더만 다운로드하여 배포 환경에 반영

**backend/find_model_folder.py**

- **역할**: `trained_models/` 내 최신 폴더를 정렬해 반환
- **Colab 연계**: Colab에서 학습한 모델을 로컬에 내려 받은 뒤 FastAPI가 자동으로 최신 모델을 로드하도록 도와줍니다.

**backend/download_model.py**

- **역할**: SOLAR 또는 koGPT2 모델을 로컬 캐시에 미리 다운로드해 최초 추론 지연을 줄임
- **Colab 사용법**: Colab에서도 동일하게 실행해 모델 가중치를 `/root/.cache/huggingface`에 미리 받아둘 수 있습니다.

**backend/download_models_from_colab.py**

- **역할**: Drive에 저장된 fold 폴더를 zip으로 묶어 외부로 내보내는 편의 스크립트
- **흐름**:
  1. `!zip -r fold_1.zip /content/drive/.../fold_1`
  2. 공유 링크 또는 `gdown` 명령으로 로컬 머신에서 다운로드
  3. `backend/trained_models/`에 압축 해제

**backend/check_fold_structure.py**

- **역할**: `trained_models/fold_*` 구조가 요구사항(토크나이저/모델/메타파일 포함)을 만족하는지 검증
- **사용 시점**: Colab 모델을 옮긴 직후, 서버가 인식 가능한 구조인지 빠르게 확인

**backend/holdout_poem_generation.py**

- **역할**: 고정된 hold-out 산문 세트로 학습 모델을 평가하고 CSV/JSON 로그를 남김
- **특징**: Colab 학습 모델을 로컬 환경에서 재검증할 때 사용하며, 결과를 곧바로 README나 보고서에 반영할 수 있습니다.

**backend/kfold_poem_generation.py**

- **역할**: `trained_models/fold_*` 전체를 순회하면서 동일 입력에 대한 생성 결과/지표를 비교
- **출력**: fold별 시 결과, 감정 분포, 평균 로그퍼플렉시티 등

**Colab 전용 워크플로 개요**
1. GPU 런타임에서 `GPU_backend.ipynb` 또는 `colab_server.py`로 환경 세팅.
2. `train_kogpt2_colab.py`로 k-fold 학습 후 Google Drive에 저장.
3. `evaluate_folds_colab.py`로 각 fold 성능을 비교해 베스트 모델 선정.
4. `download_models_from_colab.py`로 선택한 모델을 zip으로 내려받아 로컬 `trained_models/`에 배치.
5. 서버/로컬에서 `find_model_folder.py`로 최신 모델을 자동으로 찾아 로드.

#### 노트북 (Notebooks)

**GPU_backend.ipynb**

- **역할**: FastAPI 백엔드를 Google Colab GPU 환경에서 실행할 때 사용하는 노트북
- **내용**: 패키지 설치, ngrok 연동, `.env` 세팅, API 호출 테스트 셀 포함

**train_koGPT2.ipynb**

- **역할**: koGPT2 모델을 KPoEM 데이터셋으로 파인튜닝하는 과정을 단계별로 안내하는 노트북
- **내용**: 데이터 다운로드, 전처리, 학습, 평가, 모델 저장 셀 포함

#### 프론트엔드

**frontend/src/pages/PoemGeneration.jsx**

- **역할**: 시 생성 메인 페이지 컴포넌트
- **주요 기능**:
  - 텍스트 입력 및 모델 선택
  - API 호출 및 결과 표시
  - localStorage를 통한 자동 저장

**frontend/src/components/***

- **역할**: 재사용 가능한 UI 컴포넌트들
- **주요 컴포넌트**: Header, Footer, PoemCard 등

### 커스터마이징

#### 시 생성 파라미터 조정

`backend/app/services/poem_config.py`에서 기본값을 수정할 수 있습니다:

```python
# 생성 파라미터
DEFAULT_TEMPERATURE = 0.7      # 창의성 (높을수록 다양)
DEFAULT_TOP_P = 0.9            # 샘플링 범위
DEFAULT_MAX_NEW_TOKENS_GPU = 80  # GPU 환경 최대 토큰
DEFAULT_MAX_NEW_TOKENS_CPU = 40  # CPU 환경 최대 토큰
```

#### 프롬프트 템플릿 수정

`backend/app/services/poem_prompt_builder.py`에서 프롬프트 템플릿을 수정할 수 있습니다:

```python
def _build_messages(keywords, mood, lines, ...):
    # 프롬프트 템플릿 커스터마이징
    prompt = f"""
    다음 키워드와 분위기로 {lines}줄의 시를 작성해주세요.
    키워드: {', '.join(keywords)}
    분위기: {mood}
    ...
    """
```

#### 후처리 규칙 수정

`backend/app/services/poem_text_processor.py`에서 후처리 규칙을 수정할 수 있습니다:

```python
def _postprocess_poem(text, min_lines=4, max_lines=20):
    # 줄바꿈 규칙, 필터링 규칙 등 커스터마이징
    ...
```

### 개발 환경 설정

1. **가상환경 생성 및 활성화**

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

2. **의존성 설치**

```bash
pip install -r requirements.txt
```

3. **개발 모드로 서버 실행**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

`--reload` 옵션을 사용하면 코드 변경 시 자동으로 서버가 재시작됩니다.

### 테스트

현재 테스트 코드는 포함되어 있지 않지만, 다음 방법으로 API를 테스트할 수 있습니다:

1. **Swagger UI 사용**: http://localhost:8000/docs
2. **cURL 사용**: 위의 API 문서 예시 참고
3. **프론트엔드에서 테스트**: 실제 사용자 인터페이스에서 테스트

## ☆ 프론트엔드 사용 흐름

### PoemGeneration 페이지
- **입력 영역**: “일상글을 입력해주세요” 텍스트 영역에 하루 기록이나 감정을 작성합니다. 공백만 있으면 제출 버튼이 비활성화됩니다.
- **모델 선택**: 상단 버튼으로 SOLAR(GPU) 또는 koGPT2(CPU)를 명시적으로 선택할 수 있습니다. 선택하지 않으면 환경 변수에 따라 자동 결정되지만, SOLAR를 강제하려면 ngrok/Colab URL 검증을 통과해야 합니다.
- **요청 전 검증**:
  - SOLAR 선택 시 `VITE_COLAB_API_URL`이 비어 있거나 `localhost`/`127.0.0.1`이 포함되어 있으면 오류 메시지를 띄우고 API 요청을 차단합니다.
  - URL이 `https://`로 시작하지 않으면 “절대 URL 필요” 경고 후 요청을 진행하지 않습니다.
- **API 호출/타임아웃**:
  - SOLAR → ngrok/Colab URL 기반 `POST /api/poem/generate`
  - koGPT2 → 로컬 FastAPI(`http://localhost:8000`)
  - AbortController로 5분 타임아웃을 설정해 응답이 없으면 “시 생성 시간이 너무 오래 걸렸다” 메시지를 표시합니다.
- **결과 출력/자동 저장**:
  - 성공 시 키워드·감정·시 본문을 카드로 보여주고, localStorage(`saved_poems`)에 자동 저장합니다(설정에서 끌 수도 있음).
  - “보관함에 저장” 버튼으로 수동 저장도 가능합니다.
- **에러 처리**:
  - ngrok 만료, Colab 세션 종료, CORS 문제 등을 감지하면 콘솔과 UI에 동시에 디버깅 정보를 제공합니다.
  - SOLAR 요청 실패 시 ngrok health 체크 방법과 “브라우저에서 URL 방문 후 경고 우회” 팁을 안내합니다.

### EmotionTrend / Archive / Settings
- **EmotionTrend**: localStorage 데이터를 이용해 최근 7일 감정 추이, 전체 감정 분포, 감정 신뢰도 분포를 Recharts로 시각화합니다. 데이터가 없으면 차트를 숨기고 안내 문구를 표시합니다.
- **Archive**: 저장된 시 목록을 시간순으로 나열하고, 복사·삭제 기능을 제공합니다.
- **Settings**: 기본 모델 타입, 자동 저장 여부 등을 `app_settings`에 저장해 다음 실행 시 유지합니다.

### 운영 시나리오 예시
1. 로컬에서 FastAPI(`uvicorn app.main:app`)와 프론트엔드(`npm run dev`)를 실행합니다.
2. SOLAR 실험이 필요하면 Colab에서 `GPU_backend.ipynb`로 서버를 띄우고 ngrok URL을 발급받아 프론트 `.env`에 입력합니다.
3. 사용자(또는 QA)는 PoemGeneration UI에서 모델을 선택하고 “시 생성하기” 버튼을 클릭합니다.
4. 생성 결과는 즉시 화면에 표시되며 EmotionTrend/Archive 화면에서 다시 확인할 수 있습니다.


## ♥ 데이터 시각화

### 구현된 시각화

#### 1. 최근 7일 감정 추이 (라인 차트)

**차트 타입**: 다중 라인 차트 (Multi-line Chart)  
**데이터 소스**: localStorage에 저장된 시 생성 기록  
**표시 기간**: 최근 7일 (오늘 포함)

**특징:**
- **상위 5개 감정만 표시**: 일주일간 가장 많이 나타난 감정 5개만 선별하여 표시하여 가독성 향상
- **날짜별 집계**: 각 날짜별로 감정별 시 생성 개수를 집계
- **인터랙티브 툴팁**: 마우스 호버 시 해당 날짜의 각 감정별 정확한 개수 표시
- **감정별 색상 구분**: 각 감정마다 고유한 색상 할당
  - 기쁨: 초록색 (#4CAF50)
  - 슬픔: 파란색 (#2196F3)
  - 사랑: 분홍색 (#E91E63)
  - 그리움: 청록색 (#00BCD4)
  - 중립: 회색 (#9E9E9E)
  - 기타 감정들도 각각 고유 색상

**데이터 처리 로직:**
1. localStorage에서 모든 시 데이터 로드
2. `createdAt` 필드를 기준으로 최근 7일 데이터 필터링
3. 날짜별로 그룹화하여 각 감정의 개수 집계
4. 감정별 총 개수를 계산하여 상위 5개 선별
5. 날짜순으로 정렬하여 차트 데이터 구성

**사용 예시:**
```
날짜: 2024-01-15
- 기쁨: 3개
- 사랑: 2개
- 중립: 1개

날짜: 2024-01-16
- 슬픔: 2개
- 그리움: 1개
- 기쁨: 1개
```

이런 식으로 각 날짜별 감정 분포를 라인으로 연결하여 추이를 시각화합니다.

#### 2. 감정 분포 (파이 차트)

**차트 타입**: 파이 차트 (Pie Chart)  
**데이터 범위**: 전체 기간의 모든 시 생성 기록

**특징:**
- **비율 시각화**: 각 감정이 전체 중 차지하는 비율을 원형으로 표현
- **개수 표시**: 각 감정의 절대 개수도 함께 표시
- **색상 일관성**: 라인 차트와 동일한 색상 체계 사용
- **정렬**: 개수가 많은 순서대로 정렬하여 주요 감정을 쉽게 파악

**데이터 처리:**
1. 모든 시 데이터에서 `emotion` 필드 추출
2. 감정별로 개수 집계
3. 개수 순으로 정렬
4. 각 감정의 비율 계산 (개수 / 전체 개수 × 100)

**인사이트:**
- 가장 많이 나타난 감정 파악
- 감정의 다양성 확인
- 특정 감정에 치우쳐 있는지 확인

#### 3. 감정 신뢰도 분포 (바 차트)

**차트 타입**: 수평 바 차트 (Horizontal Bar Chart)  
**데이터**: 각 시 생성 시 감정 분석의 신뢰도 점수

**특징:**
- **구간별 분류**: 신뢰도를 5개 구간으로 분류
  - 0.0 ~ 0.2: 매우 낮음
  - 0.2 ~ 0.4: 낮음
  - 0.4 ~ 0.6: 보통
  - 0.6 ~ 0.8: 높음
  - 0.8 ~ 1.0: 매우 높음
- **분석 품질 평가**: 감정 분석의 전반적인 신뢰도 수준 파악
- **데이터 품질 모니터링**: 낮은 신뢰도가 많으면 입력 텍스트나 분석 모델 개선 필요

**데이터 처리:**
1. 각 시 데이터의 `emotion_confidence` 필드 추출
2. 신뢰도 값을 구간별로 분류
3. 각 구간별 개수 집계
4. 바 차트로 시각화

**활용:**
- 감정 분석의 정확도 평가
- 신뢰도가 낮은 시 생성 기록 확인
- 분석 모델의 성능 모니터링

#### 4. 전체 기간 감정 추이 (라인 차트)

**차트 타입**: 다중 라인 차트 (Multi-line Chart)  
**데이터 범위**: 모든 시 생성 기록  
**시간 단위**: 주 단위 집계

**특징:**
- **장기 추이 분석**: 전체 기간 동안의 감정 변화 패턴 파악
- **주 단위 집계**: 일별 데이터를 주 단위로 그룹화하여 장기 트렌드 확인
- **최대 8개 감정 표시**: 가장 많이 나타난 감정 8개만 표시하여 복잡도 관리
- **X축 라벨 회전**: 주 라벨이 길 경우 45도 회전하여 가독성 향상

**데이터 처리:**
1. 모든 시 데이터를 날짜순으로 정렬
2. 각 시의 생성 날짜를 주 단위로 변환 (예: "2024-W03")
3. 주별로 감정별 개수 집계
4. 감정별 총 개수를 계산하여 상위 8개 선별
5. 주 라벨 생성 (예: "2024-01-15 ~ 2024-01-21")

**인사이트:**
- 계절별 감정 변화 패턴
- 장기적인 감정 트렌드
- 특정 시기의 감정 변화 (예: 시험 기간, 휴가 기간 등)

### 그래프 상호작용 기능

모든 차트는 다음과 같은 인터랙티브 기능을 제공합니다:

1. **호버 효과**
   - 마우스를 차트 위에 올리면 해당 데이터 포인트의 상세 정보 표시
   - 툴팁에 정확한 수치 표시

2. **범례 (Legend)**
   - 각 감정의 색상을 표시하는 범례 제공
   - 범례 클릭으로 해당 감정 라인 숨기기/보이기 토글 (Recharts 기본 기능)

3. **반응형 디자인**
   - 화면 크기에 따라 자동으로 크기 조정
   - 모바일, 태블릿, 데스크톱 모든 환경에서 최적화된 표시

4. **그리드 라인**
   - 차트 배경에 그리드 라인 표시하여 수치 읽기 용이
   - 점선 스타일로 데이터 라인과 구분

### 데이터 저장 및 관리

**저장 위치**: 브라우저 localStorage  
**저장 형식**: JSON 배열

**저장되는 데이터 구조:**
```json
{
  "id": "1705123456789",
  "poem": "생성된 시 내용...",
  "keywords": ["키워드1", "키워드2"],
  "emotion": "기쁨",
  "emotion_confidence": 0.85,
  "originalText": "원본 텍스트...",
  "createdAt": "2024-01-15T10:30:00.000Z",
  "updatedAt": "2024-01-15T10:30:00.000Z"
}
```

**데이터 처리 최적화:**
- `useMemo` 훅을 사용하여 데이터 집계 연산 최적화
- 시 데이터가 변경될 때만 재계산
- 대량의 데이터도 효율적으로 처리

### 기술 스택

- **Recharts**: React 전용 차트 라이브러리
  - `LineChart`, `Line`: 라인 차트 구현
  - `PieChart`, `Pie`: 파이 차트 구현
  - `BarChart`, `Bar`: 바 차트 구현
  - `ResponsiveContainer`: 반응형 컨테이너
  - `Tooltip`, `Legend`, `CartesianGrid`: 차트 보조 요소
- **localStorage**: 클라이언트 측 데이터 저장 및 분석
- **React Hooks**: 
  - `useMemo`: 데이터 집계 연산 최적화
  - `useEffect`: 데이터 로드 및 상태 관리
  - `useState`: 컴포넌트 상태 관리

### 시각화 활용 예시

**시나리오 1: 감정 패턴 파악**
```
사용자가 최근 7일 감정 추이를 확인하여:
- 월요일에는 슬픔이 많았고
- 주말에는 기쁨이 증가하는 패턴 발견
→ 주중 스트레스 관리 필요성 인식
```

**시나리오 2: 감정 다양성 확인**
```
감정 분포 파이 차트를 통해:
- 전체 감정 중 70%가 "중립"으로 나타남
→ 더 다양한 감정을 표현하는 시 생성 시도
```

**시나리오 3: 분석 품질 모니터링**
```
감정 신뢰도 분포를 확인하여:
- 대부분의 분석이 0.6 이상의 신뢰도
→ 감정 분석 모델이 안정적으로 작동 중
```

**시나리오 4: 장기 트렌드 분석**
```
전체 기간 감정 추이를 통해:
- 1월에는 슬픔이 많았지만
- 2월부터는 기쁨이 증가하는 추세
→ 개인적인 감정 회복 과정 확인
```

> **참고**: 수업에서 배운 matplotlib의 데이터 처리 및 시각화 원리는 그대로 적용되었으며, 웹 환경에 맞게 라이브러리만 변경하여 구현했습니다.


### 프로덕션 환경 배포

#### 백엔드 배포

**1. 서버 준비**

```bash
# 서버에 Python 3.8+ 설치 확인
python3 --version

# 가상환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

**2. 환경 변수 설정**

`.env` 파일 생성:

```env
POEM_MODEL_TYPE=solar
GOOGLE_CLOUD_PROJECT_ID=your-project-id
GEMINI_API_KEY=your-api-key
```

**3. 서버 실행 (프로덕션 모드)**

```bash
# --reload 옵션 제거 (프로덕션에서는 사용하지 않음)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

또는 systemd 서비스로 등록:

```ini
# /etc/systemd/system/siot-backend.service
[Unit]
Description=SIOT Backend Service
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/siot-OSS/backend
Environment="PATH=/path/to/siot-OSS/backend/.venv/bin"
ExecStart=/path/to/siot-OSS/backend/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
```

서비스 시작:

```bash
sudo systemctl enable siot-backend
sudo systemctl start siot-backend
```

**4. 리버스 프록시 설정 (Nginx)**

```nginx
# /etc/nginx/sites-available/siot-backend
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### 프론트엔드 배포

**1. 빌드**

```bash
cd frontend
npm install
npm run build
```

**2. 정적 파일 서빙**

빌드된 파일은 `frontend/dist/` 디렉토리에 생성됩니다.

**Nginx 설정:**

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/siot-OSS/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**3. 환경 변수 설정**

프로덕션 환경에서는 빌드 시점에 환경 변수가 포함됩니다:

```bash
# .env.production 파일 생성
VITE_API_URL=https://api.your-domain.com/api/poem/generate
VITE_COLAB_API_URL=https://your-colab-ngrok-url.ngrok-free.dev
```

빌드:

```bash
npm run build
```

### Docker 배포 (선택 사항)

**Dockerfile 예시:**

```dockerfile
# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml 예시:**

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - POEM_MODEL_TYPE=solar
    volumes:
      - ./backend:/app
      - model_cache:/root/.cache/huggingface

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  model_cache:
```

### 보안 고려사항

1. **환경 변수 보호**: `.env` 파일을 `.gitignore`에 추가
2. **API 키 관리**: 환경 변수로 관리, 코드에 하드코딩 금지
3. **CORS 설정**: 프로덕션에서는 특정 도메인만 허용
4. **HTTPS 사용**: SSL/TLS 인증서 설정
5. **Rate Limiting**: API 요청 제한 설정 (선택 사항)

## ♥ 기여 가이드

프로젝트에 기여해주셔서 감사합니다! 다음 가이드를 따라주세요.

### 기여 방법

1. **Fork 및 Clone**

```bash
git clone https://github.com/your-username/siot-OSS.git
cd siot-OSS
```

2. **브랜치 생성**

```bash
git checkout -b feature/your-feature-name
```

3. **변경사항 커밋**

```bash
git add .
git commit -m "feat: 새로운 기능 추가"
```

커밋 메시지 규칙:
- `feat:`: 새로운 기능
- `fix:`: 버그 수정
- `docs:`: 문서 수정
- `style:`: 코드 스타일 변경
- `refactor:`: 리팩토링
- `test:`: 테스트 추가/수정
- `chore:`: 빌드/설정 변경

4. **Push 및 Pull Request**

```bash
git push origin feature/your-feature-name
```

GitHub에서 Pull Request를 생성하세요.

### 코드 스타일

- **Python**: PEP 8 스타일 가이드 준수
- **JavaScript**: ESLint 규칙 준수
- **주석**: 함수와 클래스에 docstring 작성

### 이슈 리포트

버그를 발견하셨다면 다음 정보를 포함하여 이슈를 생성해주세요:

- **환경**: OS, Python 버전, Node.js 버전
- **재현 단계**: 버그를 재현하는 단계
- **예상 동작**: 기대한 동작
- **실제 동작**: 실제로 발생한 동작
- **에러 메시지**: 에러 로그 (있는 경우)

### 기능 제안

새로운 기능을 제안하고 싶으시다면:

1. GitHub Issues에서 "Feature Request" 템플릿 사용
2. 기능의 목적과 사용 사례 설명
3. 구현 방법에 대한 아이디어 제시 (선택 사항)

## ☆ 라이선스

이 프로젝트는 오픈소스로 배포됩니다. Google Cloud Translation API와 Gemini API는 Google의 API 서비스를 사용하며, 각 사용자가 자신의 API 키를 발급받아 사용해야 합니다. API 키는 환경 변수로 관리되며 코드 저장소에 포함되지 않습니다.

## ☆ FAQ (자주 묻는 질문)


### Q: 모델 다운로드가 너무 느려요.

A: SOLAR 모델은 약 21GB로 다운로드에 시간이 걸릴 수 있습니다. 네트워크 상태에 따라 30분~1시간 정도 소요될 수 있습니다. koGPT2는 약 500MB로 상대적으로 빠릅니다.

### Q: Colab에서 서버를 실행했는데 연결이 안 돼요.

A: 다음을 확인해주세요:
1. ngrok 토큰이 올바르게 설정되었는지
2. Colab 셀이 정상적으로 실행되었는지
3. 프론트엔드 `.env` 파일의 `VITE_COLAB_API_URL`이 올바른지
4. ngrok URL이 만료되지 않았는지 (Colab 세션 재시작 시 URL 변경)

### Q: 생성된 시가 이상해요.

A: 다음을 시도해보세요:
1. 입력 텍스트를 더 구체적으로 작성
2. 필수 키워드나 분위기 옵션 사용
3. Gemini 개선 기능 활성화 (`use_gemini_improvement: true`)
4. 다른 모델 타입 시도 (SOLAR ↔ koGPT2)

### Q: 번역이 작동하지 않아요.

A: Google Cloud Translation API 설정을 확인해주세요:
1. `GOOGLE_CLOUD_PROJECT_ID` 환경 변수 설정
2. ADC(Application Default Credentials) 설정 또는 서비스 계정 키 설정
3. Cloud Translation API 활성화 확인

### Q: 메모리 부족 에러가 발생해요.

A: 다음을 시도해보세요:
1. CPU 환경에서는 koGPT2 모델 사용
2. `max_new_tokens` 값을 줄이기
3. GPU 메모리가 부족한 경우 모델 양자화 옵션 확인

## ☆ 추가 자료

### 관련 문서

- [백엔드 서버 가이드](backend/BACKEND_SERVER_GUIDE.md)
- [Colab 사용 가이드](COLAB_GUIDE.md)
- [Google Cloud 설정 가이드](GOOGLE_CLOUD_SETUP_GUIDE.md)

### 외부 링크

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [SOLAR 모델 정보](https://huggingface.co/upstage/SOLAR-10.7B-Instruct)
- [koGPT2 모델 정보](https://huggingface.co/skt/kogpt2-base-v2)

### 참고 자료

- **KPoEM 데이터셋**: 한국 시 데이터셋 (파인튜닝에 사용)
- **XNLI**: Cross-lingual Natural Language Inference (감정 분류에 사용)

## ☆ 감사의 말

이 프로젝트는 다음 오픈소스 프로젝트와 서비스를 활용합니다:

- [FastAPI](https://fastapi.tiangolo.com/) - 웹 프레임워크
- [Hugging Face Transformers](https://huggingface.co/transformers) - AI 모델 라이브러리
- [PyTorch](https://pytorch.org/) - 딥러닝 프레임워크
- [React](https://react.dev/) - UI 프레임워크
- [Recharts](https://recharts.org/) - 차트 라이브러리
- [Google Cloud Translation API](https://cloud.google.com/translate) - 번역 서비스
- [Google Gemini API](https://ai.google.dev/) - AI 서비스

---


---

> 💡 **팁**: 이 README는 지속적으로 업데이트됩니다. 최신 정보는 GitHub 저장소를 확인해주세요.


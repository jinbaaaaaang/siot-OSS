import React from 'react'

function About() {
    return (
        <div className="p-6 sm:p-8 md:p-10 max-w-5xl mx-auto">
            {/* 헤더 섹션 */}
            <div className="text-center mb-12">
                <h1 className="text-4xl sm:text-5xl font-semibold text-gray-800 mb-4">
                    시옷 (SIOT)
                </h1>
                <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                    당신의 일상을 아름다운 시로 변환하는 AI 시 생성 서비스
                </p>
            </div>

            {/* 소개 섹션 */}
            <div className="mb-12">
                <div className="bg-transparent border border-gray-600 rounded-lg p-8">
                    <h2 className="text-2xl font-semibold text-gray-800 mb-6">프로젝트 개요</h2>
                    
                    <div className="space-y-6">
                        <div>
                            <p className="text-gray-800 leading-relaxed text-lg mb-3">
                                <strong>시옷(SIOT)</strong>은 사용자의 일기를 분석하여 감성을 담은 한국어 시로 변환하는 AI 기반 웹 애플리케이션입니다. 
                                일상의 기록, 감정, 생각을 시로 표현하고 싶지만 시 창작에 어려움을 느끼는 사람들을 위해 개발되었으며, 
                                최신 AI 기술을 활용해 누구나 쉽게 자신만의 시를 생성할 수 있도록 돕습니다.
                            </p>
                            <p className="text-gray-700 leading-relaxed">
                                일상의 일기나 텍스트를 입력하면, TF-IDF로 핵심 키워드를 추출하고 XNLI 기반 제로샷 분류로 감정을 분석한 뒤, 
                                SOLAR-10.7B-Instruct 또는 파인튜닝된 koGPT2 모델을 활용하여 감정과 키워드를 반영한 고품질의 한국어 시를 생성합니다.
                            </p>
                        </div>

                        <div className="pt-4 border-t border-gray-300">
                            <h3 className="text-xl font-semibold text-gray-800 mb-4">시옷을 만들게 된 이유</h3>
                            <p className="text-gray-700 leading-relaxed mb-3">
                                일상에서 일기나 메모를 쓰다 보면, 시간이 지나 다시 읽어봤을 때 그때의 감정이 제대로 전달되지 않는 아쉬움이 있습니다. 
                                단순한 텍스트로만 남아있어서 그 의미가 희미해지는 것이죠. 이러한 일상의 기록들을 <strong>시</strong>로 변환하면 어떨까 하는 생각에서 시작했습니다. 
                                시는 감정을 압축하고, 핵심만 남기며, 시간이 지나도 그 느낌을 간직할 수 있기 때문입니다.
                            </p>
                            <p className="text-gray-700 leading-relaxed">
                                하지만 시를 직접 써보려고 하면 막막한 경우가 많습니다. 감정은 있지만 어떻게 표현해야 할지 모르겠고, 
                                운율이나 형식 같은 것도 부담스럽습니다. 그래서 AI를 활용하여 누구나 쉽게 시를 만들어볼 수 있는 도구를 만들고자 했습니다. 
                                복잡한 설정 없이, 오늘 하루 있었던 일을 적으면 시가 나오는 그런 경험을 제공하고 싶었습니다.
                            </p>
                        </div>

                        <div className="pt-4 border-t border-gray-300">
                            <h3 className="text-xl font-semibold text-gray-800 mb-4">핵심 가치</h3>
                            <div className="space-y-4">
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-800 mb-2">가벼운 시작</h4>
                                    <p className="text-gray-700 leading-relaxed">
                                        긴 글을 쓸 필요가 없습니다. 오늘 점심에 무엇을 먹었는지, 날씨가 어땠는지 같은 작은 일상 몇 줄만 적어도 시가 생성됩니다. 
                                        일기처럼 생각나는 대로 적으면 되므로 부담이 적습니다.
                                    </p>
                                </div>
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-800 mb-2">내 목소리 그대로</h4>
                                    <p className="text-gray-700 leading-relaxed">
                                        모델을 선택할 수 있고, 분위기나 줄 수도 조절할 수 있습니다. 같은 내용이라도 SOLAR로 만들면 더 함축적인 느낌이 나고, 
                                        koGPT2로 만들면 더 현대적인 느낌이 납니다. 누구에게 보여줄지, 어떤 톤으로 남길지에 따라 선택하면 됩니다.
                                    </p>
                                </div>
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-800 mb-2">기억 정리와 보관</h4>
                                    <p className="text-gray-700 leading-relaxed">
                                        산문으로 흩어져 있던 감정들을 시로 압축해두면, 나중에 다시 읽어봤을 때 그때의 핵심만 남아있습니다. 
                                        자동으로 번역도 되고, 표현도 다듬어지므로 더 깔끔하게 보관할 수 있습니다.
                                    </p>
                                </div>
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-800 mb-2">감정 들여다보기</h4>
                                    <p className="text-gray-700 leading-relaxed">
                                        생성된 시마다 감정 분석 결과가 함께 제공됩니다. 이를 차트로 모아보면 며칠간의 감정 변화를 한눈에 확인할 수 있습니다. 
                                        가끔 "이번 주에는 슬픈 시를 많이 만들었구나" 같은 패턴을 발견하기도 합니다.
                                    </p>
                                </div>
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-800 mb-2">창작 연습 파트너</h4>
                                    <p className="text-gray-700 leading-relaxed">
                                        시를 쓰고 싶은데 아이디어가 막힐 때도 활용할 수 있습니다. 키워드나 분위기만 지정하여 초안을 받아보고, 
                                        거기서 시작해서 고쳐나가면 됩니다. 다양한 설정을 바꿔보면서 "이렇게 하면 어떤 느낌이 나지?" 같은 실험도 가능합니다.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* 주요 기능 섹션 */}
            <div className="mb-12">
                <h2 className="text-2xl sm:text-3xl font-semibold text-gray-800 mb-6 text-center">
                    주요 기능
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* 기능 1 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">키워드 추출</h3>
                        <p className="text-gray-800 leading-relaxed">
                            TF-IDF 알고리즘을 사용하여 일상글에서 핵심 키워드를 자동으로 추출합니다. 
                            추출된 키워드는 시 생성의 핵심 재료가 됩니다.
                        </p>
                    </div>

                    {/* 기능 2 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">지능형 감정 분석</h3>
                        <p className="text-gray-800 leading-relaxed mb-2">
                            XNLI 기반 제로샷 학습으로 별도 학습 없이 감정 분류를 수행합니다.
                        </p>
                        <p className="text-gray-700 text-sm mb-2">
                            <strong>13가지 감정 인식</strong>: 기쁨, 슬픔, 분노, 놀람, 두려움, 혐오, 사랑, 그리움, 평온, 불안, 희망, 실망, 중립
                        </p>
                        <p className="text-gray-800 leading-relaxed text-sm">
                            각 감정에 대한 신뢰도 점수를 제공하며, 감정을 시의 분위기(잔잔한/담담한/쓸쓸한 등)로 자동 변환합니다.
                        </p>
                    </div>

                    {/* 기능 3 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">다중 AI 모델 지원</h3>
                        <p className="text-gray-800 leading-relaxed mb-2">
                            세 가지 AI 모델을 지원합니다:
                        </p>
                        <ul className="text-gray-700 text-sm space-y-1 mb-2">
                            <li>• <strong>SOLAR-10.7B-Instruct</strong>: GPU 환경에서 고품질 시 생성 (약 10.7B 파라미터)</li>
                            <li>• <strong>파인튜닝된 koGPT2</strong>: CPU 환경에서도 고품질 시 생성 가능 (KPoEM 데이터셋으로 학습)</li>
                            <li>• <strong>기본 koGPT2</strong>: 빠른 프로토타이핑 및 테스트용</li>
                        </ul>
                        <p className="text-gray-800 leading-relaxed text-sm">
                            시스템이 자동으로 GPU/CPU 환경을 감지하여 최적의 모델을 선택합니다.
                        </p>
                    </div>

                    {/* 기능 4 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">자동 번역 기능</h3>
                        <p className="text-gray-800 leading-relaxed">
                            AI 모델이 비한국어로 시를 생성한 경우, Google Cloud Translation API를 통해 자동으로 한국어로 번역합니다. 
                            이를 통해 항상 한국어 시를 제공할 수 있습니다.
                        </p>
                    </div>
                    
                    {/* 기능 5 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">감정 추이 시각화</h3>
                        <p className="text-gray-800 leading-relaxed mb-2">
                            생성된 시들의 감정 데이터를 수집하여 다음과 같은 시각화를 제공합니다:
                        </p>
                        <ul className="text-gray-700 text-sm space-y-1">
                            <li>• <strong>최근 7일 감정 추이</strong> – 일주일간 감정 변화를 라인 차트로 표시</li>
                            <li>• <strong>감정 분포</strong> – 전체 기간 동안의 감정 비율을 파이 차트로 표시</li>
                            <li>• <strong>감정 신뢰도 분포</strong> – 감정 분석의 신뢰도를 바 차트로 표시</li>
                            <li>• <strong>전체 기간 감정 추이</strong> – 모든 시 생성 기록의 감정 변화 추이</li>
                        </ul>
                    </div>
                    
                    {/* 기능 6 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">Gemini API 활용</h3>
                        <p className="text-gray-800 leading-relaxed">
                            Gemini API를 활용하여 감정 데이터를 서술형 스토리로 풀어내거나 시를 자연스럽게 다듬는 후처리에 사용합니다. 
                            Prompt 기반 호출만으로 동작하므로 별도 파인튜닝 없이도 높은 품질을 제공하며, 
                            감정 코멘트·사용자 맞춤 메시지 같은 다양한 추가 응답을 만들 수 있습니다.
                        </p>
                    </div>

                    {/* 기능 7 */}
                    <div className="bg-transparent border border-gray-600 rounded-lg p-6 hover:shadow-lg transition-shadow">
                        <h3 className="text-xl font-semibold text-gray-800 mb-3">시 보관함</h3>
                        <p className="text-gray-800 leading-relaxed">
                            생성된 시들을 보관함에 저장하고 관리할 수 있습니다. 
                            언제든지 시를 수정하거나 삭제할 수 있으며, 
                            데이터를 내보내거나 가져올 수 있습니다.
                        </p>
                    </div>
                </div>
            </div>

            {/* 사용 방법 섹션 */}
            <div className="mb-12">
                <h2 className="text-2xl sm:text-3xl font-semibold text-gray-800 mb-6 text-center">
                    사용 방법
                </h2>
                <div className="space-y-4">
                    <div className="flex items-start gap-4 bg-transparent border border-gray-600 rounded-lg p-6">
                        <div className="flex-shrink-0 w-10 h-10 bg-[#79A9E6] text-white rounded-full flex items-center justify-center font-bold">
                            1
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">일상글 입력</h3>
                            <p className="text-gray-800">
                                "시 생성" 페이지에서 오늘 하루 있었던 일이나 느낀 점을 자유롭게 작성해주세요. 
                                짧은 문장부터 긴 이야기까지 어떤 형식이어도 괜찮습니다.
                            </p>
                        </div>
                    </div>

                    <div className="flex items-start gap-4 bg-transparent border border-gray-600 rounded-lg p-6">
                        <div className="flex-shrink-0 w-10 h-10 bg-[#79A9E6] text-white rounded-full flex items-center justify-center font-bold">
                            2
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">시 생성하기</h3>
                            <p className="text-gray-800">
                                "시 생성하기" 버튼을 클릭하면 AI가 자동으로 키워드를 추출하고 감정을 분석한 후, 
                                몇 초 안에 아름다운 시를 생성해드립니다.
                            </p>
                        </div>
                    </div>

                    <div className="flex items-start gap-4 bg-transparent border border-gray-600 rounded-lg p-6">
                        <div className="flex-shrink-0 w-10 h-10 bg-[#79A9E6] text-white rounded-full flex items-center justify-center font-bold">
                            3
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">시 저장 및 관리</h3>
                            <p className="text-gray-800">
                                생성된 시가 마음에 드시면 "보관함에 저장" 버튼을 눌러 저장하세요. 
                                "시 보관함"에서 저장된 모든 시를 확인하고, 원하면 수정하거나 삭제할 수 있습니다.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            {/* 기술 스택 섹션 */}
            <div className="mb-12">
                <h2 className="text-2xl sm:text-3xl font-semibold text-gray-800 mb-6 text-center">
                    기술 스택
                </h2>
                <div className="bg-transparent border border-gray-600 rounded-lg p-8">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">프론트엔드</h3>
                            <ul className="space-y-2 text-gray-800 text-sm">
                                <li>• <strong>React 19.1.1</strong> + <strong>Vite 7.1.7</strong></li>
                                <li>• <strong>Tailwind CSS 4.1.16</strong> (스타일링)</li>
                                <li>• <strong>React Router DOM 7.9.5</strong> (라우팅)</li>
                                <li>• <strong>Recharts 3.3.0</strong> (데이터 시각화)</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">백엔드</h3>
                            <ul className="space-y-2 text-gray-800 text-sm">
                                <li>• <strong>FastAPI 0.120.3</strong> (웹 프레임워크)</li>
                                <li>• <strong>Uvicorn</strong> (ASGI 서버)</li>
                                <li>• <strong>Python 3.8+</strong></li>
                                <li>• <strong>PyTorch 2.0+</strong> (딥러닝 프레임워크)</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">AI 모델</h3>
                            <ul className="space-y-2 text-gray-800 text-sm">
                                <li>• <strong>SOLAR-10.7B-Instruct</strong> (시 생성, GPU 권장)</li>
                                <li>• <strong>koGPT2-base-v2</strong> (시 생성, CPU 친화적)</li>
                                <li>• <strong>XNLI (xlm-roberta-large-xnli)</strong> (감정 분석)</li>
                                <li>• <strong>TF-IDF (scikit-learn)</strong> (키워드 추출)</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">기타 서비스</h3>
                            <ul className="space-y-2 text-gray-800 text-sm">
                                <li>• <strong>Google Cloud Translation API v3</strong> (중국어 번역, 선택)</li>
                                <li>• <strong>Gemini API</strong> (감정 분석 후처리, 시 개선, 선택)</li>
                                <li>• <strong>Hugging Face Transformers</strong> (모델 로딩)</li>
                                <li>• <strong>Google Colab</strong> (GPU 환경 제공, 선택)</li>
                                <li>• <strong>ngrok</strong> (Colab 서버 터널링)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            {/* 모델 선택 전략 섹션 */}
            <div className="mb-12">
                <h2 className="text-2xl sm:text-3xl font-semibold text-gray-800 mb-6 text-center">
                    모델 선택 전략
                </h2>
                <div className="bg-transparent border border-gray-600 rounded-lg p-8">
                    <div className="space-y-6">
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">자동 모델 선택</h3>
                            <p className="text-gray-800 leading-relaxed mb-3">
                                시옷은 시스템 환경을 자동으로 감지하여 최적의 모델을 선택합니다:
                            </p>
                            <ul className="list-disc list-inside space-y-2 text-gray-700 ml-4">
                                <li><strong>GPU 감지 시</strong>: SOLAR-10.7B-Instruct 모델 자동 선택 (고품질, 약 10.7B 파라미터)</li>
                                <li><strong>CPU만 사용 가능 시</strong>: koGPT2 모델 자동 선택 (빠른 생성, 약 124M 파라미터)</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">모델 비교</h3>
                            <div className="overflow-x-auto">
                                <table className="w-full text-sm text-gray-800 border-collapse">
                                    <thead>
                                        <tr className="border-b border-gray-300">
                                            <th className="text-left p-2">항목</th>
                                            <th className="text-left p-2">SOLAR-10.7B</th>
                                            <th className="text-left p-2">파인튜닝 koGPT2</th>
                                            <th className="text-left p-2">기본 koGPT2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr className="border-b border-gray-200">
                                            <td className="p-2 font-medium">파라미터 수</td>
                                            <td className="p-2">약 10.7B</td>
                                            <td className="p-2">약 124M</td>
                                            <td className="p-2">약 124M</td>
                                        </tr>
                                        <tr className="border-b border-gray-200">
                                            <td className="p-2 font-medium">모델 크기</td>
                                            <td className="p-2">약 21GB</td>
                                            <td className="p-2">약 500MB</td>
                                            <td className="p-2">약 500MB</td>
                                        </tr>
                                        <tr className="border-b border-gray-200">
                                            <td className="p-2 font-medium">권장 환경</td>
                                            <td className="p-2">GPU (6-8GB VRAM)</td>
                                            <td className="p-2">CPU / GPU 모두 가능</td>
                                            <td className="p-2">CPU / GPU 모두 가능</td>
                                        </tr>
                                        <tr className="border-b border-gray-200">
                                            <td className="p-2 font-medium">생성 품질</td>
                                            <td className="p-2">매우 높음</td>
                                            <td className="p-2">높음 (파인튜닝)</td>
                                            <td className="p-2">보통</td>
                                        </tr>
                                        <tr>
                                            <td className="p-2 font-medium">생성 속도</td>
                                            <td className="p-2">빠름 (GPU 기준)</td>
                                            <td className="p-2">중간 (CPU 기준)</td>
                                            <td className="p-2">중간 (CPU 기준)</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">하이브리드 AI 접근</h3>
                            <p className="text-gray-800 leading-relaxed mb-3">
                                시옷은 다양한 AI 모델과 API를 목적에 맞게 활용하는 하이브리드 접근 방식을 채택했습니다:
                            </p>
                            <ul className="list-disc list-inside space-y-2 text-gray-700 ml-4 text-sm">
                                <li><strong>시 생성</strong>: SOLAR, koGPT2</li>
                                <li><strong>감정 분류</strong>: 제로샷 감정 분석 (XNLI)</li>
                                <li><strong>키워드 추출</strong>: TF-IDF</li>
                                <li><strong>후처리</strong>: Gemini API</li>
                                <li><strong>번역</strong>: Google Cloud Translation</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800 mb-3">표현 스타일 차이</h3>
                            <div className="space-y-3 text-sm">
                                <div>
                                    <p className="text-gray-800 font-semibold mb-1">SOLAR</p>
                                    <p className="text-gray-700 leading-relaxed">
                                        한 줄에 여러 이미지를 압축해 넣는 편이며, 은유·상징을 자연스럽게 섞어 묵직한 고전 시 분위기를 만듭니다. 
                                        줄 수를 많이 지정하지 않아도 스스로 호흡을 조절하고, 감정 톤을 부드럽게 감싸는 경향이 있습니다.
                                    </p>
                                </div>
                                <div>
                                    <p className="text-gray-800 font-semibold mb-1">koGPT2</p>
                                    <p className="text-gray-700 leading-relaxed">
                                        감정과 사건을 비교적 직접적으로 서술해 현대 자유시·일기체에 가깝고, 줄 수·분위기·필수 키워드 옵션에 따라 표현이 즉시 달라집니다. 
                                        구어체에 가까운 말투나 솔직한 감정 표현을 원하는 경우 더 자연스럽게 느껴집니다.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* 정보 섹션 */}
            <div className="bg-transparent border border-gray-600 rounded-lg p-8 text-center">
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">프로젝트 정보</h2>
                <p className="text-gray-800 mb-4">
                    시옷(SIOT)은 오픈소스 프로젝트입니다. 
                    GitHub에서 소스코드를 확인하고 기여할 수 있습니다.
                </p>
                <div className="flex flex-wrap justify-center gap-4 text-sm text-gray-600">
                    <span>오픈소스</span>
                    <span>•</span>
                    <span>지속적인 업데이트</span>
                    <span>•</span>
                    <span>커뮤니티 기여 환영</span>
                </div>
            </div>
        </div>
    )
}

export default About


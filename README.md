# LLM API Compare

## 프로젝트 소개
LLM API Compare는 다양한 대형 언어 모델(LLM)의 API 응답을 비교하고 평가하기 위한 도구입니다. 이 프로젝트는 Netflix 클론 코딩 프로젝트를 기반으로 한 서비스 기획서에 대해 각 LLM이 생성한 아키텍처 설계를 비교 분석합니다.

## 주요 기능
- 여러 LLM 모델의 응답을 한 번에 비교
- 사용자 정의 프롬프트를 통한 모델 응답 생성
- 모델 응답의 순열을 자동으로 생성하여 공정한 비교 지원
- Mermaid 다이어그램을 활용한 시각적 비교

## 지원하는 모델
- Grok 3
- DeepSeek V3
- Claude 3.7 Sonnet
- Gemini 2.5 Pro
- GPT-4.5 Pro Mode

## 설치 및 사용 방법

### 사전 요구 사항
- Python 3.8 이상
- 필요한 패키지: `requirements.txt` (현재는 별도의 패키지가 필요 없음)

### 실행 방법
1. 저장소 클론
```bash
git clone https://github.com/yourusername/llm-api-compare.git
cd llm-api-compare
```

2. 프롬프트 생성
```bash
python mix.py
```

3. 생성된 프롬프트 확인
- `prompts/` 디렉토리에 생성된 프롬프트 확인
- `answer_mapping.json` 파일에서 정답 매핑 정보 확인

## 디렉토리 구조
```
.
├── README.md               # 프로젝트 설명서
├── mix.py                  # 프롬프트 생성 스크립트
├── prompts/                # 생성된 프롬프트 저장 디렉토리
├── *.md                    # 각 모델의 응답 파일
└── answer_mapping.json     # 정답 매핑 정보
```

## 기여 방법
1. 이슈를 생성하여 버그 리포트 또는 기능 제안
2. Fork 후 Pull Request를 통한 기여

## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 문의
문의사항이 있으시면 이슈를 생성해 주세요.
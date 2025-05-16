import json
import os
from itertools import permutations

base_cases = [
    "grok3.md",
    "deepseek-v3.md",
    "claude-3-7-sonnet.md",
    "gemini-2-5-pro.md",
    "gpt-o1-pro-mode.md",
]


# 파일 내용을 읽어오는 함수
def read_file_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[파일을 찾을 수 없음: {file_path}]"
    except Exception as e:
        return f"[파일 읽기 오류: {str(e)}]"


# 모든 가능한 순열 생성
all_permutations = list(permutations(base_cases))

# prompts 디렉토리 생성
os.makedirs("prompts", exist_ok=True)

# 정답 맵핑 정보 저장을 위한 딕셔너리
answer_mapping = {}

PROMPT_TEMPLATE = """### 기획 내용

```
# Netflix 클론 코딩용 간소화된 서비스 기획서

## 1. 서비스 개요
- **서비스명**: MiniFlix
- **서비스 유형**: 웹 기반 스트리밍 서비스 (모바일 앱은 선택적 확장 가능)
- **목적**: 학습 목적으로 넷플릭스의 핵심 기능을 간소화하여 영화/영상 스트리밍 서비스를 구현.
- **타겟 사용자**: 간단한 스트리밍 서비스를 이용하려는 일반 사용자 (학습용 프로젝트이므로 제한 없음).

## 2. 핵심 기능 (최소 요구사항)
### 2.1 콘텐츠 스트리밍
- 사용자가 제공된 영상 콘텐츠(영화, 드라마 클립 등)를 웹에서 스트리밍으로 시청 가능.
- 샘플 영상 파일(무료/오픈소스 영상)을 서버에 업로드하여 제공.
- 기본적인 비디오 플레이어 기능(재생, 일시정지, 볼륨 조절, 전체 화면).

### 2.2 콘텐츠 탐색
- 홈 화면에 모든 콘텐츠 목록 표시(그리드 형태의 썸네일).
- 간단한 검색 기능: 제목으로 콘텐츠 검색.
- 장르별 필터링(예: 액션, 드라마, 코미디 등).

### 2.3 사용자 계정
- 기본적인 회원가입/로그인 기능(이메일, 비밀번호 기반).
- 로그인한 사용자는 콘텐츠 시청 및 찜 목록 관리 가능.
- 비로그인 사용자는 콘텐츠 목록만 볼 수 있음(시청 불가).

### 2.4 찜 목록
- 사용자가 관심 있는 콘텐츠를 "찜" 버튼으로 저장.
- 마이페이지에서 찜한 콘텐츠 목록 확인 가능.

### 2.5 반응형 디자인
- PC와 모바일 브라우저에서 모두 사용 가능한 반응형 웹 UI.
- 넷플릭스 스타일의 심플하고 직관적인 인터페이스(검정 바탕, 썸네일 중심).

## 3. 제외된 기능 (복잡도 감소 목적)
- 개인화 추천 시스템: 구현 난이도와 데이터 요구량이 높아 제외.
- 멀티 프로필: 단일 사용자 계정만 지원.
- 오프라인 다운로드: 서버 부하 및 구현 복잡도로 제외.
- 다중 디바이스 동시 스트리밍: 단일 디바이스 시청만 지원.
- 고화질(HD/4K) 및 다국어 자막: 기본 화질과 자막 없이 진행.
- 구독제 결제 시스템: 학습용이므로 무료 서비스로 가정.

## 4. 사용자 경험 (UX)
- **인터페이스**: 깔끔한 UI로 콘텐츠 탐색 및 시청에 집중.
  - 홈: 콘텐츠 썸네일 그리드, 상단 검색바.
  - 재생 페이지: 비디오 플레이어와 간단한 콘텐츠 정보(제목, 설명).
  - 마이페이지: 찜 목록과 기본 계정 정보.
- **편의성**: 빠른 페이지 로딩, 직관적인 내비게이션.
- **접근성**: 기본적인 반응형 디자인으로 모바일/PC 지원.

## 5. 비즈니스 모델 (가정)
- 학습용 프로젝트로, 실제 결제/구독 없이 무료 서비스로 운영.
- 서버에 업로드된 샘플 콘텐츠(오픈소스 영상)로만 동작.

## 6. 사용자 여정
1. **가입/로그인**: 웹사이트에서 회원가입 또는 로그인.
2. **탐색**: 홈 화면에서 콘텐츠 목록 확인, 검색/필터링으로 원하는 콘텐츠 찾기.
3. **시청**: 콘텐츠 클릭 후 비디오 플레이어로 스트리밍 시청.
4. **관리**: 찜 버튼으로 콘텐츠 저장, 마이페이지에서 찜 목록 확인.

## 7. 구현 가능성
- **콘텐츠**: 무료/오픈소스 영상 파일(예: Pixabay, Pexels 비디오) 사용.
- **프론트엔드**: HTML, CSS, JavaScript(React/Vue 등 선택 가능)로 반응형 웹 구현.
- **백엔드**: Node.js, Django, Flask 등으로 간단한 서버 구축(영상 파일 호스팅, 사용자 데이터 관리).
- **데이터베이스**: MySQL, MongoDB 등으로 사용자 정보 및 찜 목록 저장.
- **영상 스트리밍**: 기본 HTTP 스트리밍(고급 스트리밍 프로토콜은 제외).

## 8. 기대 효과
- **학습 성과**: 웹 서비스 개발의 전반적인 흐름(프론트엔드, 백엔드, DB, 미디어 호스팅) 이해.
- **사용자**: 간단한 스트리밍 서비스를 통해 넷플릭스 핵심 UX 체험.
- **확장 가능성**: 프로젝트 완성 후 추천 시스템, 구독 기능 등을 추가로 학습 가능.
```

### 문서 목록

{numbered_documents}

### 요청사항

다음 [문서 목록]들 중 [기획 내용]에 가장 맞도록 설계를 한 모델을 선정해주세요.
"""

# 각 순열에 대해 프롬프트 생성
prompts = []
for i, perm in enumerate(all_permutations, 1):
    # 각 문서에 번호 부여하고 파일 내용 읽어오기
    numbered_docs = []
    original_to_number = {}  # 원본 파일명과 번호 매핑

    for idx, doc_name in enumerate(perm, 1):
        doc_content = read_file_content(doc_name)
        numbered_docs.append(f"#### {idx}번 모델\n\n{doc_content}\n")
        original_to_number[doc_name] = idx

    # 프롬프트 생성
    prompt = PROMPT_TEMPLATE.format(numbered_documents="\n".join(numbered_docs))

    # 각 순열에 대한 프롬프트를 파일로 저장
    filename = f"prompts/{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prompt)
    prompts.append(filename)

    # 정답 맵핑 정보 저장
    answer_mapping[i] = {
        "permutation": list(perm),
        "number_to_original": {idx: doc for doc, idx in original_to_number.items()},
        "original_to_number": original_to_number,
    }

# 정답 맵핑 정보를 JSON 파일로 저장
with open("prompts/answer_mapping.json", "w", encoding="utf-8") as f:
    json.dump(answer_mapping, f, indent=2, ensure_ascii=False)

print(f"총 {len(prompts)}개의 순열 프롬프트가 생성되었습니다.")
print("생성된 파일들은 prompts/ 디렉토리에 저장되었습니다.")
print("정답 맵핑 정보는 prompts/answer_mapping.json 파일에 저장되었습니다.")

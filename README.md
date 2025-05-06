# 📰 Gemini 기반 뉴스 QA 챗봇

> 한국어 뉴스 문서를 기반으로 **요약 및 질의응답**을 지원하는 AI 챗봇 시스템입니다.  
> LangChain, FAISS, Gemini 1.5 Pro 모델과 Gradio UI를 활용하여 사용자가 질문을 하면 실제 뉴스 기반으로 답변을 제공합니다.

---

## 🎯 프로젝트 목적

- ✅ **사용자 중심 뉴스 요약 및 Q&A 지원**
- ✅ **한국어 뉴스에 특화된 자연어 처리 시스템 구현**
- ✅ **RAG(Retrieval-Augmented Generation) 구조 적용으로 신뢰성 있는 응답 제공**

---

## 🚀 핵심 기능 요약

- 🔍 **실시간 뉴스 문서 로딩 및 요약**
- 🧠 **FAISS 벡터 검색 기반 문맥 추출**
- 🤖 **Gemini 1.5 Pro 모델을 활용한 자연어 응답 생성**
- 💬 **Gradio 인터페이스로 직관적 챗봇 경험 제공**

---

## 🛠️ 사용 기술 스택

| 구분         | 사용 기술 |
|--------------|-----------|
| 언어 & 백엔드 | Python, FastAPI |
| LLM 기반 응답 | Gemini 1.5 Pro via LangChain |
| 벡터 검색     | FAISS + GoogleEmbeddings |
| 문서 처리     | LangChain WebBaseLoader, BeautifulSoup |
| 프론트엔드    | Gradio (Chat UI) |
| 기타 도구     | .env 설정, LangChain Prompt Templates |

---

## 💡 예시 질문

- "🧾 이 뉴스의 핵심은 무엇인가요?"
- "👶 출산 관련 정책이 뭐였어요?"
- "🏛️ 지자체에서 어떤 지원을 하나요?"

---

## 🗂️ 프로젝트 폴더 구조

LLM_RAG/
├── .env # 환경 변수 설정 파일 (API Key 등)
├── .gitignore # Git에서 추적 제외할 파일 목록
├── news_reg.py # 뉴스 문서 분석 및 응답 처리 메인 스크립트
├── RAG_Chatbot2.jpg # 프로젝트 대표 이미지 또는 챗봇 구조도
├── requirements.txt # 필수 Python 패키지 목록
└── README.md # 현재 문서

---

## 📺 프로젝트 시연 영상

[![Gemini 뉴스 QA 챗봇 시연](RAG_Chatbot2.jpg)](https://youtu.be/Hblze1aClLU)

---

## 📌 향후 발전 방향 (제안)

- 🔄 **멀티뉴스 요약 비교 기능** 추가 (예: 언론사 간 관점 차이 요약)
- 🌐 **다국어 지원**: 영어, 일본어 등 다양한 언어 뉴스 적용
- 🧾 **요약 vs 원문 비교모드** 추가 (사용자 선택형)

---

## 👩‍💻 개발자 정보

- **이름**: 석송이  
- **포지션**: AI 기반 웹 애플리케이션 개발자  
- **기술 관심사**: RAG, LangChain, 멀티모달 LLM, 사용자 중심 서비스 설계

> ✨ 본 프로젝트는 실제 뉴스 기반의 응답

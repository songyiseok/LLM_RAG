import os
from dotenv import load_dotenv
import bs4
import gradio as gr
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain import hub


# .env 파일 로드
load_dotenv()

# ✅ API 키 설정
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


# ✅ 뉴스 기사 로드 및 문서 처리
loader = WebBaseLoader(
    web_paths=["https://n.news.naver.com/article/437/0000378416"],
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"class": ["newsct_article _article_body", "media_end_head_title"]},
        )
    ),
)
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = splitter.split_documents(docs)


# ✅ 벡터 저장소 및 검색기
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(splits, embedding)
retriever = vectorstore.as_retriever()


# ✅ 프롬프트 및 LLM
prompt = hub.pull("teddynote/rag-prompt-korean")
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro",
    temperature=0,
    convert_system_message_to_human=True
)


rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# ✅ ChatInterface에 맞춘 응답 함수
def chat_with_news(message, history):
    try:
        retrieved_docs = retriever.invoke(message)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        prompt_input = prompt.invoke({"context": context, "question": message})
        response = llm.invoke(prompt_input)
        answer = StrOutputParser().invoke(response)
        return answer
    except Exception as e:
        return f"❌ 오류 발생: {e}"


# ✅ Gradio ChatBot UI 실행
chatbot_ui = gr.ChatInterface(
    fn=chat_with_news,
    title="📰 Gemini 뉴스 QA 챗봇",
    chatbot=gr.Chatbot(height=400),
    examples=["이 뉴스의 핵심은 무엇인가요?", "출산 관련 정책이 뭐였어요?", "지자체에서 어떤 지원을 하나요?"],
    theme="soft"
)


chatbot_ui.launch(share=True, server_name="0.0.0.0")
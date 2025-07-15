# LangChain & Context 7 샘플 코드
# 프롬프트 체인, 대화 이력 활용, 에이전트 예시

# 1. LangChain 기본 프롬프트 체인 샘플
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}"),
])
llm = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | llm | StrOutputParser()

if __name__ == "__main__":
    print("[1] 프롬프트 체인 샘플 결과:")
    result = chain.invoke({"question": "Context 7이란 무엇인가요?"})
    print(result)

    # 2. 대화 이력(Context 7) 활용 예시
    from langchain.prompts import MessagesPlaceholder
    print("\n[2] 대화 이력 활용 샘플 결과:")
    template = """Be helpful and answer the question below using the provided context:"""
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{question}"),
        ]
    )
    chat_history = [
        ("user", "Context 7이 뭔가요?"),
        ("assistant", "Context 7은 문맥 정보를 활용하는 프레임워크입니다."),
    ]
    result2 = answer_prompt | llm
    output2 = result2.invoke({"chat_history": chat_history, "question": "어디에 쓸 수 있나요?"})
    print(output2)

    # 3. LangChain Agent(에이전트) 샘플
    print("\n[3] 에이전트 샘플 결과:")
    try:
        from langgraph.prebuilt import create_react_agent
        from langchain_naver_community.tool import NaverNewsSearch
        tools = [NaverNewsSearch()]
        system_prompt = "You are a helpful assistant that can search the web for information."
        agent_executor = create_react_agent(
            llm,
            tools,
            prompt=system_prompt,
        )
        query = "서울의 오늘 날씨 알려줘"
        result3 = agent_executor.invoke({"messages": [("human", query)]})
        print(result3["messages"][-1].content)
    except ImportError:
        print("(에이전트 샘플 실행을 위해서는 langgraph, langchain_naver_community 패키지가 필요합니다.)") 
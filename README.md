 1) Cursor AI 설치
 2) Cursor AI 기초 사용법
 3) Cursor AI 랜딩 페이지 제작

Ctrl + L : 새 채팅
Ctrl + K : 그 자리에서 채팅

 agent -> python

### 환경 구축
1. 커서AI 설치 
2. 순수 파이썬 설치
3. Node.js
- 커서ai 자체의 한계라기보다는 언어 모델의 한계 ( 문맥 )
    ㄴ 브라우저를 띄워서 검색을 시키거나 , 최신 코드 예시를 불러오지 못하는 함정이 존재.
    ㄴ MCP Server를 띄우기 위해서 노드 설치함.  
    ㄴ MCP란, LLM에게 도구를 쥐어주는 것. (API를 붙여주는 것과 같은 효과 )

설치한 확장팩  Live Server

### 4. MCP 서버 설정
- 커서 AI 언어 모델의 기능을 확장 시키기 위함


Unautorized Error
- cmd 를 관리자 권한으로 실행
- cd Desktop/llm-project
- npx 명령어 실행

Ctrl + Shift + P => View : open mcp Tools

1) Context7
ㄴ LangChain 샘플 코드를 작성하는데, Context 7을 사용해

2) Playwright
ㄴ Playwrigth를 사용해서 네이버로 이동 후, 현대모비스 검색해

3) FireCrawl
ㄴ 검색엔진을 통해서 자료 서칭을 도와주는 목적
    ㄴ 네이버 부동산에서 헤리오시티 매물 수집해서 csv로 전달해줘.

    ->  채팅에서 실행 시, 모두 401 Error 발생.
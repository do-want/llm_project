import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

st.set_page_config(page_title="Google Scholar 논문 수집기", layout="wide")

st.title("📚 Google Scholar 논문 수집기")
query = st.text_input("🔍 검색어를 입력하세요:", value="LLM")
page_count = st.slider("📄 수집할 페이지 수 (1페이지당 10개 논문)", min_value=1, max_value=5, value=2)

if st.button("데이터 수집 시작"):
    st.info("브라우저를 통해 Google Scholar에서 데이터를 수집 중입니다...")

    # 크롬 드라이버 설정
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 헤드리스 X
    driver = webdriver.Chrome(options=options)

    results = []

    for i in range(page_count):
        start = i * 10
        url = f"https://scholar.google.co.kr/scholar?start={start}&q={query}&hl=ko&as_sdt=0,5"
        st.write(f"🔗 수집 중: [페이지 {i+1}]({url})")
        driver.get(url)
        time.sleep(2)

        papers = driver.find_elements(By.CSS_SELECTOR, "div.gs_r.gs_or.gs_scl")

        for paper in papers:
            try:
                title_tag = paper.find_element(By.CSS_SELECTOR, "h3.gs_rt a")
                title = title_tag.text
                link = title_tag.get_attribute("href")
            except:
                title = "(제목 없음)"
                link = ""

            try:
                authors_info = paper.find_element(By.CSS_SELECTOR, "div.gs_a").text
            except:
                authors_info = ""

            try:
                summary = paper.find_element(By.CSS_SELECTOR, "div.gs_rs").text
            except:
                summary = ""

            try:
                pdf_tag = paper.find_element(By.CSS_SELECTOR, "div.gs_or_ggsm a")
                pdf_link = pdf_tag.get_attribute("href")
            except:
                pdf_link = ""

            results.append({
                "제목": title,
                "링크": link,
                "PDF 링크": pdf_link,
                "저자 및 출처": authors_info,
                "요약": summary
            })

    driver.quit()

    # 결과 데이터프레임
    df = pd.DataFrame(results)

    st.success(f"총 {len(df)}개의 논문을 수집했습니다.")

    # 표로 결과 보여주기
    st.dataframe(df)

    # CSV 다운로드 버튼
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📁 CSV 다운로드",
        data=csv,
        file_name=f"scholar_{query}.csv",
        mime='text/csv'
    )

## pip install streamlit
## streamlit run google_get_scholar.py

#  streamlit 은 위 방법으로 실행해야 한다.
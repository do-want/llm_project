from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# 1. 크롬 드라이버 옵션 설정 (일반 모드)
options = Options()
# options.add_argument('headless')  # 헤드리스 모드 X

# 2. 드라이버 실행
driver = webdriver.Chrome(options=options)
url = "https://new.land.naver.com/complexes/112232?ms=37.395645,127.11368,17&a=APT:ABYG:JGC:PRE&e=RETAIL"
driver.get(url)
print("페이지 접속 완료")

# 3. 페이지 로딩 대기 (필요시 조정)
time.sleep(5)

# 4. 매물 정보 수집
items = driver.find_elements(By.CSS_SELECTOR, "div.item")
print(f"매물 {len(items)}건 발견")

data = []
for idx, item in enumerate(items, 1):
    try:
        title = item.find_element(By.CSS_SELECTOR, ".item_title .text").text
        price = item.find_element(By.CSS_SELECTOR, ".price_line .price").text
        apt_type = item.find_element(By.CSS_SELECTOR, ".info_area .type").text
        spec1 = item.find_element(By.CSS_SELECTOR, ".info_area .spec").text
        agent = item.find_element(By.CSS_SELECTOR, ".cp_area .agent_name").text
        print(f"{idx}: {title}, {price}, {apt_type}, {spec1}, {agent}")
        data.append({
            "매물명": title,
            "가격": price,
            "유형": apt_type,
            "스펙": spec1,
            "중개사": agent
        })
    except Exception as e:
        print(f"{idx}번 매물 정보 추출 실패: {e}")

# 5. DataFrame으로 변환 및 CSV 저장 (한글 인코딩)
df = pd.DataFrame(data)
df.to_csv("naver_land_estate_data.csv", index=False, encoding="utf-8-sig")
print("CSV 저장 완료")

# 6. 드라이버 종료
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# 크롬 드라이버 설정
options = Options()
options.add_argument('--start-maximized')  # 일반 모드

driver = webdriver.Chrome(options=options)

# 페이지네이션 기반 URL 템플릿
base_url = "https://madangs.com/search/npl?npl_group_code=&addr=&use_type=&sort=view_desc&start_date=&end_date=&share=2&progress_type=1&page={}"

# 최종 수집 결과
data_list = []
page = 0
step = 60  # madangs는 60단위 페이지네이션 사용

while True:
    url = base_url.format(page)
    driver.get(url)
    time.sleep(3)  # 페이지 로딩 대기

    items = driver.find_elements(By.CSS_SELECTOR, "a.mul_list")
    print(f"\n📄 Page {page} | 항목 수: {len(items)}")

    # 항목이 없으면 종료
    if len(items) == 0:
        print("⛔ 더 이상 항목이 없습니다. 크롤링을 종료합니다.")
        break

    for item in items:
        try:
            court = item.find_element(By.CSS_SELECTOR, ".mul_top_wrapper span:nth-child(1)").text.strip()
            case_number = item.find_element(By.CSS_SELECTOR, ".mul_top_wrapper span:nth-child(2)").text.strip()
            d_day = item.find_element(By.CSS_SELECTOR, ".mul_top_wrapper span:nth-child(3)").text.strip()
            address = item.find_element(By.CSS_SELECTOR, ".mul_address").text.strip()
            area = item.find_element(By.CSS_SELECTOR, ".mul_area").text.strip()
            eval_price = item.find_element(By.CSS_SELECTOR, ".mul_eval_price").text.strip()
            last_price = item.find_element(By.CSS_SELECTOR, ".mul_last_price").text.strip()
            try:
                special_note = item.find_element(By.CSS_SELECTOR, ".mul_special_right_wrapper span").text.strip()
            except:
                special_note = ""
            usage_type = item.find_element(By.CSS_SELECTOR, ".mul_list_use_type").text.strip()
            view_count = item.find_element(By.CSS_SELECTOR, ".mul_list_view_count").text.strip().replace("view", "").strip()
            img_url = item.find_element(By.CSS_SELECTOR, ".mul_img").get_attribute("src")

            print(f"✅ {case_number} | {address} | {last_price}")

            data_list.append({
                "사건번호": case_number,
                "법원명": court,
                "D-Day": d_day,
                "주소": address,
                "면적": area,
                "감정가": eval_price,
                "최저가": last_price,
                "유찰여부": special_note,
                "용도": usage_type,
                "조회수": view_count,
                "이미지": img_url
            })

        except Exception as e:
            print("❌ 항목 수집 중 오류:", e)
            continue

    page += step  # 다음 페이지로 이동

# 드라이버 종료
driver.quit()

# DataFrame 저장
df = pd.DataFrame(data_list)
df.to_csv("madangs_auction_list.csv", index=False, encoding="utf-8-sig")
print("\n✅ 전체 수집 완료 및 CSV 저장: madangs_auction_list.csv")

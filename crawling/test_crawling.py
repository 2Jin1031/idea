from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# 웹드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 메인 페이지로 이동
driver.get("https://www.inflearn.com/")

# 로그인 버튼 클릭 (로그인 버튼의 정확한 위치를 지정합니다)
login_button_xpath = '//*[@id="header"]/nav/div[1]/div/div[3]/button[1]'
driver.find_element(By.XPATH, login_button_xpath).click()

# 사용자가 수동으로 로그인 정보를 입력할 시간을 제공
time.sleep(180)  # 예를 들어, 3분간 대기

# 이후에 필요한 페이지로 이동하거나 추가 작업 수행
# 예: 특정 페이지로 이동
driver.get("https://www.inflearn.com/course/lecture?courseSlug=http-%EC%9B%B9-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC&unitId=61353&tab=script")

# Wait for the page to load and extract data
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
target_info = soup.find_all("p", {"class": "mantine-Text-root script-item-text css-y5z5j6 mantine-bf5u4f"})
for item in target_info:
    print(item.text)

# Close the browser
driver.quit()

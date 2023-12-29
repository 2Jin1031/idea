'''
import requests
import json


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# login data
LOGIN_URL = urlopen('https://ecampus.sejong.ac.kr/login.php')
USERNAME = '22011531'
PASSWORD = 'i.t.s.g.1+'

# session maintenance
session = requests.Session()

# login request
login_data = {
    'username' : USERNAME,
    'password' : PASSWORD
}
response = session.post(LOGIN_URL, data=login_data,verify=False)

# logion maintenance
if response.status_code == 200:
    print('login success')
else:
    print('login failure')

# crawling
CRAWLING_URL = urlopen("https://ecampus.sejong.ac.kr")
header = {'User-gent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'}
requests.get(CRAWLING_URL, headers=header, verify= False)
response = requests.get(CRAWLING_URL).text
print(response)

'''
'''
# Sol 2
html = urlopen("https://ecampus.sejong.ac.kr")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject)
'''
import requests
from bs4 import BeautifulSoup
      
# #세션만들기
# session=requests.session()
#로그인 하는 페이지의 general-requestURL에서 url 가져옴
url="https://ecampus.sejong.ac.kr/login.php"
      
#가져오고 싶은 데이터 (form data)
data={
    "return_url":"https://ecampus.sejong.ac.kr/dashboard.php",
    "m_id":"22011531",
    "m_passwd":"i.t.s.g.1+"
          
}
response=session.post(url, data=data, verify=False) #요청을 모방하면됨 (get, post, put 등)
      
#로그인 실행
response.raise_for_status()
      
      
#마이페이지 접근
url="https://ecampus.sejong.ac.kr/dashboard.php"
response=session.get(url, verify=False)
response.raise_for_status()
#print(response.text)
      
#HTML분석 (이코인 가져오기)
soup=BeautifulSoup(response.text,"html.parser")
#container > div > div.sm_mymileage > dl.mileage_section2 > dd
text=soup.select_one(".mileage_section2 span").get_text()
print("이코인:",text)
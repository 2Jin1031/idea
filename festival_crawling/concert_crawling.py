from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
#import requests

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://m.place.naver.com/place/12268494/ncr/performance"
#response = requests.get(url, verify=False)

html_data = urlopen(url)

#데이터가 잘 불러와 오는지 확인 -> sucess
#print(html_data.read())


ext_data = BeautifulSoup(html_data, "html.parser")

## h2 형태의 title 출력해보는 코드
#title = ext_data.find_all("h2")
#
#for var in title :
#   print(var.text)


## 데이터 가공하기
#festival_info = ext_data.find_all("div", {"class":"text"})
consert_info = ext_data.find_all("div", {"class":"SViKF"})

for consert in consert_info:
    print(consert.text)



'''
for festival in festival_info:
    title = festival.find("p", {"class":"title"}).text
    place = festival.find("ul", {"class":"detail_info"}).text
    place = re.sub('\s+', ' ', place)
    print("제목: ", title)
    print("장소: ", place)

'''
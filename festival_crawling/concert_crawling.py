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
print(html_data.read())

'''
ext_data = BeautifulSoup(html_data, "html.parser")
#title = ext_data.find_all("h2")


# ''
#for var in title :
#    print(var.text)
# ''

festival_info = ext_data.find_all("div", {"class":"text"})

for festival in festival_info:
    title = festival.find("p", {"class":"title"}).text
    place = festival.find("ul", {"class":"detail_info"}).text
    place = re.sub('\s+', ' ', place)
    print("제목: ", title)
    print("장소: ", place)

'''
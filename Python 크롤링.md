# Python 크롤링

- KOSPI 불러오기

```shell
import requests
from bs4 import BeautifulSoup 

url = "https://finance.naver.com/sise/"

# request = requests.get(url)
# print(request) # 200 은 성공적으로 잘 접속했다.

request = requests.get(url).text# html 소스코드 받아오기
#가져온 html 코드를 parsing 한다/python이 compile할수 있도록
soup = BeautifulSoup(request,'html.parser')
#print(soup) 한글때문에 unicode err 뜰수도!
kospi = soup.select_one('#KOSPI_now')
#소스코드 중 #KOSPI_now 이름을 가진 친구 하나만 골라줘
print(kospi.text)
```

- 달러환율 불러오기

```shell
import requests
from bs4 import BeautifulSoup 

url = "https://finance.naver.com/marketindex/"

req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')

exc = soup.select_one('#exchangeList .value')
# #은 id값
# .은 class값
# 바로 내부는 > 부모형제의 경우
# 바로 내부 아닌 경우에는 띄어쓰기 
print(exc.text)
```

- 네이버 실시간 검색어 불러오기

```shell
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

req = requests.get(url).text
data = BeautifulSoup(req,'html.parser')

#이부분 연습해야할 듯

sel = '#PM_ID_ct .ah_l .ah_k'
search = data.select(sel)

for item in search:
    print(item.text)
```
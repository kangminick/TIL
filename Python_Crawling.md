# Python 크롤링

### 1. 가상환경 만들기

> - venv: 가상 환경을 만들고 관리하는데 사용되는 모듈
> - pip: 파이썬으로 설치한 패키지를 관리하는 시스템으로, 패키지를 설치, 업그레이드 및 제거할 수 있음

`python -m venv venv`: **venv** 가상환경 만들기

`source venv/Scripts/activate`: 가상환경 활성화

`deactivate`: 가상환경 종료

`pip list`: 현재 추가된 가상환경 내에 라이브러리 목록을 보여줌

### 2. 패키지 설치

> - requests: Python에서 HTTP 요청을 보내는 라이브러리
> - BeautifulSoup: HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 할 수 있는 라이브러리

`pip install requests`: requests 패키지 설치

```python
import requests
```

`pip install beautifulsoup4`: beautifulsoup4설치

```python
from bs4 import BeautifulSoup
```

### 3. 웹 크롤링

`request.get(url).text`: *url*주소의 html을 반환

`BeautifulSoup(request, 'html.parser')`: html을 파싱해줌 (xml 등 가능)

- KOSPI 불러오기

```python
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

```python
import requests
from bs4 import BeautifulSoup 

url = "https://finance.naver.com/marketindex/"

req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')

#class를 가져올 때 상위의 id를 선택해주자
exc = soup.select_one('#exchangeList .value')
# #은 id값
# .은 class값
# 바로 내부는 > 부모형제의 경우
# 바로 내부 아닌 경우에는 띄어쓰기 
print(exc.text)
```

- 네이버 실시간 검색어 불러오기

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

req = requests.get(url).text
data = BeautifulSoup(req,'html.parser')

#이부분 연습해야할 듯

sel = '#PM_ID_ct .ah_l .ah_k'
search = data.select(sel) #모든 요소를 리스트로 반환

for item in search:
    print(item.text)
```
# Python

> 프로그래밍 언어 : 3형식(저장, 조건, 반복)
>
> 대/소문자, 띄어쓰기, 스펠링에 유의한다.

## (1) 저장

### (1-1) 변수 선언, 출력, 타입

```python
number = 123
number_two = -456
number_three = 7.89

print(number)
print(number_two)
print(number_three)
print(number, number_two, number_three)

a = 'ABC'
b = '123'
c = 123
print("Hellow world")
print(a, b, c, 123)
print(type(b), type(c), type(123))

d = True
e = False
print(d, e, type(d), type(e))
```

### (1-2) List, Array

```python
array = [1,2,3, "four", "five",  "six", True]
print(array) #[1, 2, 3, 'four', 'five', 'six', True]
print(array[0:3]) #[1, 2, 3]
print(array[4:]) #['five', 'six', True]
print(array[-1]) #True

dust = {'seoul' : 50, 'incheon' : 40} 
print(dust) #{'seoul': 50, 'incheon': 40}
print(dust['seoul']) # 50

dust_two = dict(seoul=50)
print(dust_two) #{'seoul': 50}
print(dust_two['seoul']) # 50


import random

menu = ['20층', '양자강']

phone_book = {'20층' : '010-1234-1234', '양자강' : '010-321-3211'}
ch = random.choice(menu)

print(ch, phone_book[ch])
```

## (2) 조건

### (2-1) IF

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'.format(key)
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
item = soup('item')[5]
time = item.dataTime.text
dust = int(item.pm10Value.text)

# dust 변수에 들어 있는 내용을 출력해보세요.
print('{} 기준 미세먼지 농도는 {}입니다.'.format(time, dust))
# print(f'{time} 기준 미세먼지 농도는 {dust}입니다.') 위와 같은 코드.

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해부세요.
# naver 미세먼지 기준 참고.
if dust <= 30 :
  print("미세먼지 상태 좋음")
elif dust > 30 and dust <= 80 :
  print("미세먼지 상태 보통")
elif dust > 80 and dust <= 150 :
  print("미세먼지 상태 나쁨")
else :
  print("미세먼지 상태 매우나쁨")
```

### (2-2) While

```python
while n < 3 :
    print('출력')
    n = n + 1
    
while n < 3 :
    n = 2 + 1
    print('출력') #출력된다.
    
#  break로 끝낸다    
```

### (2-3) For

```python
numbers = list(range(10))
print(numbers)

for number in numbers :
    print(number)
```


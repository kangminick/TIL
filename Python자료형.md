## 몰랐던 Python의 특징

```python
# 1. 5개 과목의 점수 합계와 평균 구하기.
sum = 80 + 66 + 73 + 90 + 94
ave = sum / 5
print('총점 ' + str(sum) + '점') # +로 연결가능
print('평균', str(ave),  '점') # ,로 연결가능 이때 띄어쓰기 한칸이 자동적용됨.
```

- print()에서  '+'와 ','가 비슷한 역할을 해준다.

```python
print('{0:<10}'.format('1234')) #'1234'
print('{0:>10}'.format('1234')) #' 1234'
print('{0:^10}'.format('1234')) #' 1234 '
print('{0:공^10}'.format('1234')) #'공공공1234공공공'
print('{0:!^10}'.format('1234')) #'!!!1234!!!'

name = 'ggoreb'
f'name is {name}' # 'name is ggoreb'

age = 10
f'10년 후 나이 {age + 10}살' # '10년 후 나이 20살'

f'{{ }}' #'{ }'
```

- formatting을 통해 문자열의 여백, 정렬이 가능하다.

```python
str = 'Life is too short, YOu need Python'

str.count('i') # 2 특정 문자의 개수를 찾아준다.
str.find('i') # 1 특정 문자의 위치를 찾아준다.
str.fine(',8,12') # 11 8번째 자리와 12번째 자리 사이의 ''위치
str.index('i') # 1 특정 문자의 위치를 찾아준다.
str.index(',8,12') # 11 8번째 자리와 12번째 자리 사이의 ''위치

str = '12345'
sep = ','

sep.join(str) # '1,2,3,4,5' join()은 각 문자 사이에 문자를 삽입할 수 있게 한다.
```

- 이외에도 str.strip() : 공백 제거, str.replace('','') : 문자열 치환
- str.split('') : 특정 문자열을 기준으로 전체 문자열을 List로 변경

```python
#List 관련 함수

list.append() #마지막 요소로 추가, 리스트를 추가하면 중첩으로 리스트가 추가된다.
list.insert() #(위치, 요소) 지정 위치에 요소 추가
list.extend() #마지막 요소로 추가, 리스트를 추가하면 중첩되지 않고 병합된다.
list.remove() #첫번째로 등장하는 지정요소를 제거
list.pop() #지정된 위치의 요소를 추출하면서 제거 (기본 위치는 마지막)
list.sort() #오름차순 정렬
list.sort(reverse=True) #내림차순 정렬
list.reverse() #현재 상태의 반대로 정렬
```

- 이외에도 문자열과 마찬가지로 index(), count() 사용 가능.

### Tuple

>List와 유사하지만  기존 요소를 수정, 삭제가 불가능하다.
>
>그럼에도 사용하는 이유는 List에 비해 더 적은 메모리를 사용하기 때문이다. (속도빠름)
>
>수정이 안되므로 더 안정적이고 프로그래머의 실수를 방지할 수 있다.

```python
tuple1 = ('a',) #요소가 한개인 경우 반드시 ,를 붙여야한다.
tuple2 = 1,2,3 #요소가 여러개인 경우 괄호 생략 가능하다.
```

### Dictionary

>여러개의 자료를 하나로 묶어 사용할 수 있는 자료형이다.
>
>{key:value, key:value,,,,,,,}의 형태를 가지고 있다.
>
>Key는 고유하고 변경이 불가능하다.

```python
#Dictionary 관련 함수

dict.keys() : key의 목록 확인
dict.values() : value의 목록 확인
dict.items() : key, value 목록 확인
dict.clear() : 모든 데이터 삭제
dict.get() : key를 이용하여 value 조회
'key값' in dict #Dictionary 요소 중 해당하는 key가 있는지 확인
```

### Set

> 여러개의 자료를 하나로 묶어 사용할 수 있는 자료형
>
>겉모습은 dict, 내부 요소는 List와 유사
>
>각 요소에 순서는 없으며 중복값을 허용하지 않음 (중복을 제거하기 위한 필터 역할로 사용가능)  ex) list를 set으로 바꾸었다가 다시 list로 바꾸면 기존에 중복들이 사라짐.

```python
#set 관련 함수

setname1.intersection(setname2) #교집합 a & b와 같음
setname1.union(setname2) #합집합 a | b
setname1.difference(setname2) #차집합 a - b

setname.add() # 하나의 값 추가
setname.update() # 여러개의 값 추가
setname.remove() # 지정값 제거
```

- 요소 복사 list3 = list1[:] , import copy  list3 = copy.copy(list1)
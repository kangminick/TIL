## Python 

### **자료형**

● 숫자 (Number) - 123, 1.23, -97, -3.14e10

​	제곱 연산 (a ** b) : a의 b 제곱 연산



● 문자 (String) - 'A', 'Hello', '888', '-17'

```python
>>> str = 'Hello Python' 

>>> str[0] 'H'

>>> str[6] 'P' 

>>> str[-1] 'n' 

>>> str[-6] 'P' 

>>> str[-12] 'H'
```

```python
>>> str = 'Hello Python'
>>> str[0:]
'Hello Python'
>>> str[6:]
'Python'
>>> str[:6]
'Hello '
>>> str[:-4]
'Hello Py'
>>> str[6:-4]
'Py
```

● Formatting : 문자열의 특정 부분만 바꿔 사용 

- 동적으로 입력되는 부분에 특수코드 사용 

- 여러개의 값을 넣는 경우 () 와 , 를 이용하여 구분

  %s 문자열 (string) 	%c 문자 (character) 	%d 정수 (integer) 

  %f 실수 (float) 	%o 8진수 	%x 16진수 	%% % 문자

```python
>>> 'Python version %d' % 1
'Python version 1'
>>> 'Python version %d' % 3
'Python version 3'
>>> 'Python version %s' % 'lastest'
'Python version lastest'
>>> 'Python version %f' % 3.6
'Python version 3.600000'
>>> 'Python version %d%%' % 100
'Python version 100%'
>>> '%s version %d' % ('Python', 3)
'Python version 3
```

 ● format 함수 이용

\- {index}

```python
>>> 'score {0}'.format(100)
'score 100'
>>> 'score {0}, {1}'.format(100, 80)
'score 100, 80'
>>> '{0} {1}'.format('score', 70)
'score 70'

```

\- {name}

```python
>>> '{lang} is easy'.format(lang='Python')
'Python is easy'
>>> '{lang} is easy, version {ver}'.format(ver=3.6, lang='Python')
'Python is easy, version 3.6'

```

\- {index}, {name} 혼용 사용

```python
>>> '{lang} is easy, version {0}.{1}'.format(3, 6, lang='Python')
'Python is easy, version 3.6'
```

\- 여백 및 정렬

```python
>>> '{0:<10}'.format('1234')
'1234 '
>>> '{0:>10}'.format('1234')
' 1234'
>>> '{0:^10}'.format('1234')
' 1234 '
>>> '{0:공^10}'.format('1234')
'공공공1234공공공'
>>> '{0:!^10}'.format('1234')
'!!!1234!!!'
```

\- f 문자열 Formatting

```python
>>> name = 'ggoreb'
>>> f'name is {name}'
'name is ggoreb'
>>> age = 10
>>> f'10년 후 나이 {age + 10}살'
'10년 후 나이 20살'
>>> f'{{ }}'
'{ }'
```



● List : 수정 가능 - [1, 2, 3], ['H', 'e', 'l', 'l', 'o'] 

● Tuple : 수정 불가 - (1, 2, 3), ('H', 'e', 'l', 'l', 'o') 

● Dictionary - {'a' : 10, 'b' : 20}, {'seoul' : '서울', 'busan' : '부산'} 

● Set - {1, 2, 3}, {'H', 'e', 'l', 'l', 'o'}

 ● 논리 (Bool 또는 Boolean) - True, False
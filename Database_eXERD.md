# 데이터베이스 eXERD

### 1. exerd설치

이클립스 플러그인으로 설치: http://ko.exerd.com/down.jsp#a3

eclipse에서 [help] > install new software

work with: 주소 붙여넣기 > enter > contact all update 체크해제

### 2. exerd 사용하기

파일생성: new- other - exerd

- 대상 DB > mysql
- 파일명 무관

비식별 관계 > 외래키 생성

식별 관계 > 외래키를 기본키로 사용할 때

속성 > 관계 > 물리속성 > 외래키 삭제시:cascade 설정

### 3. 포워트 엔지니어링하기

> 포워드 엔지니어링: eXERD > 포워드 엔지니어링

1. mysql-conncetor/j 설치

'mvn repository' 사이트에 mysql검색: mysql-connector/j (5.1.48버전)

https://mvnrepository.com/artifact/mysql/mysql-connector-java/5.1.48

1. DB연결

window > preferences > eXERD > DBMS 연결 설정 > 새연결

[![img](https://user-images.githubusercontent.com/58925328/72959900-59207980-3def-11ea-98f1-a00e10314990.PNG)](https://user-images.githubusercontent.com/58925328/72959900-59207980-3def-11ea-98f1-a00e10314990.PNG)

1. 포워드 엔지니어링

포워드 엔지니어링 > 이름앞에 스키마표시 제거

## 파이썬에서 DB사용

```python
import pymysql

conn=pymysql.connect(
    host='localhost', user='root', password='1146',
    db='python', charset='utf8'
)

cursor=conn.cursor()
sql='''CREATE TABLE mysql(
        id INTEGER PRIMARY KEY AUTO_INCREMENT
        , title VARCHAR(100), content VARCHAR(100))'''

cursor.execute(sql)

conn.commit()

# close 꼭 해주기
cursor.close()
conn.close()
```

- insert, update, delete는 아래와 같이 사용가능

```python
import pymysql

conn=pymysql.connect(
    host='localhost', user='root', password='1146',
    db='python', charset='utf8'
)

cursor=conn.cursor()
sql='''INSERT INTO mysql (id, title, content) VALUES (null, %s, %s)'''


cursor.execute(sql,('제목A', '내용Z'))

conn.commit()
cursor.close()
conn.close()
```

- select는 일단 execute를 실행시킨후 fetch() / fetchall()사용

```python
import pymysql

conn=pymysql.connect(
    host='localhost', user='root', password='1146',
    db='python', charset='utf8'
)

cursor=conn.cursor()
sql='''SELECT * FROM MYSQL'''
cursor.execute(sql)
result= cursor.fetchall()
print(result)
print(result[0])
print(result[0][1])

conn.commit()
cursor.close()
conn.close()
```
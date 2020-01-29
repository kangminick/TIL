# 데이터베이스

> MariaDB 이용

대표적인 DB

MariaDB(=MySQL), Oracle, MS-SQL

명령어: SQL (Structured Query Language)

 ANSI SQL

Server Client

WebServer(Spring) <-> Browser

DBServer(MariaDB) <-> Tool (**HeidiSQL** 또는 WorkBench)

Create

Read

Update

Delete

### 설치

1. maria db: https://mariadb.com/downloads/

   ver 10.4.11

   설치할때 utf8과 외부공유 체크!

`mysql -u root -p`: cmd로 실행하기

```
show databases
exit
```

### 데이터베이스

주요 기능: 정의, 조작, 제어

모델링

개체: 연결되는 기준

key: **기본키**, 대체키, 후보키, 슈퍼키, 외래키

- 기본키로 존재해야 외래키로 존재할 수 있음.
- 기본키를 삭제해야할 때 외래키도 같이 삭제함

## SQL

> **관계형 데이터베이스**를 위한 표준 질의어

DDL: 데이터 정의어. 테이블 생성/변경/제거

DML: 데이터 조작어

DCL: 데이터 제어어. 권한부여하기.

### 1. DDL

대소문자를 구분하지 않음

정형데이터, 생성시 속성을 정해놓음.

null값을 허용하는지 정해놔야함.

```
-- primary key 지정해주기
CREATE TABLE 연습1(
	이메일 VARCHAR(20),
	비밀번호 VARCHAR(20),
	나이 INT,
	PRIMARY KEY (이메일)
);
```

외래키

제약조건명이 있음

기본키가 삭제되었을 때 외래키도 삭제하라는 옵션

명칭은 달라도 상관없음

참조만 가능. 수정은 불가

CASCADE: 기본키가 삭제되면 외래키도 삭제

SET NULL: 기본키가 삭제되면 외래키는 NULL

`DESC [테이블명]`: 테이블 내용 조회

제약조건 변경하기

제약조건 명칭 조회 > information_schema DB

```
-- 제약조건 명칭 조회
-- 제약조건 삭제
-- 제약조건 입력
SELECT * FROM information_schema.TABLE_CONSTRAINTS
-- EMP_IBFK_1 제약조건 명칭
ALTER TABLE EMP DROP EMP_IBFK_1;

ALTER TABLE EMP ADD
	CONSTRAINT FK_EMP_DEPT
	FOREIGN KEY (DEPTNO) REFERENCES DEPT(DEPTNO)
	ON DELETE CASCADE;
```

### 2. DML

```
INSERT INTO 부서(부서번호, 부서이름) VALUES (1,'인사부');
```

`select * from [테이블명]` : 프로젝트할때는 *를 모두 적어주자

`SELECT DISTINCT [속성] FROM [테이블명];` 중복없이 검색

`SELECT 제품명, 단가 AS '가격' FROM 제품;` 단가를 '가격'이라는 이름으로 조회

 통계를 이용하는 등 없던 데이터를 넣어줄 때 많이 사용

`SELECT sal*1.1 + IFNULL(comm,0) FROM emp;`null일때 0으로 치환해서 계산.

LIKE: 부분적으로 일치하는 데이터 검색. %와 함께 사용됨.

`SELECT * FROM 고객 WHERE 나이 IS NULL;`null은 =가 안먹힘. is와 is not을 사용

csv파일 데이터베이스에 저장하기

열의 생성해줘야함

도구 > csv파일 가져오기

엑셀의 문자열을 합쳐주는 함수: concatenate()
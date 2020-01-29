# 데이터베이스 함수&서브쿼리

## 함수

substr

concat

sql은 문자열 index는 1부터

```sql
-- 프로그래밍 언어에서 해당 명령문이 실행안됨--
SELECT * FROM emp WHERE ename LIKE '%A%';

-- 대체 명령문--
SELECT * FROM emp WHERE ename LIKE CONCAT('%','A','%');
SELECT *,
	CASE DEPTNO
		WHEN 10 then '총무'
		when 20 then '운영'
		ELSE '기타' end
	FROM emp;
```

통계함수 사용시 ifnull()을 활용.

```sql
-- 제품명은 max의 영향을 받지 않으므로 잘못된 명령어임
SELECT MAX(재고량), 제품명 FROM 제품;

-- 서브쿼리를 이용
SELECT * FROM 제품 WHERE 재고량= (
		SELECT MAX(재고량) FROM 제품
);
```

count()할때 null은 제외됨을 주의하자

```sql
-- 모든 열의 개수를 count하고 싶을 때는 아래와 같이
SELECT COUNT(*) FROM 고객;
SELECT COUNT(1) FROM 고객;
```

분류하여 통계하고 싶을 때

**GROUP BY()**

```sql
-- GROUP BY 사용시 GROUP할 속성 또는 집계 함수
SELECT 제조업체, count(제조업체) FROM 제품 
	GROUP BY 제조업체;
```

- having
- 여러 항목에 중복 적용가능

```sql
-- 한글이 깨질때 convert()사용
-- 또는 cast(    as varchar())

SELECT company, convert(concat(COUNT(*),'개') USING utf8) "COUNT" 
  FROM noodle
 GROUP BY company;
```

join()

일반적으로 외래키가 조인 속성으로 사용됨

join하는 두가지 방법

```sql
-- 방법1. where사용
SELECT * 
	FROM emp, dept
	WHERE emp.DEPTNO= dept.DEPTNO;
	
-- 방법2. join ~ on 사용 (명시적으로 더 권장됨)
SELECT * 
	FROM emp
	JOIN dept
	ON emp.DEPTNO=dept.DEPTNO;
```

self조인: 자기자신과 조인.

outer조인

그냥 조인을 쓰면 null값은 모두 제거됨

outer조인을 이용해, 기준인 테이블의 행은 무조건 나오게함

참고:

데이터베이스는 열을 늘리지 않는다.

 > 데이터 추가는 행으로 이뤄져야함.

## 서브쿼리

서브쿼리는 무리가 될 수 있음

```sql
-- sub쿼리에서 두개이상이 나오면 오류.
SELECT * 
	FROM emp 
	WHERE sal=(
		SELECT * FROM emp WHERE sal=1250
	);

-- sub쿼리에서 두개이상 나온다면 IN 사용.
SELECT * 
	FROM emp 
	WHERE sal IN (
		SELECT sal FROM emp WHERE sal=1250
	);
--DCL
--rollback을 하기위해 설정되어 있어야함
SET @@AUTOCOMMit = 0;

-- 실수 되돌리기.
ROLLBACK;

-- 수정안되게 하기..?
COMMIT;
```
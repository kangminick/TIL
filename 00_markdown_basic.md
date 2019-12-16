# 마크다운

마크다운 문법 학습

## 1. 마크다운 문법

코드 블락

```java
public static void main(){
}
```

```javascript
console.log("hellow world");
```

``` html
<script>
    
</script>

```

## 인용문

> 인용문은 회색입니다. 옅지요.

## 리스트

순서가 있는 리스트(ordered list ol)

1. 이건 ol입니다.
2. 숫자가 자동으로 먹여집니다.
3. 야호

순서가 없는 리스트(unordered list)

- 이건 ul입니다.
- -를 쓰면 됩니다.
- 예스



# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하며 빠르게 문서 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1. 문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.

- `<h1>` 부터 `<h6>` 까지 표현합니다.
- #의 개수로 표현하거나 `<h1>``</h1>`의 형태로 표현 가능합니다.



# h1 태그입니다.

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5 태그입니다.

###### h6 태그입니다.



### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있으며 그 반대도 가능합니다.

- 순서가 없는 목록
  -  `1.`을 누르고 스페이스바를 누르면 생성할 수 있습니다.
  - tab 키를 눌러서 하위 항목을 생성할 수 있고 shift + tab 키를 눌러서 상위 항목으로 이동할 수 있습니다.
-  순서가 있는 목록
  -  -(하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다.
  - tab 키를 눌러서 하위 항목을 생성할 수 있고 shift + tab 키를 눌러서 상위 항목으로 이동 할 수 있습니다.



1. 순서가 있는 항목
2. 순서가 있는 항목
   1. 순서가 있는 하위 항목
   2. 순서가 있는 하위 항목



- 순서가 없는 항목
- 순서가 없는 항목
  - 순서가 없는 하위 항목
  - 순서가 없는 하위 항목



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline
  - 인라인 블럭으로 처리 하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block
  - `(백틱)을 3번 입력하고 Enter 를 눌러 생성합니다.



add 한 요소를 remote 저장소에 올리려면 $ git push origin master 를 터미널에 입력합니다.

```shell
$ git add .
$ git commit -m "first commit"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 이미지를 나타낼 때 사용합니다. 

- `![]()` 을 작성하고 ()안에 이미지 주소를 입력합니다. [] 안에는 이미지 파일의 이름을 작성합니다. 
- 로컬에 이미 파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.

![](data:image/png;base64,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)



![](data:image/png;base64,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)

### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

-  `[]()` 을 작성하고 () 안에 링크 주소를 작성하고 [] 안에 어떤 링크 주소인지 작성합니다.

[git 공식문서](https://drive.google.com/file/d/1s582bLrDx_Utn29d-DC0oUYyJJo4YWTv/view)

[github 공식문서](https://drive.google.com/file/d/1s582bLrDx_Utn29d-DC0oUYyJJo4YWTv/view)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

-  | (파이프) 사이에 컬럼을 작성하고 `enter`를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 | 를 붙여줍니다.



| working directory | Statging area | remoe repo |
| ----------------- | ------------- | ---------- |
| working tree      | index         | history    |
| working copy      | cache         | tree       |

​	

### 1.7 기타

##### 인용문

-  `>` 을 입력하고 `enter` 키를 누릅니다.

> git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

-  인용문 안에 인용문을 작성하면 중첩해서 사용할 수 있습니다.

> $ git add.
>
> > $ git commit - m "first commit"
> >
> > > $ git push origin master



##### 수평선

-  ---, ***, ___ 을 입력하여 작성합니다.

Working Directory 

***

Staging Area

***

Remote Repository

***



##### 강조

- 이텔릭체는 해당 부분을 * 혹은 _ (언더바) 로 감싸줍니다.
- 보드체는 해당 부분을 ** 혹은 __(언더바 2개)로 감싸줍니다,
- 취소선은 ~~ 표시를 사용합니다.

이것은 *이탤릭체*입니다.

이것은 **보드체**입니다.

이것은 ~~취소선~~입니다.



## 2. 과제

> 현재의 pdf 문서를 마크다운 문법을 활용하여 00_markdown_basic.md 로 만들어 보세요.

